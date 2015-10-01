Summary:	The GNOME Keyring package contains a daemon that keeps passwords and other secrets for users.
Name:		gnome-keyring
Version:	3.14.0
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/gnome-keyring/3.14/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}         \
            --sysconfdir=%{_sysconfdir} \
            --with-pam-dir=/lib/security 
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
%{_sysconfdir}/* 
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version