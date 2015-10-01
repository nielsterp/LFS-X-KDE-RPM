Summary:	Libraries for writing PNG files.
Name:		libpng
Version:	1.6.16
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
Patch0:         http://downloads.sourceforge.net/libpng-apng/libpng-1.6.16-apng.patch.gz

%description
The libpng package contains libraries used by other programs for reading
and writing PNG files. The PNG format was designed as a replacement for
GIF and, to a lesser extent, TIFF, with many improvements and extensions
and lack of patent problems.

%prep
%setup -q
gzip -cd ../../SOURCES/libpng-1.6.16-apng.patch.gz | patch -p1

%build
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*
install -vdm 755 %{buildroot}/usr/share/doc/libpng-1.6.4
cp -v README libpng-manual.txt %{buildroot}/usr/share/doc/libpng-1.6.4

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
