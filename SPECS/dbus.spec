Summary:	D-Bus is a message bus system
Name:		dbus
Version:	1.8.16
Release:	1
License:	GPL
URL:		http://dbus.freedesktop.org/releases/dbus
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	dbus-%{version}.tar.gz
Source1:	blfs-bootscripts-20150304.tar.bz2

%description

%prep
%setup -q 
tar xf %{SOURCE1}

%build
./configure --prefix=%{_prefix}                   \
	    --sysconfdir=%{_sysconfdir}           \
	    --localstatedir=%{_localstatedir}     \
	    --libexecdir=%{_libdir}/dbus-1.0      \
	    --with-console-auth-dir=/run/console/ \
	    --without-systemdsystemunitdir        \
	    --disable-systemd                     \
	    --disable-static	                  \
	    --disable-xml-docs
make

	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
mv -v %{buildroot}/usr/share/doc/dbus %{buildroot}/usr/share/doc/dbus-1.8.16

pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-dbus
popd

%{_fixperms} %{buildroot}/*

%pre
egrep -i "^messagebus" /etc/group
if [ $? -eq 0 ]; then
   echo "Group $GROUPID exists in /etc/group"
else
    groupadd -g 18 messagebus
    useradd -c "D-Bus Message Daemon User" -d /var/run/dbus -u 18 -g messagebus -s /bin/false messagebus
fi

%post
dbus-uuidgen --ensure

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%dir /etc/dbus-1/session.d
%dir /etc/dbus-1/system.d
%dir /etc/sysconfig
%dir /var/lib/dbus
%dir /var/run/dbus
%attr(4750, root, messagebus)  /usr/lib/dbus-1.0/dbus-daemon-launch-helper
%{_libdir}/*
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
