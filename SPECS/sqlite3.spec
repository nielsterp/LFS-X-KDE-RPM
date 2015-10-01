Summary:	Transactional SQL database engine
Name:		sqlite3
Version:	3080802
Release:	1
License:	GPL
URL:		http://sqlite.org/2013
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	sqlite-autoconf-%{version}.tar.gz
%description

%prep
%setup -q	-n sqlite-autoconf-3080802

%build
./configure --prefix=%{_prefix} \
	    --disable-static        \
            CFLAGS="-g -O2 -DSQLITE_ENABLE_FTS3=1 \
            -DSQLITE_ENABLE_COLUMN_METADATA=1     \
            -DSQLITE_ENABLE_UNLOCK_NOTIFY=1       \
            -DSQLITE_SECURE_DELETE=1" &&
make

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
