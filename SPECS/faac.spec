Summary:	FAAC is an encoder for a lossy sound compression scheme specified in MPEG-2 Part 7 and MPEG-4 Part 3 standards.
Name:		faac
Version:	1.28
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/faac/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
Patch0:		faac-1.28-glibc_fixes-1.patch
%description

%prep
%setup -q
patch -Np1 -i ../../SOURCES/faac-1.28-glibc_fixes-1.patch
%build
sed -i -e '/obj-type/d' -e '/Long Term/d' frontend/main.c
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--disable-static
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%check

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
