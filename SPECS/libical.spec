Summary:	The libical package contains an implementation of the iCalendar protocols and data formats.
Name:		libical
Version:	1.0.1
Release:	1
License:	GPL
URL:		https://github.com/libical/libical/releases/download/v1.0.1/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
mkdir build 
cd build 

cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=Release        \
      -DSHARED_ONLY=yes                 \
      .. 
make
cd ..

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd build
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
