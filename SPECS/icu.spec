Summary:	International Components for Unicode (ICU)
Name:		icu
Version:	54.1
Release:	1
License:	GPL
URL:		http://download.icu-project.org/files/icu4c/54.1/icu4c-54_1-src.tgz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}4c-54_1-src.tgz
%description

%prep
%setup -q -n icu

%build
cd source
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} 
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd source
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
%{_sbindir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
