Summary:	CD audio extraction tool.
Name:		cdparanoia-III
Version:	10.2
Release:	1
License:	GPL
URL:		http://downloads.xiph.org/releases/cdparanoia/-10.2.src.tgz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.src.tgz

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/cdparanoia-III-10.2-gcc_fixes-1.patch
./configure --prefix=%{_prefix} \
	    --mandir=%{_mandir}
make -j1

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%check

%post
chmod -v 755 /usr/lib/libcdda_*.so.0.10.2
/sbin/ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version