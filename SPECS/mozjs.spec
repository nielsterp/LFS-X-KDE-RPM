Summary:	JS is Mozilla's JavaScript engine written in C/C++
Name:		mozjs
Version:	17.0.0
Release:	1
License:	GPL
URL:		http://ftp.mozilla.org/pub/mozilla.org/js
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}%{version}.tar.gz
%description

%prep
%setup -q -n mozjs17.0.0

%build
cd js/src
./configure \
	--prefix=%{_prefix} \
        --enable-readline   \
        --enable-threadsafe \
        --with-system-ffi   \
        --with-system-nspr

make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd js/src
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%post
find /usr/include/js-17.0/            \
     /usr/lib/libmozjs-17.0.a         \
     /usr/lib/pkgconfig/mozjs-17.0.pc \
     -type f -exec chmod -v 644 {} \;


%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
