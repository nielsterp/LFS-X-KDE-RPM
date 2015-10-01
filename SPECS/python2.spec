Summary:	A high-level scripting language
Name:		python2
Version:	2.7.9
Release:	1
License:	PSF
URL:		http://www.python.org/
Group:		BLFS/Programming
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.python.org/ftp/python/2.7.9/Python-%{version}.tar.xz
Requires:	expat >= 2.1.0
Requires:	libffi >= 3.0.13
Requires:	pkg-config >= 0.28
Requires:	python2 >= 2.7.8
Provides:	python >= 2.7.8
%description
The Python 2 package contains the Python development environment. It 
is useful for object-oriented programming, writing scripts, 
prototyping large programs or developing entire applications. This 
version is for backward compatibility with other dependent packages.
%prep
%setup -q -n Python-%{version}
%build
export OPT="${CFLAGS}"
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--enable-shared \
	--with-system-expat \
	--with-system-ffi \
	--enable-unicode=ucs4 \
	--with-dbmliborder=gdbm:ndbm
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
chmod -v 755 %{buildroot}%{_libdir}/libpython2.7.so.1.0
install -D -m644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
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
%{_libdir}/pkgconfig/*
%{_libdir}/python2.7*
%{_includedir}/*
%{_datarootdir}/licenses/*
%{_mandir}/man1/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 2.7.9-1
*	Wed May 29 2013 baho-utot <baho-utot@columbus.rr.com> 2.7.5-1
-	Initial build.	First version
