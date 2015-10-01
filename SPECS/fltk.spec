Summary:	FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit. 
Name:		fltk
Version:	1.3.3
Release:	1
License:	GPL
URL:		http://fltk.org/pub/fltk/1.3.3/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}-source.tar.gz
%description

%prep
%setup -q

%build
sed -i -e '/cat./d' documentation/Makefile
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--enable-shared
make
make -C documentation html
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make docdir=/usr/share/doc/fltk-1.3.3 DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_docdir}/*
%{_mandir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
