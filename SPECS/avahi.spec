Summary:	The Avahi package is a system which facilitates service discovery on a local network
Name:		avahi
Version:	0.6.31
Release:	1
License:	GPL
URL:		http://avahi.org/download
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
Source1:	blfs-bootscripts-20150304.tar.bz2
%description

%prep
%setup -q
tar xf %{SOURCE1}
%build
sed -i 's/\(CFLAGS=.*\)-Werror \(.*\)/\1\2/' configure 

sed -e 's/-DG_DISABLE_DEPRECATED=1//' \
    -e '/-DGDK_DISABLE_DEPRECATED/d'  \
    -i avahi-ui/Makefile.in
    
./configure --prefix=%{_prefix}               \
            --sysconfdir=%{_sysconfdir}       \
            --localstatedir=%{_localstatedir} \
            --disable-static                  \
            --disable-mono                    \
            --disable-monodoc                 \
            --disable-python                  \
            --disable-qt3                     \
            --disable-qt4                     \
            --enable-core-docs                \
            --with-distro=none
make 

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install

pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-avahi
popd

%{_fixperms} %{buildroot}/*

%pre
egrep -i "^avahi" /etc/group
if [ $? -eq 0 ]; then
   echo "User $USERID exists in /etc/passwd"
else
    groupadd -fg 84 avahi &&
    useradd -c "Avahi Daemon Owner" -d /var/run/avahi-daemon -u 84 \
        -g avahi -s /bin/false avahi
    groupadd -fg 86 netdev

fi
        

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version