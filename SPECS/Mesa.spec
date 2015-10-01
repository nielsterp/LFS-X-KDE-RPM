Summary:	OpenGL compatible 3D graphics library.
Name:		Mesa
Version:	10.4.5
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}Lib-%{version}.tar.bz2

%description

%prep
%setup -q
# patch -Np1 -i ../../SOURCES/MesaLib-10.4.5-add_xdemos-1.patch

%build

autoreconf -f -i
./configure CFLAGS="-O2" CXXFLAGS="-O2"    \
            --prefix=%{_prefix}            \
            --sysconfdir=%{_sysconfdir}    \
            --enable-texture-float         \
            --enable-gles1                 \
            --enable-gles2                 \
            --enable-osmesa                \
            --enable-xa                    \
            --enable-gbm                   \
            --enable-glx-tls               \
            --with-egl-platforms="drm,x11" \
            --with-gallium-drivers="nouveau,r300,r600,radeonsi,svga,swrast"

make	
# make -C xdemos DEMOS_PREFIX=/usr

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*

make DESTDIR=%{buildroot} install
# make -C xdemos DEMOS_PREFIX=/usr DESTDIR=%{buildroot} install

%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_includedir}/*
%{_libdir}/*
# %_datadir/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
