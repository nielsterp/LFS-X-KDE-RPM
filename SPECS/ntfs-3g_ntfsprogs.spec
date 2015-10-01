Summary:	The Ntfs-3g package contains a stable, read-write open source driver for NTFS partitions.
Name:		ntfs-3g_ntfsprogs
Version:	2014.2.15
Release:	1
License:	GPL
URL:		http://tuxera.com/opensource/ntfs-3g_ntfsprogs-2014.2.15.tgz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tgz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
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
/bin/*
%{_lib}/*
/sbin/*
%{_bindir}/*
%{_includedir}/*
%{_sbindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
