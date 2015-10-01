Summary:	Akonadi is an extensible cross-desktop storage service for PIM data 
Name:		akonadi
Version:	1.13.0
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/akonadi/src/
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

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX  \
      -DCMAKE_BUILD_TYPE=Release          \
      -DINSTALL_QSQLITE_IN_QT_PREFIX=TRUE \
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
%{_oldincludedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version