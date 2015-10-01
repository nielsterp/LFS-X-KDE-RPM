Summary:	Contains a library which allows you to access the data held on the MusicBrainz server.
Name:		libmusicbrainz
Version:	5.1.0
Release:	1
License:	GPL
URL:		https://github.com/metabrainz/libmusicbrainz/releases/download/release-5.1.0/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
mkdir build &&
cd    build &&

cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .. 
make
cd ..

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd build
make DESTDIR=%{buildroot} install
cd ..

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
