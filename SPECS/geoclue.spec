Summary:	GeoClue is a modular geoinformation service built on top of the D-Bus messaging system.
Name:		geoclue
Version:	0.12.0
Release:	1
License:	GPL
URL:		https://launchpad.net/geoclue/trunk/0.12/+download/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
Patch0:		geoclue-0.12.0-gpsd_fix-1.patch
%description

%prep
%setup -q
%patch0 -p1

%build
sed -i "s@ -Werror@@" configure
sed -i "s@libnm_glib@libnm-glib@g" configure

sed -i "s@geoclue/libgeoclue.la@& -lgthread-2.0@g" \
       providers/skyhook/Makefile.in

./configure --prefix=%{_prefix}
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
%{_libexecdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version