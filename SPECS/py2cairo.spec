Summary:	Py2cairo provides Python 2 bindings to Cairo.
Name:		py2cairo
Version:	1.10.0
Release:	1
License:	GPL
URL:		http://cairographics.org/releases/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix}
./waf build	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
./waf install -v --nocache --destdir=%{buildroot}
%{_fixperms} %{buildroot}/*

%check

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
