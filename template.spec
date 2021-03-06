Summary:	
Name:		
Version:	
Release:	1
License:	GPL
URL:		
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q 

%build

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)

%changelog
*	Sun Jun 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version