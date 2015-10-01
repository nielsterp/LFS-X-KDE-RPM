Summary:	Xorg application.
Name:		luit
Version:	1.1.1
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q
      line1="#ifdef _XOPEN_SOURCE"
      line2="#  undef _XOPEN_SOURCE"
      line3="#  define _XOPEN_SOURCE 600"
      line4="#endif"
 
      sed -i -e "s@#ifdef HAVE_CONFIG_H@$line1\n$line2\n$line3\n$line4\n\n&@" sys.c
      unset line1 line2 line3 line4

%build
./configure \
	CFLAGS="%{optflags}"              \
	CXXFLAGS="%{optflags}"            \
	--prefix=%{_prefix}               \
	--sysconfdir=%{_sysconfdir}       \
	--localstatedir=%{_localstatedir} \
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
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
