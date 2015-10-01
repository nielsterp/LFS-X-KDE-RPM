Summary:	A portable, high level programming interface to various calling conventions
Name:		libffi
Version:	3.2.1
Release:	1
License:	MIT
URL:		http://sourceware.org/libffi/
Group:		BLFS/GeneralLibraries
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	ftp://sourceware.org/pub/libffi/%{name}-%{version}.tar.gz
%description
The libffi library provides a portable, high level programming interface
to various calling conventions. This allows a programmer to call any 
function specified by a call interface description at run time.
%prep
%setup -q
sed -e '/^includesdir/ s:$(libdir)/@PACKAGE_NAME@-@PACKAGE_VERSION@/include:$(includedir):' \
    -i include/Makefile.in &&
sed -e '/^includedir/ s:${libdir}/@PACKAGE_NAME@-@PACKAGE_VERSION@/include:@includedir@:' \
    -e 's/^Cflags: -I${includedir}/Cflags:/' \
    -i libffi.pc.in
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--disable-static
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -D -m644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
find %{buildroot}/%{_libdir} -name '*.la' -delete
rm -rf %{buildroot}/%{_infodir}
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
%ifarch x86_64
/usr/lib64/*
%else
/usr/lib/*
%endif
/usr/lib/pkgconfig/*
%{_includedir}/*
%{_datarootdir}/licenses/libffi/LICENSE
%{_mandir}/man3/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 3.2.1-1
*	Wed May 29 2013 baho-utot <baho-utot@columbus.rr.com> 3.0.13-1
-	Initial build.	First version