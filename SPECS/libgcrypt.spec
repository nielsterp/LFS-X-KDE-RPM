Summary:	General purpose crypto library.
Name:		libgcrypt
Version:	1.6.2
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description
The libgcrypt package contains a general purpose crypto library based on
the code used in GnuPG. The library provides a high level interface to
cryptographic building blocks using an extendable and flexible API.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--disable-static 
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
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
