Summary:	AAlib is a library to render any graphic into ASCII Art.
Name:		aalib
Version:	1.4.0
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/aa-project/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-1.4rc5.tar.gz

%description

%prep
%setup -q	

%build
sed -i -e '/AM_PATH_AALIB,/s/AM_PATH_AALIB/[&]/' aalib.m4
./configure --prefix=%{_prefix}        \
            --infodir=%{_datadir}/info \
            --mandir=%{_mandir}        \
            --disable-static          
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

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
