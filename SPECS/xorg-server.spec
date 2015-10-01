Summary:	The Xorg Server is the core of the X Window system.
Name:		xorg-server
Version:	1.17.1
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
Patch0:		xorg-server-1.17.1-add_prime_support-1.patch
Patch1:		xorg-server-1.17.1-fix_modesetting-1.patch
%description

%prep
%setup -q
patch -Np1 -i  	../../SOURCES/xorg-server-1.17.1-add_prime_support-1.patch
patch -Np1 -i  	../../SOURCES/xorg-server-1.17.1-fix_modesetting-1.patch

%build
./configure \
        CFLAGS="%{optflags}"              \
	CXXFLAGS="%{optflags}"            \
	--prefix=%{_prefix}               \
	--sysconfdir=%{_sysconfdir}       \
	--localstatedir=%{_localstatedir} \
	--disable-static                  \
        --with-xkb-output=/var/lib/xkb
make %{?_smp_mflags} 
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install


%{_fixperms} %{buildroot}/*

%post
mkdir -pv /etc/X11/xorg.conf.d

cat >> /etc/sysconfig/createfiles << "EOF"
/tmp/.ICE-unix dir 1777 root root
/tmp/.X11-unix dir 1777 root root
EOF

chmod u+s /usr/bin/Xorg
%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
%{_sharedstatedir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
