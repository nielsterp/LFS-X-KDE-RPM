Summary:	QJson is a Qt-based library that maps JSON data to QVariant objects and vice versa.
Name:		qjson
Version:	0.8.1
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/qjson/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
mkdir build 
cd    build 

cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=Release  \
      .. 
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
