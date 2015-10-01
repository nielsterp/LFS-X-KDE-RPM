Summary:	The Net-tools package is a collection of programs for controlling the network subsystem
Name:		net-tools
Version:	20101030
Release:	1
License:	GPL
URL:		http://anduin.linuxfromscratch.org/sources/BLFS/svn/n
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-CVS_%{version}.tar.gz
%description

%prep
%setup -q -n net-tools-CVS_20101030

%build
sed -i -e '/Token/s/y$/n/'        config.in &&
sed -i -e '/HAVE_HWSTRIP/s/y$/n/' config.in &&
yes "" | make config                 &&
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} update
rm -rf %{buildroot}/bin/hostname
rm -rf %{buildroot}/usr/share/man/man1/dnsdomainname.1.gz
rm -rf %{buildroot}/usr/share/man/man1/hostname.1.gz
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)

/sbin/*
/bin/*
%{_mandir}

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version

