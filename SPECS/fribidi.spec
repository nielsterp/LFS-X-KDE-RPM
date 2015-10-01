Summary:	The FriBidi package is an implementation of the Unicode Bidirectional Algorithm (BIDI). 
Name:		fribidi
Version:	0.19.6
Release:	1
License:	GPL
URL:		http://fribidi.org/download/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
sed -i "s|glib/gstrfuncs\.h|glib.h|" charset/fribidi-char-sets.c
sed -i "s|glib/gmem\.h|glib.h|"      lib/mem.h
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
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
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version