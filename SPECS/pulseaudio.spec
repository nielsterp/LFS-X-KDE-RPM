Summary:	Sound system for POSIX OSes
Name:		pulseaudio
Version:	5.0
Release:	1
License:	GPL
URL:		http://freedesktop.org/software/pulseaudio/releases
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q

%build
find . -name "Makefile.in" | xargs sed -i "s|(libdir)/@PACKAGE@|(libdir)/pulse|" &&
./configure --prefix=%{_prefix}               \
            --sysconfdir=%{_sysconfdir}       \
            --localstatedir=%{_localstatedir} \
            --disable-bluez4                  \
            --disable-rpath                   \
            --without-caps 	              \
            --with-module-dir=%{_libdir}/pulse/modules &&
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%pre
egrep -i "^pulse" /etc/group
if [ $? -eq 0 ]; then
   echo "User $USERID exists in /etc/passwd"
else
    groupadd -g 58 pulse &&
    groupadd -g 59 pulse-access &&
    useradd -c "Pulseaudio User" -d /var/run/pulse -g pulse \
        -s /bin/false -u 58 pulse &&
    usermod -a -G audio pulse
fi


%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_lib}/*
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
