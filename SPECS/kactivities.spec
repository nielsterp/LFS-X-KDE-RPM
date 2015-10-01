Summary:	This package provides the activitymanager for KDE.
Name:		kactivities
Version:	4.13.3
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/4.13.3/src/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
mkdir build 
cd    build 

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX \
      -DCMAKE_BUILD_TYPE=Release         \
      -Wno-dev ..
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
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
