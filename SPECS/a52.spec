Summary:	liba52 is a free library for decoding ATSC A/52 (also known as AC-3) streams.
Name:		a52
Version:	0.7.4
Release:	1
License:	GPL
URL:		http://liba52.sourceforge.net/files/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}dec-%{version}.tar.gz

%description

%prep
%setup -q	-n a52dec-0.7.4

%build
./configure --prefix=%{_prefix} \
            --mandir=%{_mandir} \
            --enable-shared \
            --disable-static \
            CFLAGS="-g -O2 $([ $(uname -m) = x86_64 ] && echo -fPIC)" 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install
cp liba52/a52_internal.h /usr/include/a52dec &&
install -v -m644 -D doc/liba52.txt %{buildroot}/usr/share/doc/liba52-0.7.4/liba52.txt
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