Summary:	A simple library designed for accessing DVDs as a block device
Name:		libdvdcss
Version:	1.3.0
Release:	1
License:	GPL
URL:		http://download.videolan.org/libdvdcss/1.3.0/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}  \
            --disable-static     \
            --docdir=/usr/share/doc/libdvdcss-1.3.0 
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
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
