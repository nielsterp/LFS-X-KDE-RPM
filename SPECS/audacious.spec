Summary:	Audacious is a GTK+ based audio player.
Name:		audacious
Version:	3.5.2
Release:	1
License:	GPL
URL:		http://distfiles.audacious-media-player.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
TPUT=/bin/true ./configure --prefix=%{_prefix} \
                           --with-buildstamp="BLFS" 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post
gtk-update-icon-cache 
update-desktop-database

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