Summary:	An interface to the X Window System protocol.
Name:		libxcb
Version:	1.11
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description
The libxcb package provides an interface to the X Window System
protocol, which replaces the current Xlib interface. Xlib can also use
XCB as a transport layer, allowing software to make requests and receive
responses with both.

%prep
%setup -q

%build
sed -e "s/pthread-stubs//" -i configure.ac
autoreconf -fi
./configure \
	CFLAGS="%{optflags}"                   \
	CXXFLAGS="%{optflags}"                 \
	--prefix=%{_prefix}                    \
	--sysconfdir=%{_sysconfdir}            \
	--localstatedir=%{_localstatedir}      \
	--disable-static                       \
        --docdir=%{_docdir}/libxcb-1.9.1       \
        --enable-xinput                        \
        --enable-xkb

make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/* 
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
