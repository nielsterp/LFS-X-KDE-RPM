Summary:	Library for rendering TrueType fonts.
Name:		freetype
Version:	2.5.5
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description
The libpng package contains libraries used by other programs for reading
and writing PNG files. The PNG format was designed as a replacement for
GIF and, to a lesser extent, TIFF, with many improvements and extensions
and lack of patent problems.

%prep
%setup -q 
tar -xf /usr/src/Octothorpe/SOURCES/freetype-doc-2.5.5.tar.bz2 --strip-components=2 -C docs

%build
sed -i  -e "/AUX.*.gxvalid/s@^# @@" \
        -e "/AUX.*.otvalid/s@^# @@" \
        modules.cfg                   

sed -ri -e 's:.*(#.*SUBPIXEL.*) .*:\1:' \
        include/config/ftoption.h    
        
./configure \
	--prefix=%{_prefix} \
	--disable-static
make 

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*
install -v -m755 -d %{buildroot}/usr/share/doc/freetype-2.5.0.1
cp -v -R docs/*     %{buildroot}/usr/share/doc/freetype-2.5.0.1

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
