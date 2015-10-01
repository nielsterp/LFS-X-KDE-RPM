Summary:	Programs and libraries that are central to development and execution of KDE programs.
Name:		kdelibs
Version:	4.14.5
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/applications/14.12.2/src/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
sed -i "s@{SYSCONF_INSTALL_DIR}/xdg/menus@& RENAME kde-applications.menu@" \
        kded/CMakeLists.txt 

sed -i "s@applications.menu@kde-&@" \
        kded/kbuildsycoca.cpp

mkdir build 
cd    build 

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX \
      -DSYSCONF_INSTALL_DIR=/etc         \
      -DCMAKE_BUILD_TYPE=Release         \
      -DDOCBOOKXML_CURRENTDTD_DIR=/usr/share/xml/docbook/xml-dtd-4.5 \
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
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
