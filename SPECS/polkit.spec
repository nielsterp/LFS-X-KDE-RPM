Summary:	Toolkit for defining and handling authorizations
Name:		polkit
Version:	0.112
Release:	1
License:	GPL
URL:		http://www.freedesktop.org/software/polkit/releases
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir} \
	--with-authfw=shadow \
	--disable-static  \
	--disable-man-pages \
	--libexecdir=%{_libdir}/polkit-1
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%pre
egrep -i "^polkitd" /etc/group
if [ $? -eq 0 ]; then
   echo "User $USERID exists in /etc/passwd"
else
groupadd -fg 27 polkitd &&
useradd -c "PolicyKit Daemon Owner" -d /etc/polkit-1 -u 27 \
        -g polkitd -s /bin/false polkitd
fi


%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
