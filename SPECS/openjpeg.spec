Summary:	OpenJPEG is an open-source implementation of the JPEG-2000 standard.
Name:		openjpeg
Version:	1.5.2
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/openjpeg.mirror/openjpeg-1.5.2.tar.gz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
autoreconf -f -i 
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
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
