Summary:	Daemon turns other process into daemons
Summary(pl.UTF-8):	Daemon - zamiana innych procesów w demony
Name:		daemon
Version:	0.6.4
Release:	1
License:	GPL v2
Group:		Daemons
#Source0Download: http://libslack.org/daemon/
Source0:	http://libslack.org/daemon/download/%{name}-%{version}.tar.gz
# Source0-md5:	6cd0a28630a29ac279bc501f39baec66
URL:		http://libslack.org/daemon/
BuildRequires:	perl-tools-pod
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
conf/linux
%{__make} \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags}" \
	APP_INSDIR="%{_sbindir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	APP_INSDIR=$RPM_BUILD_ROOT%{_sbindir} \
	APP_MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	FMT_MANDIR=tmp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/daemon
%{_mandir}/man1/daemon.1*
