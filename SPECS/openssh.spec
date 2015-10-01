Summary:	Free version of the SSH connectivity tools
Name:		openssh
Version:	6.7p1
Release:	1
License:	BSD
URL:		http://openssh.org
Group:		BLFS/Security
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{name}-%{version}.tar.gz
Source1:	http://www.linuxfromscratch.org/blfs/downloads/7.7/blfs-bootscripts-20150304.tar.bz2

%description
The OpenSSH package contains ssh clients and the sshd daemon. This is
useful for encrypting authentication and subsequent traffic over a 
network. The ssh and scp commands are secure implementions of telnet 
and rcp respectively.
%prep
%setup -q
tar xf %{SOURCE1}
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--sysconfdir=/etc/ssh \
	--datadir=/usr/share/sshd \
	--with-md5-passwords \
	--with-privsep-path=/var/lib/sshd
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
mkdir -vp %{buildroot}/var/lib/sshd
echo "PermitRootLogin yes" >> %{buildroot}/etc/ssh/sshd_config
#	Install daemon script
pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-sshd
popd
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post
/sbin/ldconfig
chown -v root:sys /var/lib/sshd
if ! getent group sshd >/dev/null; then
	groupadd -g 50 sshd
fi
if ! getent passwd sshd >/dev/null; then
	useradd -c 'sshd PrivSep' -d /var/lib/sshd -g sshd -s /bin/false -u 50 sshd
fi
ssh-keygen -A
%postun
/sbin/ldconfig
if getent passwd sshd >/dev/null; then
	userdel sshd
fi
if getent group sshd >/dev/null; then
	groupdel sshd
fi
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
/etc/ssh/*
/etc/rc.d/init.d/sshd
/etc/rc.d/rc0.d/K30sshd
/etc/rc.d/rc1.d/K30sshd
/etc/rc.d/rc2.d/K30sshd
/etc/rc.d/rc3.d/S30sshd
/etc/rc.d/rc4.d/S30sshd
/etc/rc.d/rc5.d/S30sshd
/etc/rc.d/rc6.d/K30sshd
%{_bindir}/*
%{_sbindir}/*
%{_libexecdir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%attr(700,root,sys)/var/lib/sshd
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 6.7p1-1
*	Sun Sep 01 2013 nielsterp <nielsterp@comhem.se> 6.2p2-1
-	Upgrade to ver. 6.2p2
*	Wed May 22 2013 baho-utot <baho-utot@columbus.rr.com> 6.2p1-1
-	Initial build.	First version
