Summary:	Libevent is an asynchronous event notification software library.
Name:		libevent
Version:	2.0.22
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/levent/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}-stable.tar.gz

%description

%prep
%setup -q -n %{name}-%{version}-stable

%build
./configure --prefix=%{_prefix} \
	    --disable-static
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

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
