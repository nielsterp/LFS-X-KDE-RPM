Summary:	The Parted package is a disk partitioning and partition resizing tool.
Name:		parted
Version:	3.2
Release:	1
License:	GPL
URL:		http://ftp.gnu.org/gnu/parted/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --disable-static 
make 

make -C doc html                                       
makeinfo --html      -o doc/html       doc/parted.texi 
makeinfo --plaintext -o doc/parted.txt doc/parted.texi

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/parted-3.2/html &&
install -v -m644    doc/html/* \
                    %{buildroot}/usr/share/doc/parted-3.2/html &&
install -v -m644    doc/{FAT,API,parted.{txt,html}} \
                    %{buildroot}/usr/share/doc/parted-3.2
%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
