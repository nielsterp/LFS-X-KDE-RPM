Summary:	The GStreamer Libav package contains GStreamer plugins for Libav (a fork of FFmpeg).
Name:		gst-libav
Version:	1.4.5
Release:	1
License:	GPL
URL:		http://gstreamer.freedesktop.org/src/gst-libav/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}                                      \
            --with-package-name="GStreamer Libav Plugins 1.4.5 BLFS" \
            --with-package-origin="http://www.linuxfromscratch.org/blfs/view/svn/" 
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
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
