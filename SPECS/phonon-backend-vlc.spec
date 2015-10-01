Summary:	This package provides a Phonon backend which utilizes the VLC media framework.
Name:		phonon-backend-vlc
Version:	0.8.2
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/phonon/phonon-backend-vlc/0.8.2/src/
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

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX \
      -DCMAKE_INSTALL_LIBDIR=lib         \
      -DCMAKE_BUILD_TYPE=Release         \
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
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version