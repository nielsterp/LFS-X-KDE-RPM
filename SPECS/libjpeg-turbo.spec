Summary:	libjpeg-turbo is a fork of the original IJG libjpeg
Name:		libjpeg-turbo
Version:	1.4.0
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/libjpeg-turbo
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
	--mandir=%{_mandir}    \
	--with-jpeg8 \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
docsdir=/usr/share/doc/libjpeg-turbo-1.3.0
make DESTDIR=%{buildroot} docdir=$docsdir exampledir=$docsdir install
unset docsdir
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
