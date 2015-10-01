Summary:	The Zip package contains Zip utilities
Name:		zip
Version:	30
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/infozip
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}%{version}.tar.gz
%description

%prep
%setup -q -n zip30

%build
make -f unix/Makefile generic_gcc
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} prefix=%{buildroot}/usr -f unix/Makefile install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
/usr/man/man1/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
