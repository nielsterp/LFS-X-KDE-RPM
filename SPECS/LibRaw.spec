Summary:	Libraw is a library for reading RAW files obtained from digital photo cameras
Name:		LibRaw
Version:	0.16.0
Release:	1
License:	GPL
URL:		http://www.libraw.org/data/LibRaw-0.16.0.tar.gz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
            --enable-jpeg       \
            --enable-jasper     \
            --enable-lcms       \
            --disable-static    \
            --docdir=%{_docdir}/libraw-0.16.0 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install

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
