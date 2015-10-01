Summary:	C comiler cache
Name:		ccache
Version:	3.2.1
Release:	1
License:	GPL
URL:		https://ccache.samba.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--disable-static
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%post
mv /usr/bin/ccache /usr/bin/ccache-tmp
mkdir /usr/bin/ccache
mv /usr/bin/ccache-tmp /usr/bin/ccache/ccache
cd /usr/bin/ccache
ln -s ccache gcc
ln -s ccache cc
ln -s ccache c++
ln -s ccache g++
ln -s ccache i686-pc-linux-gnu-c++
ln -s ccache i686-pc-linux-gnu-g++
ln -s ccache i686-pc-linux-gnu-gcc


%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*


%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version