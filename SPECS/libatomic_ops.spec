Summary:	Implementations for atomic memory update operations
Name:		libatomic_ops
Version:	7.4.2
Release:	1
License:	GPL
URL:		http://www.ivmaisoft.com/_bin/atomic_ops//libatomic_ops-7.4.2.tar.gz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q 

%build
sed -i 's#pkgdata#doc#' doc/Makefile.am
autoreconf -fi
./configure --prefix=%{_prefix} \
            --enable-shared     \
            --disable-static    \
            --docdir=/usr/share/doc/libatomic_ops-7.4.2
make  
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
mv -v   %{buildroot}/usr/share/libatomic_ops/* \
        %{buildroot}/usr/share/doc/libatomic_ops-7.4.2 &&
rm -vrf %{buildroot}/usr/share/libatomic_ops
%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_docdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
