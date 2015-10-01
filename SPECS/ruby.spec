Summary:	The Ruby package contains the Ruby development environment
Name:		ruby
Version:	2.2.0
Release:	1
License:	GPL
URL:		ftp://ftp.ruby-lang.org/pub/ruby/2.0
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q 

%build
./configure --prefix=%{_prefix} \
	    --docdir=%{_docdir}/ruby-2.2.0 \
	    --enable-shared 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
