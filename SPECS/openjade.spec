Summary:	The OpenJade package contains a DSSSL engine
Name:		openjade
Version:	1.3.2
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/openjade
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q
patch -Np1 -i ../../SOURCES/openjade-1.3.2-gcc_4.6-1.patch
%build
sed -i -e '/getopts/{N;s#&G#g#;s#do .getopts.pl.;##;}' \
       -e '/use POSIX/ause Getopt::Std;' msggen.pl
./configure	--prefix=%{_prefix} \
		--enable-http                                \
		--disable-static                             \
		--enable-default-catalog=/etc/sgml/catalog   \
		--enable-default-search-path=/usr/share/sgml \
		--datadir=/usr/share/sgml/openjade-1.3.2 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-man
install -v -m644 dsssl/catalog %{buildroot}/usr/share/sgml/openjade-1.3.2/ 
install -v -m644 dsssl/*.{dtd,dsl,sgm} %{buildroot}/usr/share/sgml/openjade-1.3.2                             



%{_fixperms} %{buildroot}/*

%post
ln -v -sf openjade /usr/bin/jade                               
ln -v -sf libogrove.so /usr/lib/libgrove.so                    
ln -v -sf libospgrove.so /usr/lib/libspgrove.so                
ln -v -sf libostyle.so /usr/lib/libstyle.so                    


install-catalog --add /etc/sgml/openjade-1.3.2.cat  \
    /usr/share/sgml/openjade-1.3.2/catalog                     

install-catalog --add /etc/sgml/sgml-docbook.cat    \
    /etc/sgml/openjade-1.3.2.cat

echo "SYSTEM \"http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd\" \
    \"/usr/share/xml/docbook/xml-dtd-4.5/docbookx.dtd\"" >> \
    /usr/share/sgml/openjade-1.3.2/catalog

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
/usr/man/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
