Summary:	Package contains a class library that has its genesis many years ago as PWLib
Name:		ptlib
Version:	2.10.10
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/ptlib/2.10/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/ptlib-2.10.10-bison_fixes-1.patch
./configure --prefix=%{_prefix}
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
chmod -v 755 %{buildroot}/usr/lib/libpt.so.2.10.10

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
