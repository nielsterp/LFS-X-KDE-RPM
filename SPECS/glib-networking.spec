Summary:	Contains Network related gio modules for GLib
Name:		glib-networking
Version:	2.42.1
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/glib-networking/2.36
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"                          \
	CXXFLAGS="%{optflags}"                        \
	--prefix=%{_prefix}                           \
        --libexecdir=%{_libdir}/glib-networking       \
        --with-ca-certificates=/etc/ssl/ca-bundle.crt \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
