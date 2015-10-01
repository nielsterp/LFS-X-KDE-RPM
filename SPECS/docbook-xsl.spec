Summary:	The DocBook XSL Stylesheets package contains XSL stylesheets
Name:		docbook-xsl
Version:	1.78.1
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/docbook
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q
tar -xf ../../SOURCES/docbook-xsl-doc-1.78.1.tar.bz2 --strip-components=1
%build

	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/
install -v -m755 -d %{buildroot}/usr/share/xml/docbook/xsl-stylesheets-1.78.1

cp -v -R VERSION common eclipse epub extensions fo highlighting html \
         htmlhelp images javahelp lib manpages params profiling \
         roundtrip slides template tests tools webhelp website \
         xhtml xhtml-1_1 \
    %{buildroot}/usr/share/xml/docbook/xsl-stylesheets-1.78.1

ln -s VERSION %{buildroot}/usr/share/xml/docbook/xsl-stylesheets-1.78.1/VERSION.xsl

install -v -m644 -D README \
                    %{buildroot}/usr/share/doc/docbook-xsl-1.78.1/README.txt
install -v -m644    RELEASE-NOTES* NEWS* \
                    %{buildroot}/usr/share/doc/docbook-xsl-1.78.1
# cp -v -R %{buildroot}docbook-xsl-1.78.1-1.x86_64/usr/share/doc/* %{buildroot}/usr/share/doc/docbook-xsl-1.78.1


%{_fixperms} %{buildroot}/*

%post
 
if [ ! -d /etc/xml ]; then install -v -m755 -d /etc/xml; fi &&
if [ ! -f /etc/xml/catalog ]; then
    xmlcatalog --noout --create /etc/xml/catalog
fi &&

xmlcatalog --noout --add "rewriteSystem" \
           "http://docbook.sourceforge.net/release/xsl/1.78.1" \
           "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" \
    /etc/xml/catalog &&

xmlcatalog --noout --add "rewriteURI" \
           "http://docbook.sourceforge.net/release/xsl/1.78.1" \
           "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" \
    /etc/xml/catalog &&

xmlcatalog --noout --add "rewriteSystem" \
           "http://docbook.sourceforge.net/release/xsl/current" \
           "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" \
    /etc/xml/catalog &&

xmlcatalog --noout --add "rewriteURI" \
           "http://docbook.sourceforge.net/release/xsl/current" \
           "/usr/share/xml/docbook/xsl-stylesheets-1.78.1" \
    /etc/xml/catalog


%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_docdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
