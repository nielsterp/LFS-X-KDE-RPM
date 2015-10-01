Summary:	Low-level libraries
Name:		glib
Version:	2.42.1
Release:	1
License:	GPLv3
URL:		http://ftp.gnome.org/pub/gnome/sources/glib/2.42/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description
The GLib package contains a low-level libraries useful for providing data 
structure handling for C, portability wrappers and interfaces for such runtime 
functionality as an event loop, threads, dynamic loading and an object system.
%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--with-pcre=system
make %{?_smp_mflags}
%check

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*   
%{_libdir}/*
%{_datadir}/* 

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 2.42.1
*	Sat Mar 22 2014 baho-utot <baho-utot@columbus.rr.com> 2.19-1
*	Sun Sep 01 2013 baho-utot <baho-utot@columbus.rr.com> 2.18-2
*	Sat Aug 24 2013 baho-utot <baho-utot@columbus.rr.com> 2.18-1
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 2.17-1
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.16-1
-	Initial version