Summary:	Linux kernel packet control tool
Name:		iptables
Version:	1.4.21
Release:	2
License:	GPLv2
URL:		http://www.netfilter.org/projects/iptables
Group:		BLFS/ Security
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.netfilter.org/projects/iptables/files/%{name}-%{version}.tar.bz2
Source1:	http://www.linuxfromscratch.org/blfs/downloads/7.7/blfs-bootscripts-20150304.tar.bz2
%description
The next part of this chapter deals with firewalls. The principal 
firewall tool for Linux is Iptables. You will need to install 
Iptables if you intend on using any form of a firewall.
%prep
%setup -q
tar xf %{SOURCE1}
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--disable-silent-rules \
	--prefix=%{_prefix} \
	--exec-prefix= \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--with-xtlibdir=%{_libdir}/iptables \
	--with-pkgconfigdir=%{_libdir}/pkgconfig \
	--enable-libipq \
	--enable-devel
	
make V=0 %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
ln -sfv ../../sbin/xtables-multi %{buildroot}%{_libdir}/iptables-xml
#for file in libip4tc libip6tc libipq libiptc libxtables
#do
#  ln -sfv ../../lib/`readlink %{buildroot}/lib/${file}.so` %{buildroot}/usr/lib/${file}.so
#  rm -v %{buildroot}/lib/${file}.so
#done
#	Install daemon script
pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-iptables
popd
find %{buildroot} -name '*.a'  -delete
find %{buildroot} -name '*.la' -delete
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
/etc/rc.d/init.d/*
/etc/rc.d/rc3.d/*
/etc/rc.d/rc4.d/*
/etc/rc.d/rc5.d/*
/sbin/*
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/iptables/*
%{_libdir}/pkgconfig/*
%{_libdir}/iptables-xml
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man8/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 1.4.21
*	Fri May 31 2013 baho-utot <baho-utot@columbus.rr.com> 1.4.18-2
-	fixed directories, place into /usr/<path>
*	Thu May 23 2013 baho-utot <baho-utot@columbus.rr.com> 1.4.18-1
-	Initial build.	First version