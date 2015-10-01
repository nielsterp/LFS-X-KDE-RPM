Summary:	Simple DirectMedia Layer
Name:		SDL
Version:	1.2.15
Release:	1
License:	GPL
URL:		http://www.libsdl.org
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
%description

%prep
%setup -q

%build
sed -i '/_XData32/s:register long:register _Xconst long:' src/video/x11/SDL_x11sym.h
./configure --prefix=%{_prefix} \
	    --disable-static
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}/usr/share/doc/SDL-1.2.15/html
install -v -m644    docs/html/*.html \
                    %{buildroot}/usr/share/doc/SDL-1.2.15/html
                    
%{_fixperms} %{buildroot}/*

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
