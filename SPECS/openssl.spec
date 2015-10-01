Summary:	Management tools and libraries relating to cryptography
Name:		openssl
Version:	1.0.2
Release:	1
License:	BSD
URL:		http://www.openssl.org
Group:		BLFS/Security
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.openssl.org/source/%{name}-%{version}.tar.gz
Patch0:		openssl-1.0.2-fix_parallel_build-1.patch
%description
The OpenSSL package contains management tools and libraries relating
to cryptography. These are useful for providing cryptography 
functions to other packages, such as OpenSSH, email applications and
web browsers (for accessing HTTPS sites).
%prep
%setup -q
%patch0 -p1
%build
export CFLAGS="%{optflags}"
./config \
	--prefix=%{_prefix} \
	--libdir=lib \
	--openssldir=/etc/ssl \
	shared \
	zlib-dynamic \
	-Wa,--noexecstack "${CFLAGS}" "${LDFLAGS}"
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make INSTALL_PREFIX=%{buildroot} MANDIR=/usr/share/man MANSUFFIX=ssl install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
/etc/ssl/*
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*
/usr/share/man/man3/.3ssl.gz
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 1.0.2-1
*	Wed May 22 2013 baho-utot <baho-utot@columbus.rr.com> 1.0.1e-1
-	Initial build.	First version
