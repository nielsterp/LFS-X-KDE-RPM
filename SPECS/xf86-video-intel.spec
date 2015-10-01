Summary:	Xorg Intel Driver package.
Name:		xf86-video-intel
Version:	2.99.917
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
	--prefix=%{_prefix}              \
	--sysconfdir=%{_sysconfdir}      \
	--localstatedir=%{_localstatedir} \
	--disable-static                 \
        --enable-kms-only                \
        --with-default-accel=sna
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_libdir}/*
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/*


%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
