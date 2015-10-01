Summary:	The GTK-Doc package contains a code documenter.
Name:		gtk-doc
Version:	1.21
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/gtk-doc/1.19
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description
The GTK-Doc package contains a code documenter. This is useful for
extracting specially formatted comments from the code to create API
documentation. This package is optional; if it is not installed,
packages will not build the documentation. This does not mean that you
will not have any documentation. If GTK-Doc is not available, the
install process will copy any pre-built documentation to your system.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
