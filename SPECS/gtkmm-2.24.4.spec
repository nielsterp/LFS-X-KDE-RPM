Summary:	Provides a C++ interface to GTK+ 2
Name:		gtkmm
Version:	2.24.4
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/gtkmm/2.24
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q -n gtkmm-2.24.4

%build
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} 
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
