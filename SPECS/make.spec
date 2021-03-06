Summary:	Program for compiling packages
Name:		make
Version:	4.1
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/make
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/make/%{name}-%{version}.tar.bz2
%description
The Make package contains a program for compiling packages.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix} \
	--disable-silent-rules
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/gnumake.h
%{_mandir}/*/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 4.1-1
*	Sun Apr 06 2014 baho-utot <baho-utot@columbus.rr.com> 4.0-1
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 3.82-1
-	Initial build.	First version
