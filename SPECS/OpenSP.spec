Summary:	The OpenSP package contains a C++ library for using SGML/XML files
Name:		OpenSP
Version:	1.5.2
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/openjade
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
sed -i 's/32,/253,/' lib/Syntax.cxx
sed -i 's/LITLEN          240 /LITLEN          8092/' unicode/{gensyntax.pl,unicode.syn}
./configure --prefix=%{_prefix}                        \
	    --disable-static                           \
            --disable-doc-build                        \
            --enable-default-catalog=/etc/sgml/catalog \
            --enable-http                              \
            --enable-default-search-path=/usr/share/sgml
make pkgdatadir=/usr/share/sgml/OpenSP-1.5.2 

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} pkgdatadir=/usr/share/sgml/OpenSP-1.5.2 install
%{_fixperms} %{buildroot}/*

%post
ln -v -sf onsgmls /usr/bin/nsgmls &&
ln -v -sf osgmlnorm /usr/bin/sgmlnorm &&
ln -v -sf ospam /usr/bin/spam &&
ln -v -sf ospcat /usr/bin/spcat &&
ln -v -sf ospent /usr/bin/spent &&
ln -v -sf osx /usr/bin/sx &&
ln -v -sf osx /usr/bin/sgml2xml &&
ln -v -sf libosp.so /usr/lib/libsp.so

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
