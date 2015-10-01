Summary:	Linux API header files
Name:		linux-api-headers
Version:	4.2.2
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/
Group:		System Environment/Kernel
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.kernel.org/pub/linux/kernel/v4.x/linux-%{version}.tar.xz
BuildArch:	noarch
%description
The Linux API Headers expose the kernel's API for use by Glibc.
%prep
%setup -q -n linux-%{version}
%build
make mrproper
make headers_check
%install
cd %{_builddir}/linux-%{version}
make INSTALL_HDR_PATH=%{buildroot}%{_prefix} headers_install
find /%{buildroot}%{_includedir} \( -name .install -o -name ..install.cmd \) -delete
%files
%defattr(-,root,root)
%{_includedir}/asm-generic/*
%{_includedir}/asm/*
%{_includedir}/drm/*
%{_includedir}/linux
%{_includedir}/mtd/*
%{_includedir}/rdma/*
%{_includedir}/scsi/*
%{_includedir}/sound/*
%{_includedir}/video/*
%{_includedir}/xen/*
%{_includedir}/misc/cxl.h
%changelog
*	Thu Oct 01 2015 nielsterp <nielsterp@comhem.se> 4.2.2
*	Thu Sep 03 2015 nielsterp <nielsterp@comhem.se> 4.2
*	Thu Aug 27 2015 nielsterp <nielsterp@comhem.se> 4.1.6
*	Thu Aug 13 2015 nielsterp <nielsterp@comhem.se> 4.1.5
*	Sun Aug 09 2015 nielsterp <nielsterp@comhem.se> 4.1.4
*	Sat Jul	25 2015 nielsterp <nielsterp@comhem.se> 4.1.3
*	Sun Jul 05 2015 nielsterp <nielsterp@comhem.se> 4.1.1
*	Wed Feb 18 2015 nielsterp <nielsterp@comhem.se> 3.19
*	Tue Dec 26 2014 nielsterp <nielsterp@comhem.se> 3.18.1
*	Tue Nov 18 2014 nielsterp <nielsterp@comhem.se> 3.17.3-1
*	Sun Nov 09 2014 nielsterp <nielsterp@comhem.se> 3.17.2-1
*	Sat Mar 22 2014 baho-utot <baho-utot@columbus.rr.com> 3.13.3-1
*	Sat Aug 31 2013 baho-utot <baho-utot@columbus.rr.com> 3.10.10-1
*	Sat Aug 24 2013 baho-utot <baho-utot@columbus.rr.com> 3.10.9-1
*	Thu Jun 27 2013 baho-utot <baho-utot@columbus.rr.com> 3.9.7-1
*	Wed May 15 2013 baho-utot <baho-utot@columbus.rr.com> 3.9.2-1
*	Sat May 11 2013 baho-utot <baho-utot@columbus.rr.com> 3.9.1-1
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 3.9-1
*	Mon Apr 1 2013 baho-utot <baho-utot@columbus.rr.com> 3.8.5-1
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 3.8.3-1
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 3.8.1-1
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 3.5.2-1
-	initial version
