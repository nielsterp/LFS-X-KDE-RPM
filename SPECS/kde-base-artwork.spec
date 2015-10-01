Summary:	This package provides the default splash screen for KDE.
Name:		kde-base-artwork
Version:	14.12.2
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/applications/14.12.2/src/kde-base-artwork-14.12.2.tar.xz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
mkdir build &&
cd    build &&

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX -Wno-dev ..
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
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
