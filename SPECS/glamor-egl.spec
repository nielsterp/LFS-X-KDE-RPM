Summary:	GL-based rendering acceleration library for X server.
Name:		glamor-egl
Version:	0.5.0
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
Patch0:		glamor-egl-0.5.0-fixes-1.patch

%description

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
./configure \
	CFLAGS="%{optflags}"               \
	CXXFLAGS="%{optflags}"             \
	--prefix=%{_prefix}                \
	--sysconfdir=%{_sysconfigdir}      \
	--localstatedir=%{_localstatedir} \
	--disable-static                   \
        --enable-glx-tls
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
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
