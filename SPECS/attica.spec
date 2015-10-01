Summary:	Attica is a library to access "Open Collaboration Service" providers.
Name:		attica
Version:	0.4.2
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/attica/
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

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX \
      -DCMAKE_BUILD_TYPE=Release         \
      -DQT4_BUILD=ON                     \
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