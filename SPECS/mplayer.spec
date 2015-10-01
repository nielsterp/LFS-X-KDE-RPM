Summary:	MPlayer is a powerful audio/video player
Name:		mplayer
Version:	20150220
Release:	1
License:	GPL
URL:		http://anduin.linuxfromscratch.org/sources/other/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-2015-02-20.tar.xz

%description

%prep
%setup -q -n mplayer-2015-02-20

%build
sed -i 's:libsmbclient.h:samba-4.0/&:' configure stream/stream_smb.c

./configure --prefix=%{_prefix}      \
            --confdir=/etc/mplayer   \
            --enable-dynamic-plugins \
            --enable-menu            \
            --enable-gui            
make
make doc

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/mplayer-2015-02-20 
install -v -m644    DOCS/HTML/en/* \
                    %{buildroot}/usr/share/doc/mplayer-2015-02-20   
install -v -m644 etc/*.conf %{buildroot}/etc/mplayer  

tar -xvf  ../../SOURCES/Clearlooks-1.6.tar.bz2 -C  %{buildroot}/usr/share/mplayer/skins

%{_fixperms} %{buildroot}/*

%check

%post
gtk-update-icon-cache 
update-desktop-database
ln -svf /usr/share/icons/hicolor/48x48/apps/mplayer.png /usr/share/pixmaps/mplayer.png

ln  -sfvn Clearlooks /usr/share/mplayer/skins/default

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
