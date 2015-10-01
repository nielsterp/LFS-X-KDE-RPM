Summary:	VLC is a media player, streamer, and encoder.
Name:		vlc
Version:	2.1.5
Release:	1
License:	GPL
URL:		http://download.videolan.org/vlc/2.1.5/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
sed -i 's:libsmbclient.h:samba-4.0/&:' modules/access/smb.c 
./bootstrap 

sed "s:< 56:< 57:g" -i configure 
./configure --prefix=%{_prefix}      

sed -i 's/luaL_optint/(int)&eger/'         modules/lua/libs/{net,osd,volume}.c             
sed -i 's/luaL_checkint(/(int)luaL_checkinteger(/' \
       modules/lua/{demux,libs/{configuration,net,osd,playlist,stream,variables,volume}}.c 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make docdir=/usr/share/doc/vlc-2.1.5 DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post
gtk-update-icon-cache 
update-desktop-database
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
