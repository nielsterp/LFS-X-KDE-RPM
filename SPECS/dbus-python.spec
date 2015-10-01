Summary:	D-Bus Python provides Python bindings to the D-Bus.
Name:		dbus-python
Version:	1.2.0
Release:	1
License:	GPL
URL:		http://dbus.freedesktop.org/releases/dbus-python/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q 

%build
mkdir python2 
pushd python2 
PYTHON=/usr/bin/python     \
../configure --prefix=%{_prefix} \
	      --docdir=%{_docdir}/dbus-python-1.2.0 
make 
popd

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make -C python2 DESTDIR=%{buildroot} install

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
