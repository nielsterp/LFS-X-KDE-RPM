Summary:	GStreamer is a streaming media framework
Name:		gstreamer
Version:	1.4.5
Release:	1
License:	GPL
URL:		http://gstreamer.freedesktop.org/src/gstreamer
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"    \
	CXXFLAGS="%{optflags}"  \
	    --prefix=%{_prefix} \
            --with-package-name="GStreamer 1.4.5 BLFS" \
            --with-package-origin="http://www.linuxfromscratch.org/blfs/view/svn/" &&
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
%{_libexecdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
