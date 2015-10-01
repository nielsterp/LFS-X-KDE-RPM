Summary:	The Wireless Extension (WE) is a generic API in the Linux kernel
Name:		wireless_tools
Version:	29
Release:	1
License:	GPL
URL:		http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}.%{version}.tar.gz
%description

%prep
%setup -q -n wireless_tools.29

%build

make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make \
        INSTALL_DIR="%{buildroot}%{_bindir}"     \
        INSTALL_LIB="%{buildroot}%{_libdir}"     \
        INSTALL_INC="%{buildroot}%{_includedir}" \
        INSTALL_MAN="%{buildroot}%{_mandir}"     \
        install
%{_fixperms} %{buildroot}/*

%post        -p /sbin/ldconfig
%postun      -p /sbin/ldconfig


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
