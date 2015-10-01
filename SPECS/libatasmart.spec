Summary:	The libatasmart package is a disk reporting library.
Name:		libatasmart
Version:	0.19
Release:	1
License:	GPL
URL:		http://0pointer.de/public/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --disable-static 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make docdir=/usr/share/doc/libatasmart-0.19 DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
