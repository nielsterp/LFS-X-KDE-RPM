Summary:	The Quasar DV Codec (libdv) is a software CODEC for DV video
Name:		libdv
Version:	1.0.0
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/libdv
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
	--disable-xv \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d      %{buildroot}/usr/share/doc/libdv-1.0.0
install -v -m644 README* %{buildroot}/usr/share/doc/libdv-1.0.0
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
