Summary:	libdvdread is a library which provides a simple foundation for reading DVDs.
Name:		libdvdread
Version:	5.0.2
Release:	1
License:	GPL
URL:		http://download.videolan.org/videolan/libdvdread/5.0.2/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
            --disable-static    \
            --docdir=%{_docdir}/libdvdread-5.0.2 
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
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
