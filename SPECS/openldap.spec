Summary:	Open source implementation of the Lightweight Directory Access Protocol.
Name:		openldap
Version:	2.4.40
Release:	1
License:	GPL
URL:		ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tgz

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/openldap-2.4.40-blfs_paths-1.patch 
patch -Np1 -i ../../SOURCES/openldap-2.4.40-symbol_versions-1.patch 
autoconf 

sed -i '/6.0.20/ a\\t__db_version_compat' configure 

./configure --prefix=%{_prefix}         \
            --sysconfdir=%{_sysconfdir} \
            --disable-static            \
            --enable-dynamic            \
            --disable-debug             \
            --disable-slapd 
make depend 
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
