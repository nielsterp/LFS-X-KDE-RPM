Summary:	Web rendering engine WebKit to the GTK+ 2 platform
Name:		webkitgtk
Version:	2.6.5
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
sed -i 's/â€/\"/g' Source/WebCore/xml/XMLViewer.{css,js} 

mkdir -vp build 
cd build        

cmake -DCMAKE_BUILD_TYPE=Release        \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_SKIP_RPATH=ON             \
      -DPORT=GTK                        \
      -DLIB_INSTALL_DIR=%{_libdir}      \
      -Wno-dev .. 
make
cd ..	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
ulimit -s 32768
cd build
make DESTDIR=%{buildroot} install
install -vdm755 %{buildroot}/usr/share/gtk-doc/html/webkit{2,dom}gtk-4.0 &&
install -vm644  ../Documentation/webkit2gtk/html/* \
                %{buildroot}/usr/share/gtk-doc/html/webkit2gtk-4.0 &&
install -vm644  ../Documentation/webkitdomgtk/html/* \
                %{buildroot}/usr/share/gtk-doc/html/webkitdomgtk-4.0
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
