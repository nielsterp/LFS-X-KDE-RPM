Summary:	The Gcr package contains libraries used for displaying certificates and accessing key stores. 
Name:		gcr
Version:	3.14.0
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/gcr/3.14/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}         \
            --sysconfdir=%{_sysconfdir}
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
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_datadir}/* 

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version