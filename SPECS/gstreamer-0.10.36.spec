Summary:	GStreamer is a streaming media framework
Name:		gstreamer
Version:	0.10.36
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/gstreamer/0.10
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
sed -i  -e '/YYLEX_PARAM/d'                                       \
        -e '/parse-param.*scanner/i %lex-param { void *scanner }' \
            gst/parse/grammar.y
./configure \
	CFLAGS="%{optflags}"    \
	CXXFLAGS="%{optflags}"  \
	--prefix=%{_prefix}     \
	--libexecdir=%{_libdir} \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/gstreamer-0.10/design
install -v -m644 docs/design/*.txt \
                    %{buildroot}/usr/share/doc/gstreamer-0.10/design

if [ -d /usr/share/doc/gstreamer-0.10/faq/html ]; then
    chown -v -R root:root \
        /usr/share/doc/gstreamer-0.10/*/html
fi

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
