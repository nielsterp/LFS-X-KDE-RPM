Summary:	libmad is a high-quality MPEG audio decoder capable of 24-bit output
Name:		libmad
Version:	0.15.1b
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/mad
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
Patch0:		libmad-0.15.1b-fixes-1.patch
%description

%prep
%setup -q
%patch0 -p1

%build
sed "s@AM_CONFIG_HEADER@AC_CONFIG_HEADERS@g" -i configure.ac
touch NEWS AUTHORS ChangeLog
autoreconf -fi

./configure --prefix=%{_prefix} \
	    --disable-static
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%post
cat > /usr/lib/pkgconfig/mad.pc << "EOF"
prefix=/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: mad
Description: MPEG audio decoder
Requires:
Version: 0.15.1b
Libs: -L${libdir} -lmad
Cflags: -I${includedir}
EOF

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
