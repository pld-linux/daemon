Summary:	Daemon turns other process into daemons
Summary(pl):	Daemon - zamiana innych procesów w demony
Name:		daemon
Version:	0.6.3
Release:	1
License:	GPL
Group:		Daemons
#Source0Download: http://libslack.org/daemon/
Source0:	http://libslack.org/daemon/download/%{name}-%{version}.tar.gz
# Source0-md5:	d2f3001b20bb035d55202f1945c0a0ee
URL:		http://libslack.org/daemon/
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Daemon turns other process into daemons. There are many tasks that
need to be performed to correctly set up a daemon process. This can be
tedious. Daemon performs these tasks for other processes.

%description -l pl
Daemon zamienia inne procesy w demony. Jest wiele zadañ, które trzeba
wykonaæ, aby poprawnie uruchomiæ demona. Mo¿e to byæ mêcz±ce. Daemon
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
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
