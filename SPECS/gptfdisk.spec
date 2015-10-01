Summary:	A set of programs for creation and maintenance of GUID Partition Table (GPT) disk drives.
Name:		gptfdisk
Version:	0.8.10
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/project/gptfdisk/gptfdisk/0.8.10/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/gptfdisk-0.8.10-convenience-1.patch &&
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
/sbin/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
