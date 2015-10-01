Summary:	Web rendering engine WebKit to the GTK+ 2 platform
Name:		webkitgtk
Version:	2.4.8
Release:	1
License:	GPL
URL:		http://webkitgtk.org/releases
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz


%description

%prep
%setup -q
ulimit -s 32768
%build
# First build against GTK+ 3

mkdir -vp build-3           &&
cp -a Documentation build-3 &&
cd build-3                  &&

../configure --prefix=%{_prefix} \
	     --enable-introspection &&
make
cd ..

# Now build against GTK+ 2

mkdir -vp build-1
cp -a Documentation build-1
cd build-1 &&


../configure --prefix=%{_prefix} \
	     --with-gtk=2.0      \
	     --disable-webkit2 &&
make
cd ..

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
ulimit -s 32768

# Install build against GTK+ 3

cd build-3
make DESTDIR=%{buildroot} install
cd ..

# Install build against GTK+ 2

cd build-1
make DESTDIR=%{buildroot} install
cd ..

%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%{_includedir}/*
%{_libdir}/*
%{_libexecdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
