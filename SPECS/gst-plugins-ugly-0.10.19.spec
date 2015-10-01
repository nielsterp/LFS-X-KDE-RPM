Summary:	GStreamer Ugly Plug-ins is a set of plug-ins considered by the GStreamer 
#		developers to have good quality and correct functionality, 
#		but distributing them might pose problems.
Name:		gst-plugins-ugly
Version:	0.10.19
Release:	1
License:	GPL
URL:		http://gstreamer.freedesktop.org/src/gst-plugins-ugly/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q
patch -Np1 -i ../../SOURCES/gst-plugins-ugly-0.10.19-libcdio_fixes-1.patch
%build
./configure --prefix=%{_prefix}	\
	    --enable-gtk-doc
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
