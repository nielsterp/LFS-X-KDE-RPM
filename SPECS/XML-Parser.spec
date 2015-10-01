Summary:	Perl interface to Expat
Name:		XML-Parser
Version:	2.44
Release:	1
License:	GPLv3
URL:		https://github.com/chorny/XML-Parser
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		XML-Parser-2.44.tar.gz

%description
The XML::Parser module is a Perl interface to James Clark's XML parser, Expat. 

%prep
%setup -q
perl Makefile.PL

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post	-p /sbin/ldconfig

%postun	-p /sbin/ldconfig

%files 
%{_libdir}/*
%{_mandir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
