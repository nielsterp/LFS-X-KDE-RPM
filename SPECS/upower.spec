Summary:	Interface to enumerating power devices
Name:		upower
Version:	0.9.23
Release:	1
License:	GPL
URL:		http://upower.freedesktop.org/releases/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}               \
            --sysconfdir=%{_sysconfdir}       \
            --localstatedir=%{_localstatedir} \
            --enable-deprecated  \
            --disable-static &&
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
%{_sysconfdir}/*
%{_lib}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_datadir}

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
