Summary:	Daemon that displays passive pop-up notifications
Name:		notification-daemon
Version:	3.14.1
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/notification-daemon/0.7
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"    		    \
	CXXFLAGS="%{optflags}"    		    \
	--prefix=%{_prefix}        		    \
	--sysconfdir=%{_sysconfdir} 		    \
	--libexecdir=%{_libdir}/notification-daemon \
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
%{_libdir}/*
%{_datadir}/*
%{_sysconfdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
