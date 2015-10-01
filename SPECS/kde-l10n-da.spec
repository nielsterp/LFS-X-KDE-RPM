Summary:	Danish language for KDE
Name:		kde-l10n-da
Version:	14.12.2
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/applications/14.12.2/src/kde-l10n/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
#mkdir build 
#cd    build 

#cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX \
#      -DCMAKE_BUILD_TYPE=Release         \
#      -Wno-dev .. 
#make
#cd ..

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
#cd build
#make DESTDIR=%{buildroot} install

install -vdm 755 %{buildroot}/etc/skel
cat > %{buildroot}/etc/skel/.xinitrc << EOF
# Begin .xinitrc

exec ck-launch-session dbus-launch --exit-with-session startkde

# End .xinitrc
EOF

%{_fixperms} %{buildroot}/*

%check

%post
cat >> /etc/inittab << EOF
kd:5:respawn:/usr/bin/kdm
EOF

sed -i 's#id:3:initdefault:#id:5:initdefault:#' /etc/inittab

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
/etc/skel/.*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version