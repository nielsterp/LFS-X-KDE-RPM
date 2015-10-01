Summary:	Contains components that are central to providing the KDE desktop environment.
Name:		kde-workspace
Version:	4.11.16
Release:	1
License:	GPL
URL:		http://download.kde.org/stable/applications/14.12.2/src/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
mkdir build &&
cd    build &&

cmake -DCMAKE_INSTALL_PREFIX=$KDE_PREFIX           \
      -DSYSCONF_INSTALL_DIR=/etc                   \
      -DCMAKE_BUILD_TYPE=Release                   \
      -DINSTALL_PYTHON_FILES_IN_PYTHON_PREFIX=TRUE \
      -Wno-dev .. &&
make
cd ..

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd build
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/usr/share/xsessions &&


%{_fixperms} %{buildroot}/*

%check

%post
if ! getent group kdm >/dev/null; then
	groupadd -g 37 kdm
	useradd -c "KDM Daemon Owner" -d /var/lib/kdm -g kdm \
        -u 37 -s /bin/false kdm &&
	install -o kdm -g kdm -dm755 /var/lib/kdm
fi
ln -sf /$KDE_PREFIX/share/apps/kdm/sessions/kde-plasma.desktop \
       /usr/share/xsessions/kde-plasma.desktop
       
%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
