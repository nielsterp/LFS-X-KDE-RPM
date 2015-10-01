Summary:	Gtk 2 GUI for other command line tools that can create, reorganise or delete disk partitions.
Name:		gparted
Version:	0.21.0
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/gparted/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q 

%build
./configure --prefix=%{_prefix} \
            --disable-doc       \
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
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
