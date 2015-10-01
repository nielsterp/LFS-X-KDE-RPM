Summary:	Daemon that maps devices to color profiles
Name:		colord
Version:	1.2.9
Release:	1
License:	GPL
URL:		http://www.freedesktop.org/software/colord/releases
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix}                \
            --sysconfdir=%{_sysconfdir}        \
            --localstatedir=%{_localstatedir}  \
            --with-daemon-user=colord          \
            --enable-vala                      \
            --enable-systemd-login=no          \
            --disable-argyllcms-sensor         \
            --disable-bash-completion          \
            --disable-static                   \
            --with-systemdsystemunitdir=no 
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%pre
egrep -i "^colord" /etc/group
if [ $? -eq 0 ]; then
   echo "User $USERID exists in /etc/passwd"
else
  groupadd -g 71 colord &&
  useradd -c "Color Daemon Owner" -d /var/lib/colord -u 71 \
        -g colord -s /bin/false colord
fi


%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_lib}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*
%{_libexecdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
