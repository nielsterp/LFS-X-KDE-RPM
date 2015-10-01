Summary:	Libraries used for creating graphical user interfaces for applications
Name:		gtk+
Version:	3.14.8
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/gtk+/3.8
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q -n gtk+-3.14.8

%build
./configure \
	--prefix=%{_prefix}         \
	--sysconfdir=%{_sysconfdir} \
	--enable-broadway-backend   \
	--enable-x11-backend        \
	--disable-wayland-backend 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%post

glib-compile-schemas /usr/share/glib-2.0/schemas

gtk-query-immodules-3.0 --update-cache

%clean

rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
%{_bindir}/*
%{_sysconfdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
