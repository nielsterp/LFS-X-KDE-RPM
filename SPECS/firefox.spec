Summary:	Firefox is a stand-alone browser based on the Mozilla codebase.
Name:		firefox
Version:	36.0
Release:	1
License:	GPL
URL:		https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/36.0/source/firefox-36.0.source.tar.bz2
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.source.tar.bz2

%description

%prep
%setup -q -n mozilla-release

%build
cat > mozconfig << "EOF"
# If you have a multicore machine, all cores will be used by default.
# If desired, you can reduce the number of cores used, e.g. to 1, by
# uncommenting the next line and setting a valid number of CPU cores.
#mk_add_options MOZ_MAKE_FLAGS="-j1"

# If you have installed DBus-Glib comment out this line:
# ac_add_options --disable-dbus

# If you have installed dbus-glib, and you have installed (or will install)
# wireless-tools, and you wish to use geolocation web services, comment out
# this line
# ac_add_options --disable-necko-wifi

# If you have installed libnotify comment out this line:
# ac_add_options --disable-libnotify

# GStreamer is necessary for H.264 video playback in HTML5 Video Player;
# to be enabled, also remember to set "media.gstreamer.enabled" to "true"
# in about:config. If you have GStreamer 0.x.y, comment out this line:
# ac_add_options --disable-gstreamer
# or uncomment this line, if you have GStreamer 1.x.y
ac_add_options --enable-gstreamer=1.0

# Uncomment these lines if you have installed optional dependencies:
# ac_add_options --enable-system-hunspell
ac_add_options --enable-startup-notification

# Comment out following option if you have PulseAudio installed
# ac_add_options --disable-pulseaudio

# Comment out following options if you have not installed
# recommended dependencies:
ac_add_options --enable-system-sqlite
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-icu

# The BLFS editors recommend not changing anything below this line:
ac_add_options --prefix=/usr
ac_add_options --enable-application=browser

ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests

ac_add_options --enable-optimize
ac_add_options --enable-strip
ac_add_options --enable-install-strip

ac_add_options --enable-gio
ac_add_options --enable-official-branding
ac_add_options --enable-safe-browsing
ac_add_options --enable-url-classifier

ac_add_options --enable-system-cairo
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

ac_add_options --with-pthreads

ac_add_options --with-system-bz2
ac_add_options --with-system-jpeg
ac_add_options --with-system-png
ac_add_options --with-system-zlib

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/firefox-build-dir
EOF

make -f client.mk
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make  -f client.mk DESTDIR=%{buildroot} install INSTALL_SDK= 

chown -R 0:0 %{buildroot}%{_libdir}/firefox-36.0  
mkdir -pv %{buildroot}%{_libdir}/mozilla/plugins  

mkdir -pv %{buildroot}%{_datadir}/applications 
mkdir -pv %{buildroot}%{_datadir}/pixmaps 

cat > %{buildroot}%{_datadir}/applications/firefox.desktop << "EOF" 
[Desktop Entry]
Encoding=UTF-8
Name=Firefox Web Browser
Comment=Browse the World Wide Web
GenericName=Web Browser
Exec=firefox %u
Terminal=false
Type=Application
Icon=firefox
Categories=GNOME;GTK;Network;WebBrowser;
MimeType=application/xhtml+xml;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;x-scheme-handler/http;x-scheme-handler/https;
StartupNotify=true
EOF


%{_fixperms} %{buildroot}/*

%check

%post
ln -sfv ../../mozilla/plugins /usr/lib/firefox-36.0/browser

ln -sfv /usr/lib/firefox-36.0/browser/icons/mozicon128.png \
        /usr/share/pixmaps/firefox.png

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Sun Jun 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version