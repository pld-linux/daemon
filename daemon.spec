#
# Conditional build
%bcond_without	systemd	# systemd-logind support
%bcond_with	elogind	# elogind support

Summary:	Daemon turns other process into daemons
Summary(pl.UTF-8):	Daemon - zamiana innych procesów w demony
Name:		daemon
Version:	0.8.4
Release:	1
License:	GPL v2
Group:		Daemons
#Source0Download: https://libslack.org/daemon/#download
Source0:	https://libslack.org/daemon/download/%{name}-%{version}.tar.gz
# Source0-md5:	871ff0cc66b1eafbb17965b5ec164509
URL:		https://libslack.org/daemon/
%{?with_elogind:BuildRequires:	elogind-devel}
BuildRequires:	perl-tools-pod
%{?with_systemd:BuildRequires:	systemd-devel >= 1:209}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Daemon turns other process into daemons. There are many tasks that
need to be performed to correctly set up a daemon process. This can be
tedious. Daemon performs these tasks for other processes.

%description -l pl.UTF-8
Daemon zamienia inne procesy w demony. Jest wiele zadań, które trzeba
wykonać, aby poprawnie uruchomić demona. Może to być męczące. Daemon
wykonuje te zadania dla innych procesów.

%prep
%setup -q

%build
# not autoconf configure
CC="%{__cc}" \
./configure \
	--destdir=$RPM_BUILD_ROOT \
	--prefix=%{_prefix} \
%if %{with elogind} || %{with systemd}
	--enable-logind \
%endif
	--disable-mail-test

%{__make} \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags} -Wall -pedantic" \
	APP_INSDIR="%{_sbindir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	APP_INSDIR=%{_sbindir} \
	MAN_GZIP=0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md REFERENCES
%attr(755,root,root) %{_sbindir}/daemon
%{_mandir}/man1/daemon.1*
%{_mandir}/man5/daemon.conf.5*
