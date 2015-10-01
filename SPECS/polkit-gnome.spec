Summary:	Provides an Authentication Agent for Polkit that integrates well with the GNOME Desktop environment.
Name:		polkit-gnome
Version:	0.105
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/polkit-gnome/0.105/
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
%{_libexecdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
