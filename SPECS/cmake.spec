Summary:	The CMake package contains a modern toolset used for generating Makefiles.
Name:		cmake
Version:	3.1.3
Release:	1
License:	GPL
URL:		http://www.cmake.org/files/v3.1/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
./bootstrap --prefix=%{_prefix} \
            --system-libs       \
            --mandir=/share/man \
            --docdir=/share/doc/cmake-3.1.3
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
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version