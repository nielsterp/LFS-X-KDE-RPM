Summary:	Contains the libquicktime library
Name:		libquicktime
Version:	1.2.4
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/libquicktime/libquicktime-1.2.4.tar.gz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/libquicktime-1.2.4-ffmpeg2-1.patch
./configure --prefix=%{_prefix}                    \
            --enable-gpl                           \
            --without-doxygen                      \
            --docdir=%{_docdir}/libquicktime-1.2.4 \
            --with-libdv
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/libquicktime-1.2.4 
install -v -m644    README doc/{*.txt,*.html,mainpage.incl} \
                    %{buildroot}/usr/share/doc/libquicktime-1.2.4
%{_fixperms} %{buildroot}/*

%check

%post

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
