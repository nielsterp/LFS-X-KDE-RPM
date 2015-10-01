Summary:	This package contains a library which allows you to access the data held on the MusicBrainz server.
Name:		libmusicbrainz
Version:	2.1.5
Release:	1
License:	GPL
URL:		http://ftp.musicbrainz.org/pub/musicbrainz/historical/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
patch -Np1 -i ../../SOURCES/libmusicbrainz-2.1.5-missing-includes-1.patch
./configure --prefix=%{_prefix}
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install
install -v -m644 -D docs/mb_howto.txt %{buildroot}/usr/share/doc/libmusicbrainz-2.1.5/mb_howto.txt

%{_fixperms} %{buildroot}/*

%check

%post

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
