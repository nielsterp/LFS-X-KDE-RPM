Summary:	Script to give lsb data
Name:		lsb-release
Version:	1.4
Release:	1
License:	GPLv3
URL:		http://sourceforge.net/projects/lsb/files/lsb_release/1.4
Group:		BLFS/System-Utilities
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://sourceforge.net/projects/lsb/files/lsb_release/1.4/lsb-release-1.4.tar.gz
%description
The lsb_release script gives information about the Linux Standards Base (LSB) status of the distribution.
%prep
%setup -q
%build
./help2man -N --include ./lsb_release.examples \
              --alt_version_key=program_version ./lsb_release > lsb_release.1
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

install -vdm 755 %{buildroot}/usr/share/man/man1
install -vdm 755 %{buildroot}/usr/bin

install -v -m 644 lsb_release.1 %{buildroot}/usr/share/man/man1/lsb_release.1 &&
install -v -m 755 lsb_release %{buildroot}/usr/bin/lsb_release
%check

%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%changelog
*	Sun May 19 2013 baho-utot <baho-utot@columbus.rr.com> 2.20-1
-	Initial build.	First version
