Summary:	A network utility to retrieve files from the Web
Name:		wget
Version:	1.16.1
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/wget/wget.html
Group:		BLFS/NetworkingPrograms
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
%description
The Wget package contains a utility useful for non-interactive 
downloading of files from the Web.
%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--disable-silent-rules \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--sysconfdir=/etc \
	--with-ssl=openssl
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/etc
cat >> %{buildroot}/etc/wgetrc <<-EOF
#	default root certs location
	ca_certificate=/etc/ssl/certs/ca-bundle.crt
EOF
rm -rf %{buildroot}/%{_infodir}
%find_lang %{name}
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}/*
%files -f %{name}.lang
%defattr(-,root,root)
%config(noreplace) /etc/wgetrc
%{_bindir}/*
%{_mandir}/man1/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 1.16.1-1
*	Sun Sep 01 2013 nielsterp <nielsterp@comhem.se> 1.14-1
-	Added patch
*	Fri May 31 2013 baho-utot <baho-utot@columbus.rr.com> 1.14-1
-	Initial build.	First version