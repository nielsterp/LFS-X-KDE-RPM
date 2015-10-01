Summary:	Contains a library for creating MusicBrainz DiscIDs from audio CDs.
Name:		libdiscid
Version:	0.6.1
Release:	1
License:	GPL
URL:		http://ftp.musicbrainz.org/pub/musicbrainz/libdiscid/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
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
%{_includedir}/*
%{_libdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
