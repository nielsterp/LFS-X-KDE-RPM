Summary:	The libmpeg2 package contains a library for decoding MPEG-2 and MPEG-1 video streams
Name:		libmpeg2
Version:	0.5.1
Release:	1
License:	GPL
URL:		http://libmpeg2.sourceforge.net/files
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
sed -i 's/static const/static/' libmpeg2/idct_mmx.c
./configure --prefix=%{_prefix}
make 
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/mpeg2dec-0.5.1 &&
install -v -m644 README doc/libmpeg2.txt %{buildroot}/usr/share/doc/mpeg2dec-0.5.1
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
