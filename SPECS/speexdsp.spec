Summary:	Speexdsp is part of the speex package
Name:		speexdsp
Version:	1.2rc3
Release:	1
License:	GPL
URL:		http://downloads.us.xiph.org/releases/speex/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}  \
            --disable-static     \
            --docdir=%{_docdir}/speexdsp-1.2rc3
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
%{_includedir}*
%{_libdir}/*
%{_docdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
