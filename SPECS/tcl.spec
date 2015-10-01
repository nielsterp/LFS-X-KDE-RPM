Summary:	The Tcl package contains the Tool Command Language, a robust general-purpose scripting language.
Name:		tcl
Version:	8.6.3
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/tcl/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}%{version}-src.tar.gz
Source1:	%{name}%{version}-html.tar.gz		
%description

%prep
%setup -q -n tcl8.6.3
tar xf %{SOURCE1} --strip-components=1

%build
export SRCDIR=`pwd` 

cd unix 

./configure --prefix=%{_prefix}     \
            --without-tzdata        \
            --mandir=%{_mandir}     \
            $([ $(uname -m) = x86_64 ] && echo --enable-64bit) 
make 

sed -e "s#$SRCDIR/unix#/usr/lib#" \
    -e "s#$SRCDIR#/usr/include#"  \
    -i tclConfig.sh               

sed -e "s#$SRCDIR/unix/pkgs/tdbc1.0.2#/usr/lib/tdbc1.0.2#" \
    -e "s#$SRCDIR/pkgs/tdbc1.0.2/generic#/usr/include#"    \
    -e "s#$SRCDIR/pkgs/tdbc1.0.2/library#/usr/lib/tcl8.6#" \
    -e "s#$SRCDIR/pkgs/tdbc1.0.2#/usr/include#"            \
    -i pkgs/tdbc1.0.2/tdbcConfig.sh                        

sed -e "s#$SRCDIR/unix/pkgs/itcl4.0.2#/usr/lib/itcl4.0.2#" \
    -e "s#$SRCDIR/pkgs/itcl4.0.2/generic#/usr/include#"    \
    -e "s#$SRCDIR/pkgs/itcl4.0.2#/usr/include#"            \
    -i pkgs/itcl4.0.2/itclConfig.sh                        

unset SRCDIR	

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-private-headers 
ln -v -sf tclsh8.6 /usr/bin/tclsh 
chmod -v 755 /usr/lib/libtcl8.6.so
mkdir -v -p /usr/share/doc/tcl-8.6.3 
cp -v -r  ../html/* /usr/share/doc/tcl-8.6.3

%{_fixperms} %{buildroot}/*

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)

%changelog
*	Sat Nov 16 2013 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version