Summary:	Qca aims to provide a straightforward and cross-platform crypto API
Name:		qca
Version:	2.1.0
Release:	1
License:	GPL
URL:		http://delta.affinix.com/download/qca/2.0/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz

%description

%prep
%setup -q

%build
mkdir build &&
cd    build &&

cmake -DCMAKE_INSTALL_PREFIX=$QT4DIR            \
      -DCMAKE_BUILD_TYPE=Release                \
      -DQT4_BUILD=ON                            \
      -DQCA_MAN_INSTALL_DIR:PATH=/usr/share/man \
      ..                                        &&

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
/usr/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
