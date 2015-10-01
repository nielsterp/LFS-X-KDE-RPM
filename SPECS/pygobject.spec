Summary:	PyGObject-2.28.6 provides Python 2 bindings to the GObject class from GLib.
Name:		pygobject
Version:	2.28.6
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/pygobject/2.28/pygobject-2.28.6.tar.xz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
Patch0:		pygobject-2.28.6-fixes-1.patch
%description

%prep
%setup -q
patch -Np1 -i ../../SOURCES/pygobject-2.28.6-fixes-1.patch
%build
./configure --prefix=%{_prefix}
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%check

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
