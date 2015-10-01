Summary:	The Pnmixer package provides a lightweight volume control with a tray icon.
Name:		pnmixer
Version:	0.5.1
Release:	1
License:	GPL
URL:		https://github.com/downloads/nicklan/pnmixer/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
./autogen.sh --prefix=%{_prefix}
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
