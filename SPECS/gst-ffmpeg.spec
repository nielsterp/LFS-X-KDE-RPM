Summary:	The Gst FFMpeg contains GStreamer plugins for FFMpeg.
Name:		gst-ffmpeg
Version:	0.10.13
Release:	1
License:	GPL
URL:		http://gstreamer.freedesktop.org/src/gst-ffmpeg/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
patch -p1 < ../../SOURCES/gst-ffmpeg-0.10.13-gcc-4.7-1.patch &&
./configure --prefix=%{_prefix}
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

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
