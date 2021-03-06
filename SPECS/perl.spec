Summary:	Practical Extraction and Report Language
Name:		perl
Version:	5.20.2
Release:	1
License:	GPLv1
URL:		http://www.perl.org/
Group:		Development/Languages
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.cpan.org/src/5.0/%{name}-%{version}.tar.bz2
Provides:	perl >= 0:5.003000
%description
The Perl package contains the Practical Extraction and
Report Language.
%prep
%setup -q
echo "127.0.0.1 localhost $(hostname)" > /etc/hosts
export BUILD_ZLIB=False
export BUILD_BZIP2=0

%build
CFLAGS="%{_optflags}"
sh Configure -des \
	-Dprefix=%{_prefix} \
	-Dvendorprefix=%{_prefix} \
	-Dman1dir=%{_mandir}/man1 \
	-Dman3dir=%{_mandir}/man3 \
	-Dpager=%{_bindir}"/less -isR" \
	-Duseshrplib
make VERBOSE=1 %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_bindir}/*
%dir %{_libdir}/perl5
%dir %{_libdir}/perl5/%{version}
%{_libdir}/perl5/%{version}/*
%{_mandir}/*/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 5.20.2-1
*	Sun Apr 06 2014 baho-utot <baho-utot@columbus.rr.com> 5.18.2-1
*	Sat Aug 24 2013 baho-utot <baho-utot@columbus.rr.com> 5.18.1-1
*	Fri Jun 28 2013 baho-utot <baho-utot@columbus.rr.com> 5.18.0-1
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 5.16.3-1
-	Upgrade version