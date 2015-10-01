Summary:	Phonon is the multimedia API for KDE4. 
Name:		phonon
Version:	4.8.3
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/phonon/4.8.3/src/
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

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX                         \
      -DCMAKE_BUILD_TYPE=Release                                 \
      -DCMAKE_INSTALL_LIBDIR=lib                                 \
      -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=FALSE        \
      -DDBUS_INTERFACES_INSTALL_DIR=/usr/share/dbus-1/interfaces \
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
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
