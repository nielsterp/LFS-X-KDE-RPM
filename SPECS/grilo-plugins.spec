Summary:	Grilo-Plugins is a collection of plugins for media discovery 
Name:		grilo-plugins
Version:	0.2.14
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/grilo-plugins/0.2/grilo-plugins-0.2.14.tar.xz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
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
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
