Summary:	Contains libraries used for creating graphical user interfaces for applications
Name:		gtk+
Version:	2.24.26
Release:	1
License:	GPL
URL:		http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q	-n gtk+-2.24.26

%build
sed -i 's#l \(gtk-.*\).sgml#& -o \1#' docs/{faq,tutorial}/Makefile.in 
sed -i -e 's#pltcheck.sh#$(NULL)#g' gtk/Makefile.in                   
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir}                          
make	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%post
gtk-query-immodules-2.0 --update-cache


cat > ~/.gtkrc-2.0 << "EOF"
include "/usr/share/themes/Glider/gtk-2.0/gtkrc"
gtk-icon-theme-name = "hicolor"
EOF

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
