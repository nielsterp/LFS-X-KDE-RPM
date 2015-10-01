Summary:	Tool and a panel applet used to configure wired and wireless network connections through GUI.
Name:		network-manager-applet
Version:	1.0.0
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/network-manager-applet/1.0/network-manager-applet-1.0.0.tar.xz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q 

%build
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
            --disable-migration \
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
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
