Summary:	x264 package provides a library for encoding video streams into the H.264/MPEG-4 AVC format.
Name:		x264-snapshot
Version:	20141208
Release:	1
License:	GPL
URL:		http://download.videolan.org/pub/videolan/x264/snapshots/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}-2245-stable.tar.bz2
%description

%prep
%setup -q	-n %{name}-%{version}-2245-stable

%build
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
	--enable-shared        \
	--disable-cli
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%check

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
   
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
