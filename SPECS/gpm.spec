Summary:	The GPM package contains a mouse server for the console and xterm.
Name:		gpm
Version:	1.20.7
Release:	1
License:	GPL
URL:		http://www.nico.schottelius.org/software/gpm/archives/gpm-1.20.7.tar.bz2
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.nico.schottelius.org/software/gpm/archives/%{name}-%{version}.tar.bz2
Source1:        http://www.linuxfromscratch.org/blfs/downloads/svn/blfs-bootscripts-20150304.tar.bz2
	
%description

%prep
%setup -q
tar xf %{SOURCE1}

%build
./autogen.sh &&
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
	--bindir=%{_bindir}    \
	--libdir=%{_libdir}    \
	--sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install 
  
pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-gpm
popd
cat > /etc/sysconfig/mouse << "EOF"
MDEVICE="/dev/psaux"
PROTOCOL="imps2"
GPMOPTS=""

# End /etc/sysconfig/mouse
EOF
%{_fixperms} %{buildroot}/*

%check

%post

%postun

%clean
rm -rf %{buildroot} %{pkgdir}

%files 
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}/*
%{_sysconfdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
