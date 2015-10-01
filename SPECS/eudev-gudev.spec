Summary:	Programs for dynamic creation of device nodes
Name:		eudev-gudev
Version:	2.1.1
Release:	1
License:	GPLv2
URL:		http://www.freedesktop.org/wiki/Software/systemd/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://dev.gentoo.org/~blueness/eudev/eudev-2.1.1.tar.gz
%description
The Eudev package contains programs for dynamic creation of device nodes.
%prep
tar xf %{SOURCE0}

cd %{_builddir}
cd eudev-%{version}
sed -r -i 's|/usr(/bin/test)|\1|'         test/udev-test.pl  &&

./configure --prefix=%{_prefix}         \
            --bindir=/sbin              \
            --sbindir=/sbin             \
            --libdir=%{_libdir}         \
            --sysconfdir=%{_sysconfdir} \
            --libexecdir=%{_lib}        \
            --with-rootprefix=          \
            --with-rootlibdir=/lib      \
            --enable-split-usr          \
            --enable-libkmod            \
            --enable-rule_generator     \
            --enable-keymap             \
            --disable-introspection     \
            --disable-gtk-doc-html      \
            --with-firmware-path=/lib/firmware
%build
cd %{_builddir}/eudev-%{version}
make %{?_smp_mflags}
%install
cd %{_builddir}/eudev-%{version}
mkdir -pv /lib/{firmware,eudev}
mkdir -pv /lib/eudev/rules.d
mkdir -pv /etc/eudev/rules.d
make DESTDIR=%{buildroot} install
tar -xvf ../../SOURCES/eudev-%{version}-manpages.tar.bz2 -C /usr/share
tar -xvf ../../SOURCES/udev-lfs-20140408.tar.bz2
make -f udev-lfs-20140408/Makefile.lfs install
%post
/sbin/ldconfig
/sbin/eudevadm hwdb --update
bash /lib/eudev/init-net-rules.sh || true
%postun	-p /sbin/ldconfig
%files 
%defattr(-,root,root)
%{_sysconfdir}/*
%{_lib}/*
/sbin/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 2.1.1
*	Tue Jun 17 2014 baho-utot <baho-utot@columbus.rr.com> 208-1
*	Fri Aug 30 2013 baho-utot <baho-utot@columbus.rr.com> 206-2
-	fix perms on /lib/usev/init-net-rules.sh
*	Sat Aug 24 2013 baho-utot <baho-utot@columbus.rr.com> 206-1
-	Update version
*	Sat May 11 2013 baho-utot <baho-utot@columbus.rr.com> 204-1
-	Update version to 204
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 202-1
-	Intial version
