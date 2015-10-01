Summary:	Contains a C++ class library for normalising the numerous telephony protocols into a single integrated call model.
Name:		opal
Version:	3.10.10
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/opal/3.10/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/opal-3.10.10-ffmpeg2-1.patch
./configure --prefix=%{_prefix}
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
chmod -v 644 %{buildroot}/usr/lib/libopal_s.a

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
