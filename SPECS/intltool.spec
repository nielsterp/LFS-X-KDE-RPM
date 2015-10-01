Summary:	Internationalization tool 
Name:		intltool
Version:	0.50.2
Release:	1
License:	GPLv3
URL:		http://freedesktop.org/wiki/Software/intltool
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://launchpad.net/intltool/trunk/0.50.2/+download/%{name}-%{version}.tar.gz

%description
The Intltool is an internationalization tool used for extracting translatable strings from source files.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --docdir=%{_docdir}/gperf-3.0.4
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post	-p /sbin/ldconfig

%postun	-p /sbin/ldconfig

%files
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version