Summary:	Reference implementation of the vp8 Codec
Name:		libvpx
Version:	1.3.0
Release:	1
License:	GPL
URL:		http://webm.googlecode.com/files
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-v%{version}.tar.xz
%description

%prep
%setup -q -n libvpx-v1.3.0

%build
sed -i 's/cp -p/cp/' build/make/Makefile
chmod -v 644 vpx/*.h
mkdir ../libvpx-build 
cd ../libvpx-build 
../libvpx-v1.3.0/configure --prefix=%{_prefix} \
                           --enable-shared \
                           --disable-static 
make
cd ..

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd ../libvpx-build
make DESTDIR=%{buildroot} install
cd ..
%{_fixperms} %{buildroot}/*

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
