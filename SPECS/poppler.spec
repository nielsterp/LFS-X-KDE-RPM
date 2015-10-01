Summary:	The Poppler package contains a PDF rendering library.
Name:		poppler
Version:	0.31.0
Release:	1
License:	GPL
URL:		http://poppler.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}         \
            --sysconfdir=%{_sysconfdir} \
            --disable-static      \
            --enable-xpdf-headers 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install
tar -xf ../../SOURCES/poppler-data-0.4.7.tar.gz
cd poppler-data-0.4.7
make prefix=/usr DESTDIR=%{buildroot} install

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
