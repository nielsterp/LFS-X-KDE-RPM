Summary:	Application framework
Name:		qt
Version:	4.8.6
Release:	1
License:	GPL
URL:		http://download.qt-project.org/official_releases/qt/4.8/4.8.6/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-everywhere-opensource-src-%{version}.tar.gz
%description

%prep
%setup -q -n qt-everywhere-opensource-src-4.8.6

%build
sed -i -e '631a if (image->isNull()) { state = Error; return -1; }' \
    src/gui/image/qgifhandler.cpp

export QT4LINK=/usr

sed -i -e "/#if/d" -e "/#error/d" -e "/#endif/d" \
     config.tests/unix/libmng/libmng.cpp

sed -i '/CONFIG -/ a\isEmpty(OUTPUT_DIR): OUTPUT_DIR = ../..' \
     src/3rdparty/webkit/Source/WebKit2/DerivedSources.pro

./configure -prefix         %{_prefix}                   \
            -bindir         %{_bindir}                   \
            -plugindir      %{_libdir}/qt4/plugins       \
            -importdir      %{_libdir}/qt4/imports       \
            -headerdir      %{_includedir}/qt4           \
            -datadir        %{_datadir}/qt4              \
            -sysconfdir     %{_sysconfdir}/xdg           \
            -docdir         %{_docdir}/qt4               \
            -demosdir       %{_docdir}/qt4/demos         \
            -examplesdir    %{_docdir}/qt4/examples       \
            -translationdir %{_datadir}/qt4/translations \
            -confirm-license   				 \
            -opensource       				 \
            -release        			   	 \
            -dbus-linked       				 \
            -openssl-linked   				 \
            -system-sqlite    				 \
            -no-phonon        				 \
            -no-phonon-backend				 \
            -no-nis           				 \
            -no-openvg        				 \
            -nomake demos     				 \
            -nomake examples  				 \
            -optimized-qmake   
make

find . -name "*.pc" -exec perl -pi -e "s, -L$PWD/?\S+,,g" {} \;

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make INSTALL_ROOT="%{buildroot}" install

rm -rf %{buildroot}/usr/tests

# Remove references to the build directory from installed files

for file in 3Support CLucene Core DBus Declarative DesignerComponents \
            Designer Gui Help Multimedia Network OpenGL Script \
            ScriptTools Sql Svg Test UiTools WebKit XmlPatterns Xml phonon; do

     [ -e %{buildroot}/usr/lib/libQt${file}.prl ] &&
     sed -r '/^QMAKE_PRL_BUILD_DIR/d;s/(QMAKE_PRL_LIBS =).*/\1/' \
         -i %{buildroot}/usr/lib/libQt${file}.prl
done
unset file

# Install images and create menu entries.

install -v -Dm644 src/gui/dialogs/images/qtlogo-64.png \
                  %{buildroot}/usr/share/pixmaps/qt4logo.png

install -v -Dm644 tools/assistant/tools/assistant/images/assistant-128.png \
                  %{buildroot}/usr/share/pixmaps/assistant-qt4.png

install -v -Dm644 tools/designer/src/designer/images/designer.png \
                  %{buildroot}/usr/share/pixmaps/designer-qt4.png

install -v -Dm644 tools/linguist/linguist/images/icons/linguist-128-32.png \
                  %{buildroot}/usr/share/pixmaps/linguist-qt4.png

install -v -Dm644 tools/qdbus/qdbusviewer/images/qdbusviewer-128.png \
                  %{buildroot}/usr/share/pixmaps/qdbusviewer-qt4.png

install -dm755 %{buildroot}/usr/share/applications

cat > %{buildroot}/usr/share/applications/assistant-qt4.desktop << EOF
[Desktop Entry]
Name=Qt4 Assistant 
Comment=Shows Qt4 documentation and examples
Exec=/opt/qt4/bin/assistant
Icon=assistant-qt4.png
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Development;Documentation;
EOF

cat > %{buildroot}/usr/share/applications/designer-qt4.desktop << EOF
[Desktop Entry]
Name=Qt4 Designer
Comment=Design GUIs for Qt4 applications
Exec=/opt/qt4/bin/designer
Icon=designer-qt4.png
MimeType=application/x-designer;
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Development;
EOF

cat > %{buildroot}/usr/share/applications/linguist-qt4.desktop << EOF
[Desktop Entry]
Name=Qt4 Linguist 
Comment=Add translations to Qt4 applications
Exec=/opt/qt4/bin/linguist
Icon=linguist-qt4.png
MimeType=text/vnd.trolltech.linguist;application/x-linguist;
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Development;
EOF

cat > %{buildroot}/usr/share/applications/qdbusviewer-qt4.desktop << EOF
[Desktop Entry]
Name=Qt4 QDbusViewer 
GenericName=D-Bus Debugger
Comment=Debug D-Bus applications
Exec=/opt/qt4/bin/qdbusviewer
Icon=qdbusviewer-qt4.png
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Development;Debugger;
EOF

cat > %{buildroot}/usr/share/applications/qtconfig-qt4.desktop << EOF
[Desktop Entry]
Name=Qt4 Config 
Comment=Configure Qt4 behavior, styles, fonts
Exec=/opt/qt4/bin/qtconfig
Icon=qt4logo.png
Terminal=false
Encoding=UTF-8
Type=Application
Categories=Qt;Settings;
EOF

# Configuration

install -vdm 755 %{buildroot}/etc/profile.d
cat > /etc/profile.d/qt4.sh << EOF
# Begin /etc/profile.d/qt4.sh

QT4DIR=/usr
export QT4DIR

# End /etc/profile.d/qt4.sh
EOF

%pre


%post

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
