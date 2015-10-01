Summary:	The LVM2 package is a package that manages logical partitions.
Name:		LVM2
Version:	2.02.116
Release:	1
License:	GPL
URL:		ftp://sources.redhat.com/pub/lvm2/LVM2.2.02.116.tgz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}.%{version}.tgz

%description

%prep
%setup -q -n LVM2.2.02.116

%build
./configure --prefix=%{_prefix}           \
            --exec-prefix=                \
            --with-confdir=%{_sysconfdir} \
            --enable-applib               \
            --enable-cmdlib               \
            --enable-pkgconfig            \
            --enable-udev_sync  
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
/lib/*
/sbin/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
