Summary:	Numerical library for C and C++ programmers
Name:		gsl
Version:	1.16
Release:	1
License:	GPL
URL:		http://ftp.gnu.org/pub/gnu/gsl
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
	--disable-static
make %{?_smp_mflags}
make html %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -d -m755 %{buildroot}/usr/share/doc/gsl-1.16 
cp doc/gsl-ref.html/* %{buildroot}/usr/share/doc/gsl-1.16
%{_fixperms} %{buildroot}/*

%post
mkdir /usr/share/doc/gsl-1.16
cp doc/gsl-ref.html/* /usr/share/doc/gsl-1.16

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
