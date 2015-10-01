Summary:	GStreamer Bad Plug-ins package contains a set a set of plug-ins that aren't up to par
Name:		gst-plugins-bad
Version:	0.10.23
Release:	1
License:	GPL
URL:		http://gstreamer.freedesktop.org/src/gst-plugins-bad/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --with-gtk=3.0      \
	    --disable-examples 
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
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
