Summary:	Terminal emulator for the X Window System.
Name:		xterm
Version:	314
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tgz
%description

%prep
%setup -q

%build
sed -i '/v0/,+1s/new:/new:kb=^?:/' termcap
echo -e '\tkbs=\\177,' >>terminfo

TERMINFO=/usr/share/terminfo \
./configure \
	CFLAGS="%{optflags}"              \
	CXXFLAGS="%{optflags}"            \
	--prefix=%{_prefix}               \
	--sysconfdir=%{_sysconfdir}       \
	--localstatedir=%{_localstatedir} \
	--disable-static \
        --with-app-defaults=/etc/X11/app-defaults
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-ti
rm -rf %{buildroot}/usr/share/terminfo/v/vs100
rm -rf %{buildroot}/usr/share/terminfo/x/xterm
rm -rf %{buildroot}/usr/share/terminfo/x/xterm+pcc0
rm -rf %{buildroot}/usr/share/terminfo/x/xterm+pcc2
rm -rf %{buildroot}/usr/share/terminfo/x/xterm+pce0
rm -rf %{buildroot}/usr/share/terminfo/x/xterm+pce2
rm -rf %{buildroot}/usr/share/terminfo/x/xterm+pcfkeys
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-16color
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-24
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-256color
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-88color
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-8bit
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-basic
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-bold
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-color
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-hp
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-new
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-noapp
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-old
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-r5
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-r6
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-sco
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-sun
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-vt220
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-vt52
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-xf86-v44
rm -rf %{buildroot}/usr/share/terminfo/x/xterm-xfree86
rm -rf %{buildroot}/usr/share/terminfo/x/xterms

%{_fixperms} %{buildroot}/*

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
