Summary:	v4l-utils provides a series of utilities for media devices
Name:		v4l-utils
Version:	1.6.2
Release:	1
License:	GPL
URL:		http://www.linuxtv.org/downloads/v4l-utils/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}         \
            --sysconfdir=%{_sysconfdir} \
            --disable-static
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_lib}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
%{_sbindir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
