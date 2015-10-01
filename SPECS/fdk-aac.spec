Summary:	Fdk-aac package provides the Fraunhofer FDK AAC library
Name:		fdk-aac
Version:	0.1.3
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/opencore-amr/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --disable-static
make	

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
%{_includedir}/*
%{_libdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
