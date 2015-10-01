Summary:	Polkit-Qt provides an API to polkit in the Qt environment.
Name:		polkit-qt
Version:	0.112.0
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/apps/KDE4.x/admin/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-1-%{version}.tar.bz2

%description

%prep
%setup -q -n polkit-qt-1-0.112.0

%build
mkdir build &&
cd    build &&

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX \
      -DCMAKE_BUILD_TYPE=Release       \
      -DCMAKE_INSTALL_LIBDIR=lib       \
      -DUSE_QT4=TRUE                   \
      -Wno-dev .. &&
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
