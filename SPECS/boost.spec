Summary:	A set of free peer-reviewed portable C++ source libraries
Name:		boost
Version:	1_57_0
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/boost
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}_%{version}.tar.bz2
%description

%prep
%setup -q -n boost_1_57_0

%build
BOOST_ROOT=`pwd`
export BOOST_ROOT
sed -e '1 i#ifndef Q_MOC_RUN' \
    -e '$ a#endif'            \
    -i boost/type_traits/detail/has_binary_operator.hpp
./bootstrap.sh --prefix=%{buildroot}/usr/ --with-toolset=gcc --with-icu
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
install -d -m 755 %{buildroot}/usr/
./b2 --layout=system install threading=multi link=shared

%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*


%changelog
*	Mon Dec 02 2013 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
