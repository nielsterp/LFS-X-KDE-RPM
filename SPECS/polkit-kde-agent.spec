Summary:	Polkit-kde-agent provides a graphical authentication prompt.
Name:		polkit-kde-agent
Version:	0.99.0
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/apps/KDE4.x/admin/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-1-%{version}.tar.bz2

%description

%prep
%setup -q -n polkit-kde-agent-1-0.99.0

%build
patch -Np1 -i ../../SOURCES/polkit-kde-agent-1-0.99.0-remember_password-1.patch 

mkdir build 
cd    build 

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX -Wno-dev .. 
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
