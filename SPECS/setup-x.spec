Summary:	Setup environment for X
Name:		setup-x
Version:	20150626
Release:	1
License:	GPL
URL:		http://www.linuxfromscratch.org
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe

%description

%prep

%build


%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

install -vdm 755 %{buildroot}/etc/profile.d

cat > %{buildroot}/etc/profile.d/xorg.sh << "EOF"
XORG_PREFIX="/usr"
XORG_CONFIG="--prefix=$XORG_PREFIX --sysconfdir=/etc --localstatedir=/var --disable-static"
QT4LINK=/usr

as_root()
{
  if   [ $EUID = 0 ];        then $*
  elif [ -x /usr/bin/sudo ]; then sudo $*
  else                            su -c \\"$*\\"
  fi
}

export -f as_root

export XORG_PREFIX XORG_CONFIG QT4LINK
EOF
chmod 644 /etc/profile.d/xorg.sh

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
