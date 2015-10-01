Summary:	Grantlee is a set of free software libraries written using the Qt framework.
Name:		grantlee
Version:	0.5.1
Release:	1
License:	GPL
URL:		http://downloads.grantlee.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
mkdir build 
cd    build 

cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=Release        \
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
