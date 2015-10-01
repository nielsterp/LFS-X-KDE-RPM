Summary:	Setup locales
Name:		setlocales
Version:	1.0
Release:	1
License:	GPL
URL:		none
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	none
%description

%prep

%post
	/sbin/locale-gen.sh
	/sbin/ldconfig
	/usr/sbin/pwconv
	/usr/sbin/grpconv

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
