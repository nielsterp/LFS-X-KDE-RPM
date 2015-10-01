Summary:	Shared libraries, portable interface
Name:		libtool
Version:	2.4.6
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/libtool
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.xz
%description
It wraps the complexity of using shared libraries in a 
consistent, portable interface.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--disable-silent-rules
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -delete
rm -rf %{buildroot}%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datarootdir}/aclocal/*
%{_datarootdir}/%{name}/*
%{_mandir}/*/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 2.4.6-1
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.4.2-1
-	Initial build.	First version	
