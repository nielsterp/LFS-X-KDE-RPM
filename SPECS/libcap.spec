Summary:	POSIX 1003.1e capabilities
Name:		libcap
Version:	2.24
Release:	1
License:	GPLv2
URL:		http://sites.google.com/site/fullycapable/
Group:		BLFS/Security
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.de.debian.org/debian/pool/main/libc/libcap2/%{name}-%{version}.tar.xz
Provides:	libcap.so.2 = 2.24
%description
The libcap2 package implements the user-space interfaces to the 
POSIX 1003.1e capabilities available in Linux kernels. 
These capabilities are a partitioning of the all powerful root 
privilege into a set of distinct privileges.
%prep
%setup -q -n libcap-%{version}
sed -i "/SBINDIR/s#sbin#bin#" Make.Rules
%build
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make prefix=/usr lib=/lib DESTDIR=%{buildroot} RAISE_SETFCAP=no install
find %{buildroot}/%{_libdir} -name '*.a'  -delete
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so*
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man8/*
   /usr/lib/pkgconfig/libcap.pc

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 2.24-1
*	Thu May 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.22-1
-	Initial build.	First version