Summary:	The libnl suite is a collection of libraries providing APIs to netlink protocol 
Name:		libnl
Version:	3.2.25
Release:	1
License:	GPL
URL:		http://www.infradead.org/~tgr/libnl/files
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"        \
	CXXFLAGS="%{optflags}"      \
	--prefix=%{_prefix}         \
	--sysconfdir=%{_sysconfdir} \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
