Summary:	Yasm is a complete rewrite of the NASM-2.10.09 assembler
Name:		yasm
Version:	1.3.0
Release:	1
License:	GPL
URL:		http://www.tortall.net/projects/yasm/releases
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
sed -i 's#) ytasm.*#)#' Makefile.in
./configure --prefix=%{_prefix} 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
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
