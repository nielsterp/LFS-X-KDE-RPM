Summary:	Imlib2 is a graphics library for fast file loading, saving, rendering and manipulation.
Name:		imlib2
Version:	1.4.6
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/enlightenment/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
sed -i 's/@my_libs@//' imlib2-config.in   
sed -e '/DGifOpen/s:fd:&, NULL:'           \
    -e '/DGifCloseFile/s:gif:&, NULL:'     \
    -i src/modules/loaders/loader_gif.c
./configure \
	CFLAGS="%{optflags}"   \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix}    \
	--disable-static
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/imlib2-1.4.6 
install -v -m644    doc/{*.gif,index.html} \
                    %{buildroot}/usr/share/doc/imlib2-1.4.6
%{_fixperms} %{buildroot}/*

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

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
