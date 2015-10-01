Summary:	Facilities to integrate Clutter into GTK+ applications
Name:		clutter-gtk
Version:	1.6.0
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/clutter-gtk/1.4
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}" \
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