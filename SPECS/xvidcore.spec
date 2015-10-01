Summary:	XviD is an MPEG-4 compliant video CODEC
Name:		xvidcore
Version:	1.3.3
Release:	1
License:	GPL
URL:		http://downloads.xvid.org/downloads
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q -n xvidcore

%build
cd build/generic 
sed -i 's/^LN_S=@LN_S@/& -f -v/' platform.inc.in 
./configure --prefix=%{_prefix}
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd build/generic
sed -i '/libdir.*STATIC_LIB/ s/^/#/' Makefile
make DESTDIR=%{buildroot} install
chmod -v 755 %{buildroot}/usr/lib/libxvidcore.so.4.3 
install -v -m755 -d %{buildroot}/usr/share/doc/xvidcore-1.3.2/examples &&
install -v -m644 ../../doc/* %{buildroot}/usr/share/doc/xvidcore-1.3.2 &&
install -v -m644 ../../examples/* \%{buildroot}/usr/share/doc/xvidcore-1.3.2/examples

%{_fixperms} %{buildroot}/*

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
