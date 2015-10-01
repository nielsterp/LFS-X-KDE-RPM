Summary:	A fast, versatile and command-line based audio/video everything to everything converter.
Name:		transcode
Version:	1.1.7
Release:	1
License:	GPL
URL:		https://bitbucket.org/france/transcode-tcforge/downloads/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
sed -i "s:#include <freetype/ftglyph.h>:#include FT_GLYPH_H:" filter/subtitler/load_font.c

sed -i 's|doc/transcode|&-$(PACKAGE_VERSION)|' \
       $(find . -name Makefile.in -exec grep -l 'docsdir =' {} \;) 

sed -i "s:av_close_input_file:avformat_close_input:g" \
       import/probe_ffmpeg.c

patch -Np1 -i ../../SOURCES/transcode-1.1.7-ffmpeg2-1.patch

./configure --prefix=%{_prefix} \
            --enable-alsa \
            --enable-libmpeg2 \
            --enable-freetype2
make
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
