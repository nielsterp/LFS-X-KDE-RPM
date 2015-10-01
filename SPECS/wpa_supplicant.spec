Summary:	WPA Supplicant is a Wi-Fi Protected Access (WPA) client and IEEE 802.1X supplicant
Name:		wpa_supplicant
Version:	2.3
Release:	1
License:	GPL
URL:		http://hostap.epitest.fi/releases
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
Source1:	blfs-bootscripts-20150304.tar.bz2
%description

%prep
%setup -q
tar xf %{SOURCE1}
cat > wpa_supplicant/.config << "EOF"
CONFIG_BACKEND=file
CONFIG_CTRL_IFACE=y
CONFIG_DEBUG_FILE=y
CONFIG_DEBUG_SYSLOG=y
CONFIG_DEBUG_SYSLOG_FACILITY=LOG_DAEMON
CONFIG_DRIVER_NL80211=y
CONFIG_DRIVER_WEXT=y
CONFIG_DRIVER_WIRED=y
CONFIG_EAP_GTC=y
CONFIG_EAP_LEAP=y
CONFIG_EAP_MD5=y
CONFIG_EAP_MSCHAPV2=y
CONFIG_EAP_OTP=y
CONFIG_EAP_PEAP=y
CONFIG_EAP_TLS=y
CONFIG_EAP_TTLS=y
CONFIG_IEEE8021X_EAPOL=y
CONFIG_IPV6=y
CONFIG_LIBNL32=y
CONFIG_PEERKEY=y
CONFIG_PKCS12=y
CONFIG_READLINE=y
CONFIG_SMARTCARD=y
CONFIG_WPS=y
CFLAGS += -I/usr/include/libnl3
CONFIG_CTRL_IFACE_DBUS=y
CONFIG_CTRL_IFACE_DBUS_NEW=y
CONFIG_CTRL_IFACE_DBUS_INTRO=y
EOF

%build
cd wpa_supplicant
make BINDIR=/sbin LIBDIR=/lib

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
mkdir %{buildroot}
cd %{buildroot}

install -vdm 755 %{buildroot}/etc
install -vdm 755 %{buildroot}/etc/sysconfig
install -vdm 755 %{buildroot}/sbin
install -vdm 755 %{buildroot}/usr/share/man/man5
install -vdm 755 %{buildroot}/usr/share/man/man8
install -vdm 755 %{buildroot}/usr/bin
install -vdm 755 %{buildroot}/usr/share/applications
install -vdm 755 %{buildroot}/usr/share/pixmaps

install -v -m755 ../../BUILD/wpa_supplicant-2.3/wpa_supplicant/wpa_{cli,passphrase,supplicant} \
		 %{buildroot}/sbin/ 
install -v -m644 ../../BUILD/wpa_supplicant-2.3/wpa_supplicant/doc/docbook/wpa_supplicant.conf.5 \
		 %{buildroot}/usr/share/man/man5/ &&
install -v -m644 ../../BUILD/wpa_supplicant-2.3/wpa_supplicant/doc/docbook/wpa_{cli,passphrase,supplicant}.8 \
		 %{buildroot}/usr/share/man/man8/

cd ../../BUILD/wpa_supplicant-2.3
pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-service-wpa
popd

cat > %{buildroot}/etc/sysconfig/ifconfig.wifi0 << "EOF"
ONBOOT="yes"
IFACE="wlan0"
SERVICE="wpa"

# Additional arguments to wpa_supplicant
WPA_ARGS=""

WPA_SERVICE="dhclient"
DHCP_START=""
DHCP_STOP=""

# Set PRINTIP="yes" to have the script print
# the DHCP assigned IP address
PRINTIP="no"

# Set PRINTALL="yes" to print the DHCP assigned values for
# IP, SM, DG, and 1st NS. This requires PRINTIP="yes".
PRINTALL="no"
EOF
%{_fixperms} %{buildroot}/*

%post
update-desktop-database
wpa_passphrase ComHem 333jytte4444 > /etc/sysconfig/wpa_supplicant-wifi0.conf

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
/sbin/*
%{_datadir}/*
%{_lib}/*
%{_sysconfdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
