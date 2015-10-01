Summary:	Open-source audio processing library
Name:		soundtouch
Version:	1.8.0
Release:	1
License:	GPL
URL:		http://www.surina.net/soundtouch/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q -n soundtouch

%build
sed "s@AM_CONFIG_HEADER@AC_CONFIG_HEADERS@g" -i configure.ac 
./bootstrap 

./configure --prefix=%{_prefix}
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make pkgdocdir=/usr/share/doc/soundtouch-1.8.0 DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post

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