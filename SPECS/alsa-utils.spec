Summary:	The ALSA Utilities package contains various utilities which are useful for controlling your sound card
Name:		alsa-utils
Version:	1.0.28
Release:	1
License:	GPL
URL:		http://alsa.cybermirror.org/utils
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
Source1:	blfs-bootscripts-20150304.tar.bz2
%description

%prep
%setup -q
tar xf %{SOURCE1}

%build
./configure --disable-alsaconf 
make	

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make  DESTDIR=%{buildroot} udevrulesdir=/lib/udev/rules.d install
pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-alsa
popd
touch %{buildroot}/var/lib/alsa/asound.state

%{_fixperms} %{buildroot}/*

%post
alsactl -L store
usermod -a -G audio niels
usermod -a -G audio lfs

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_lib}/udev/rules.d/90-alsa-restore.rules
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/*
%{_sysconfdir}/rc.d/*
%{_sharedstatedir}/*


%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
