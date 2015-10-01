Summary:	A set a set of plug-ins that aren't up to par
Name:		gst-plugins-bad
Version:	1.4.5
Release:	1
License:	GPL
URL:		http://gstreamer.freedesktop.org/src/gst-plugins-bad
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/gst-plugins-bad-1.4.5-openjpeg21-1.patch
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
        --with-package-name="GStreamer Bad Plugins 1.4.5 BLFS" \
        --with-package-origin="http://www.linuxfromscratch.org/blfs/view/svn/"
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
