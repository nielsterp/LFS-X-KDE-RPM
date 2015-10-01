Summary:	Set of co-operative tools that make networking simple and straightforward.
Name:		NetworkManager
Version:	1.0.0
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/NetworkManager/1.0/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
Source1:	blfs-bootscripts-20150304.tar.bz2

%description

%prep
%setup -q
tar -xf ../../SOURCES/blfs-bootscripts-20150304.tar.bz2

%build
./configure --prefix=%{_prefix}               \
            --sysconfdir=%{_sysconfdir}       \
            --localstatedir=%{_localstatedir} \
            --with-nmtui                      \
            --disable-ppp                     \
            --with-systemdsystemunitdir=no    \
            --docdir=%{_docdir}/network-manager-1.0.0 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install

cat >> %{buildroot}/etc/NetworkManager/NetworkManager.conf << "EOF"
[main]
plugins=keyfile
EOF

pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot}  install-networkmanager
popd

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
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
