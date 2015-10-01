Summary:	Contains a set of programs for listing PCI devices, inspecting their status and setting their configuration registers
Name:		pciutils
Version:	3.3.0
Release:	1
License:	GPL
URL:		http://ftp.kernel.org/pub/software/utils/pciutils
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
	make PREFIX=%{_prefix}    \
     	SHAREDIR=%{_datadir}/misc \
     	MANDIR=%{_mandir}         \
     	SHARED=yes                \
     	ZLIB=no                   \
     	all
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} PREFIX=/usr              \
     SHAREDIR=/usr/share/misc \
     MANDIR=/usr/share/man    \
     SHARED=yes               \
     ZLIB=no                  \
     install install-lib
%{_fixperms} %{buildroot}/*

%post
chmod -v 755 /usr/lib/libpci.so.3.3.0

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
