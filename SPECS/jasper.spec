Summary:	Open-source initiative to provide a free software-based reference implementation of the JPEG-2000 codec.
Name:		jasper
Version:	1.900.1
Release:	1
License:	GPL
URL:		http://www.ece.uvic.ca/~mdadams/jasper/software/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.zip

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/jasper-1.900.1-security_fixes-2.patch 
./configure --prefix=%{_prefix}    \
            --enable-shared        \
            --disable-static       \
            --mandir=%{_mandir} 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/jasper-1.900.1 
install -v -m644 doc/*.pdf %{buildroot}/usr/share/doc/jasper-1.900.1
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
