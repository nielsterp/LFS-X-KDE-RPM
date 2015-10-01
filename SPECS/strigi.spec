Summary:	Strigi is a program for fast indexing and searching of personal data.
Name:		strigi
Version:	0.7.8
Release:	1
License:	GPL
URL:		http://www.vandenoever.info/software/strigi/strigi-0.7.8.tar.bz2
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
sed -i "s/BufferedStream :/STREAMS_EXPORT &/" libstreams/include/strigi/bufferedstream.h 

mkdir build 
cd    build 

cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_INSTALL_LIBDIR=lib        \
      -DCMAKE_BUILD_TYPE=Release        \
      -DENABLE_CLUCENE=OFF              \
      -DENABLE_CLUCENE_NG=OFF           \
      .. 
make
cd ..

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd build
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
