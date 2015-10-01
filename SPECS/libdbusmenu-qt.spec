Summary:	This library provides a Qt implementation of the DBusMenu specs
Name:		libdbusmenu-qt
Version:	0.9.2
Release:	1
License:	GPL
URL:		http://launchpad.net/libdbusmenu-qt/trunk/0.9.2/+download/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
mkdir build &&
cd    build &&

cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=Release        \
      -DWITH_DOC=OFF .. 
make
cd ..

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd build
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

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
