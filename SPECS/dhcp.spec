Summary:	The ISC DHCP package contains both the client and server programs for DHCP
Name:		dhcp
Version:	4.3.1
Release:	1
License:	GPL
URL:		ftp://ftp.isc.org/isc/dhcp/4.3.0
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
Source1:	blfs-bootscripts-20150304.tar.bz2

%description

%prep
%setup
tar xf %{SOURCE1}
patch -Np1 -i ../../SOURCES/dhcp-4.3.1-missing_ipv6-1.patch
patch -Np1 -i ../../SOURCES/dhcp-4.3.1-client_script-1.patch

%build
CFLAGS="-D_PATH_DHCLIENT_SCRIPT='\"/sbin/dhclient-script\"'         \
        -D_PATH_DHCPD_CONF='\"/etc/dhcp/dhcpd.conf\"'               \
        -D_PATH_DHCLIENT_CONF='\"/etc/dhcp/dhclient.conf\"'"        \
./configure --prefix=%{_prefix}                                     \
            --sysconfdir=%{_sysconfdir}/dhcp                        \
            --localstatedir=%{_localstatedir}                       \
            --with-srv-lease-file=%{_sharedstatedir}/dhcpd/dhcpd.leases       \
            --with-srv6-lease-file=%{_sharedstatedir}/dhcpd/dhcpd6.leases     \
            --with-cli-lease-file=%{_sharedstatedir}/dhclient/dhclient.leases \
            --with-cli6-lease-file=%{_sharedstatedir}/dhclient/dhclient6.leases
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} -C client install
mkdir %{buildroot}/sbin
mv -v %{buildroot}/usr/sbin/dhclient %{buildroot}/sbin 
install -v -m755 client/scripts/linux %{buildroot}/sbin/dhclient-script

cat > %{buildroot}/etc/dhcp/dhclient.conf << "EOF"
# Begin /etc/dhcp/dhclient.conf
#
# Basic dhclient.conf(5)

#prepend domain-name-servers 127.0.0.1;
request subnet-mask, broadcast-address, time-offset, routers,
        domain-name, domain-name-servers, domain-search, host-name,
        netbios-name-servers, netbios-scope, interface-mtu,
        ntp-servers;
require subnet-mask, domain-name-servers;
#timeout 60;
#retry 60;
#reboot 10;
#select-timeout 5;
#initial-interval 2;

# End /etc/dhcp/dhclient.conf
EOF

install -v -dm 755 %{buildroot}/var/lib/dhclient
install -v -dm 755 %{buildroot}/etc/sysconfig

pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-service-dhclient
popd

cat > %{buildroot}/etc/sysconfig/ifconfig.eth0 << "EOF"
ONBOOT="yes"
IFACE="eth0"
SERVICE="dhclient"
DHCP_START=""
DHCP_STOP=""

# Set PRINTIP="yes" to have the script print
# the DHCP assigned IP address
PRINTIP="no"

# Set PRINTALL="yes" to print the DHCP assigned values for
# IP, SM, DG, and 1st NS. This requires PRINTIP="yes".
PRINTALL="no"
EOF

cat > %{buildroot}/etc/sysconfig/ifconfig.wifi0 << "EOF"
ONBOOT="no"
IFACE="wlan0"
SERVICE="dhclient"
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

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_lib}/*
/sbin/*
%_datadir/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
