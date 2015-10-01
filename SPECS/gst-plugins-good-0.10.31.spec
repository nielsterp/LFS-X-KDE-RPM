Summary:	GStreamer Good Plug-ins is a set of plug-ins considered by the GStreamer developers to have good quality code
Name:		gst-plugins-good
Version:	0.10.31
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/gst-plugins-good/0.10/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
sed -i -e "/input:/d" sys/v4l2/gstv4l2bufferpool.c 
sed -i -e "/case V4L2_CID_HCENTER/d" -e "/case V4L2_CID_VCENTER/d" sys/v4l2/v4l2_calls.c 
./configure --prefix=%{_prefix}         \
            --sysconfdir=%{_sysconfdir} \
            --with-gtk=3.0 
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
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
