Summary:	The D-Bus GLib package contains GLib interfaces to the D-Bus API
Name:		dbus-glib
Version:	0.104
Release:	1
License:	GPL
URL:		http://dbus.freedesktop.org/releases/dbus-glib
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"           \
	CXXFLAGS="%{optflags}"         \
	--prefix=%{_prefix}              \
	--sysconfdir=%{_sysconfdir}      \
	--libexecdir=%{_libdir}/dbus-1.0 \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%post
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas >/dev/null 2>&1

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
