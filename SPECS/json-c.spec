Summary:	Reference counting object model
Name:		json-c
Version:	0.12
Release:	1
License:	GPL
URL:		https://s3.amazonaws.com/json-c_releases/releases
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
sed -i s/-Werror// Makefile.in             
./configure --prefix=%{_prefix} \
	    --disable-static 
make -j1
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
