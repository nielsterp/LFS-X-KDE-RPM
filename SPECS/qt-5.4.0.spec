Summary:	Qt is a cross-platform application framework
Name:		qt
Version:	5.4.0
Release:	1
License:	GPL
URL:		http://download.qt-project.org/official_releases/qt/5.1/5.1.1/single
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-everywhere-opensource-src-%{version}.tar.xz
%description

%prep
%setup -q -n qt-everywhere-opensource-src-5.4.0

%build
export QT5DIR=/opt/qt-5.4.0 &&
export QT5LINK=/opt/qt5 &&

./configure -prefix  /opt/qt-5.4.0         \
            -sysconfdir %{_sysconfdir}/xdg \
            -confirm-license               \
            -opensource                    \
            -dbus-linked                   \
            -openssl-linked                \
            -system-sqlite                 \
            -no-nis                        \
            -nomake examples               \
            -skip qtwebengine              \
            -optimized-qmake 
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make INSTALL_ROOT="%{buildroot}"	install
ln -svfn /opt/qt-5.4.0 /opt/qt5

find /opt/qt-5.4.0 -name qt_lib_bootstrap_private.pri \
   -exec sed -i -e "s:$PWD/qtbase:/%{buildroot}/opt/qt-5.4.0/lib/:g" {} \; &&

find /opt/qt-5.4.0 -name \*.prl \
   -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d' {} \;


install -v -dm755 %{buildroot}/usr/share/pixmaps/                  

install -v -Dm644 qttools/src/assistant/assistant/images/assistant-128.png \
                  %{buildroot}/usr/share/pixmaps/assistant-qt5.png 

install -v -Dm644 qttools/src/designer/src/designer/images/designer.png \
                  %{buildroot}/usr/share/pixmaps/designer-qt5.png  

install -v -Dm644 qttools/src/linguist/linguist/images/icons/linguist-128-32.png \
                  %{buildroot}/usr/share/pixmaps/linguist-qt5.png  

install -v -Dm644 qttools/src/qdbus/qdbusviewer/images/qdbusviewer-128.png \
                  %{buildroot}/usr/share/pixmaps/qdbusviewer-qt5.png 

install -dm755 %{buildroot}/usr/share/applications 

cat > %{buildroot}/usr/share/applications/assistant-qt5.desktop << EOF
[Desktop Entry]
Name=Qt5 Assistant 
Comment=Shows Qt5 documentation and examples
Exec=$QT5LINK/bin/assistant
Icon=assistant-qt5.png
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Development;Documentation;
EOF

cat > %{buildroot}/usr/share/applications/designer-qt5.desktop << EOF
[Desktop Entry]
Name=Qt5 Designer
GenericName=Interface Designer
Comment=Design GUIs for Qt5 applications
Exec=$QT5LINK/bin/designer
Icon=designer-qt5.png
MimeType=application/x-designer;
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Development;
EOF

cat > %{buildroot}/usr/share/applications/linguist-qt5.desktop << EOF
[Desktop Entry]
Name=Qt5 Linguist
Comment=Add translations to Qt5 applications
Exec=$QT5LINK/bin/linguist
Icon=linguist-qt5.png
MimeType=text/vnd.trolltech.linguist;application/x-linguist;
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Development;
EOF

cat > %{buildroot}/usr/share/applications/qdbusviewer-qt5.desktop << EOF
[Desktop Entry]
Name=Qt5 QDbusViewer 
GenericName=D-Bus Debugger
Comment=Debug D-Bus applications
Exec=$QT5LINK/bin/qdbusviewer
Icon=qdbusviewer-qt5.png
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Development;Debugger;
EOF

install -vdm 755 %{buildroot}/etc/profile.d

cat > %{buildroot}/etc/profile.d/qt5.sh << EOF
# Begin /etc/profile.d/qt5.sh

QT5DIR=/opt/qt5

pathappend /opt/qt5/bin           PATH
pathappend /opt/qt5/lib/pkgconfig PKG_CONFIG_PATH

export QT5DIR

# End /etc/profile.d/qt5.sh
EOF     
%{_fixperms} %{buildroot}/*

%post
cat >> /etc/ld.so.conf << EOF
# Begin Qt addition

/opt/qt5/lib

# End Qt addition
EOF

ldconfig
%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
/opt/qt-5.4.0/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
