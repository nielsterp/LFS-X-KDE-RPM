Summary:	FAAD2 is a decoder for a lossy sound compression scheme specified in MPEG-2 Part 7 and MPEG-4 Part 3
Name:		faad2
Version:	2.7
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/faac/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
Source1:	faad2-2.7-mp4ff-1.patch
%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/faad2-2.7-mp4ff-1.patch 
sed -i "s:AM_CONFIG_HEADER:AC_CONFIG_HEADERS:g" configure.in 
sed -i "s:man_MANS:man1_MANS:g" frontend/Makefile.am 
autoreconf -fi 
./configure --prefix=%{_prefix} \
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
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
