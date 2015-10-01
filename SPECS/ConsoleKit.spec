Summary:	Framework for keeping track of the various users, sessions, and seats present on a system.
Name:		ConsoleKit
Version:	0.4.6
Release:	1
License:	GPL
URL:		http://anduin.linuxfromscratch.org/sources/BLFS/svn/c/ConsoleKit-0.4.6.tar.xz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}                \
            --sysconfdir=%{_sysconfdir}       \
            --localstatedir=%{_localstatedir} \
            --enable-udev-acl    \
            --with-systemdsystemunitdir=no
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_lib}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_sbindir}/*
%{_datadir}/* 

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version