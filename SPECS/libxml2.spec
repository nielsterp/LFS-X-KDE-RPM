Summary:	Contains libraries and utilities for parsing XML files.
Name:		libxml2
Version:	2.9.2
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q
tar xf ../../SOURCES/xmlts20130923.tar.gz
%build
sed \
  -e /xmlInitializeCatalog/d \
  -e 's/((ent->checked =.*&&/(((ent->checked == 0) ||\
          ((ent->children == NULL) \&\& (ctxt->options \& XML_PARSE_NOENT))) \&\&/' \
  -i parser.c
./configure \
	--prefix=%{_prefix} \
	--disable-static    \
        --with-history
make	

make check > ../../LOGS/libxml2_check.log
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install

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
