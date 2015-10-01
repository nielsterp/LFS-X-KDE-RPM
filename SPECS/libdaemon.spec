Summary:	The libdaemon package is a lightweight C library that eases the writing of UNIX daemons.
Name:		libdaemon
Version:	0.14
Release:	1
License:	GPL
URL:		http://0pointer.de/lennart/projects/libdaemon/libdaemon-0.14.tar.gz
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
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
