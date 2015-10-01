Summary:	Scripts for booting system
Name:		bootscripts
Version:	20150222
Release:	1
License:	GPLv3
URL:		http://www.linuxfromscratch.org/lfs
Group:		LFS/Base
Vendor:		Bildanet
Distribution:	Octothorpe
BuildArch:	noarch
Source0:	http://www.linuxfromscratch.org/lfs/downloads/development/lfs-%{name}-%{version}.tar.bz2
%description
The LFS-Bootscripts package contains a set of scripts to start/stop
the LFS system at boot up/shutdown.
%prep
cd %{_builddir}
tar xvf %{SOURCE0}
cd %{_builddir}/lfs-%{name}-%{version}
%build
%install
cd %{_builddir}/lfs-%{name}-%{version}
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_lib}/*
%{_mandir}/*
/sbin/*

%changelog
*	Sat Aug 24 2013 baho-utot <baho-utot@columbus.rr.com> 20130821-1
*	Thu May 16 2013 baho-utot <baho-utot@columbus.rr.com> 20130515-1
*	Wed May 15 2013 baho-utot <baho-utot@columbus.rr.com> 20130511-1
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 20130123-1
-	Upgrade version
