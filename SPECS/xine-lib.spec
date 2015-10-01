Summary:	The Xine Libraries package contains xine libraries. 
Name:		xine-lib
Version:	1.2.6
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/xine/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}    \
            --disable-vcd          \
            --with-external-dvdnav \
            --docdir=%{_docdir}/xine-lib-1.2.6 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install

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
