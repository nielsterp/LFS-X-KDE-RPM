Summary:	Exiv2 is a C++ library and a command line utility for managing image metadata.
Name:		exiv2
Version:	0.24
Release:	1
License:	GPL
URL:		http://www.exiv2.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

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
chmod -v 755 %{buildroot}/usr/lib/libexiv2.so

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