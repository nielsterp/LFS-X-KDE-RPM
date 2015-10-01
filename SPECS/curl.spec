Summary:	An URL retrieval utility and library
Name:		curl
Version:	7.42.1
Release:	1
License:	MIT
URL:		http://curl.haxx.se
Group:		BLFS/NetworkingLibraries
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.lzma
Requires:	ca-certificates >= 20130524
%description
The cURL package contains an utility and a library used for 
transferring files with URL syntax to any of the following 
protocols: FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, 
DICT, LDAP, LDAPS and FILE. Its ability to both download and 
upload files can be incorporated into other programs to support
functions like streaming media.
%prep
%setup -q
sed -i '/--static-libs)/{N;s#echo .*#echo #;}' curl-config.in
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--disable-static \
	--enable-threaded-resolver \
	--with-ca-path=/etc/ssl/certs
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
find %{buildroot}/%{_libdir} -name '*.la' -delete
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
/usr/share/aclocal/libcurl.m4
%changelog
*	Wed Oct 30 2013 nielsterp <nielsterp@comhem.se> 7.32.0-1
-	Updated to ver. 7.32.0
*	Wed May 29 2013 baho-utot <baho-utot@columbus.rr.com> 7.30.0-1
-	Initial build.	First version