Summary:	Interactive spell checking program and the Aspell libraries
Name:		aspell
Version:	0.60.6.1
Release:	1
License:	GPL
URL:		http://ftp.gnu.org/gnu/aspell
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} 
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/aspell-0.60.6.1/aspell{,-dev}.html &&
install -v -m644 manual/aspell.html/* \
    %{buildroot}/usr/share/doc/aspell-0.60.6.1/aspell.html &&
install -v -m644 manual/aspell-dev.html/* \
    %{buildroot}/usr/share/doc/aspell-0.60.6.1/aspell-dev.html
install -v -m 755 scripts/ispell %{buildroot}/usr/bin/
install -v -m 755 scripts/spell %{buildroot}/usr/bin/
%{_fixperms} %{buildroot}/*

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
