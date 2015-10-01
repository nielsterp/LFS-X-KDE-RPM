Summary:	The giflib package contains libraries for reading and writing GIFs 
Name:		giflib
Version:	5.1.1
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/giflib
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --disable-static 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install

find doc \( -name Makefile\* -o -name \*.1 \
         -o -name \*.xml \) -exec rm -v {} \; &&

install -v -dm755 %{buildroot}/usr/share/doc/giflib-5.1.1 &&
cp -v -R doc/* %{buildroot}/usr/share/doc/giflib-5.1.1

%{_fixperms} %{buildroot}/*

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
