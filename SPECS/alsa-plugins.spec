Summary:	The ALSA Plugins package contains plugins for various audio libraries and sound servers
Name:		alsa-plugins
Version:	1.0.28
Release:	1
License:	GPL
URL:		http://alsa.cybermirror.org/plugins
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
sed -i "/speex_preprocess/i#include <stdint.h>" speex/pcm_speex.c 
./configure 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_prefix}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
