Summary:	The SGML Common package contains install-catalog
Name:		sgml-common
Version:	0.6.3
Release:	1
License:	GPL
URL:		ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tgz
Patch0:		sgml-common-0.6.3-manpage-1.patch
%description

%prep
%setup -q
patch -Np1 -i ../../SOURCES/sgml-common-0.6.3-manpage-1.patch
%build
autoreconf -f -i
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%post
install-catalog --add /etc/sgml/sgml-ent.cat \
    /usr/share/sgml/sgml-iso-entities-8879.1986/catalog
install-catalog --add /etc/sgml/sgml-docbook.cat \
    /etc/sgml/sgml-ent.cat

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
/usr/doc/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
