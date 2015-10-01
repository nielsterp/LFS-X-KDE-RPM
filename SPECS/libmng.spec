Summary:	Multiple-image Network Graphics (MNG)
Name:		libmng
Version:	2.0.2
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/libmng
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
sed -i "s:#include <jpeg:#include <stdio.h>\n&:" libmng_types.h
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/libmng-2.0.2
install -v -m644 doc/*.txt %{buildroot}/usr/share/doc/libmng-2.0.2
%{_fixperms} %{buildroot}/*

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
