Summary:	Simple Authentication and Security Layer.
Name:		cyrus-sasl
Version:	2.1.26
Release:	1
License:	GPL
URL:		ftp://ftp.cyrusimap.org/cyrus-sasl/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/cyrus-sasl-2.1.26-fixes-3.patch 
autoreconf -fi 

./configure --prefix=%{_prefix}                   \
            --sysconfdir=%{_sysconfdir}           \
            --enable-auth-sasldb                \
            --with-dbpath=/var/lib/sasl/sasldb2 \
            --with-saslauthd=/var/run/saslauthd 
make -j1

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
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version