Summary:	The Totem PL Parser package contains a simple GObject-based library used to parse a host of playlist formats
Name:		totem-pl-parser
Version:	3.10.4
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/totem-pl-parser/3.10/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}    \
            --disable-quvi         \
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
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
