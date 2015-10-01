Summary:	QImageblitz is a graphical effect and filter library for KDE.
Name:		qimageblitz
Version:	0.0.6
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/qimageblitz/
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

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX -Wno-dev .. &&
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

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
