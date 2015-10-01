Summary:	Low-level cryptographic library
Name:		nettle
Version:	2.7.1
Release:	1
License:	GPL
URL:		http://ftp.gnu.org/gnu/nettle
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
chmod -v 755 %{buildroot}/usr/lib/libhogweed.so.2.5 %{buildroot}/usr/lib/libnettle.so.4.7
install -v -m755 -d %{buildroot}/usr/share/doc/nettle-2.7.1
install -v -m644 nettle.html %{buildroot}/usr/share/doc/nettle-2.7.1
rm -rf %{buildroot}/usr/share/info/dir
%{_fixperms} %{buildroot}/*

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

