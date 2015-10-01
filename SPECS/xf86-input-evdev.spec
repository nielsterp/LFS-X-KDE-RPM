Summary:	Generic Linux input driver for the Xorg X server.
Name:		xf86-input-evdev
Version:	2.9.1
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"              \
	CXXFLAGS="%{optflags}"            \
	--prefix=%{_prefix}               \
	--sysconfdir=%{_sysconfdir}       \
	--localstatedir=%{_localstatedir} \
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
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
