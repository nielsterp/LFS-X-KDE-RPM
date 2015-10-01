Summary:	Allows users to run commands as another user
Name:		sudo
Version:	1.8.12
Release:	1
License:	GPLv2
URL:		http://www.sudo.ws
Group:		BLFS/Security
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.sudo.ws/sudo/dist/%{name}-%{version}.tar.gz

%description
The Sudo package allows a system administrator to give certain users (or
groups of users) the ability to run some (or all) commands as root or
another user while logging the commands and arguments.

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libexec=%{_libexecdir} \
        --docdir=%{_docdir} \
        --with-all-insults \
        --with-env-editor  

make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%find_lang %{name}
%{_fixperms} %{buildroot}/*
%check

%post

%clean
rm -rf %{buildroot}/*

%files -f %{name}.lang
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libexecdir}/*
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 1.8.12-1
*	Wed May 29 2013 baho-utot <baho-utot@columbus.rr.com> 1.8.2.3-1
-	Initial build.	First version
