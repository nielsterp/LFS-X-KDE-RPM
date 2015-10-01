Summary:	The DocBook XML DTD-4.5 package contains document type definitions
Name:		docbook-xml
Version:	4.5
Release:	1
License:	GPL
URL:		http://www.docbook.org/xml/4.5
Group:		Documentation/Other
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.zip
%description

%prep
# %setup -q
install -v -d -m755 /usr/src/Octothorpe/BUILD/docbook-xml-4.5
cd /usr/src/Octothorpe/BUILD/docbook-xml-4.5
cp /usr/src/Octothorpe/SOURCES/docbook-xml-4.5.zip .
unzip docbook-xml-4.5

%build
chown -R root:root . 

%install
#[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
install -v -d -m755 %{buildroot}/usr/share/xml/docbook/xml-dtd-4.5 
install -v -d -m755 %{buildroot}/usr/share/xml/docbook/xml-dtd-4.5/ent
install -v -d -m755 %{buildroot}/etc/xml


cp /usr/src/Octothorpe/BUILD/docbook-xml-4.5/docbook.cat %{buildroot}/usr/share/xml/docbook/xml-dtd-4.5
cp /usr/src/Octothorpe/BUILD/docbook-xml-4.5/*dtd %{buildroot}/usr/share/xml/docbook/xml-dtd-4.5
cp /usr/src/Octothorpe/BUILD/docbook-xml-4.5/ent/* %{buildroot}/usr/share/xml/docbook/xml-dtd-4.5/ent
cp /usr/src/Octothorpe/BUILD/docbook-xml-4.5/*mod %{buildroot}/usr/share/xml/docbook/xml-dtd-4.5

if [ ! -e %{buildroot}/etc/xml/docbook ]; then
    xmlcatalog --noout --create %{buildroot}/etc/xml/docbook
fi &&
xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML V4.5//EN" \
    "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML CALS Table Model V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/calstblx.dtd" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/soextblx.dtd" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Information Pool V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbpoolx.mod" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbhierx.mod" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML HTML Tables V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/htmltblx.mod" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Notations V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbnotnx.mod" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Character Entities V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbcentx.mod" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbgenent.mod" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/4.5" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
    %{buildroot}/etc/xml/docbook &&
xmlcatalog --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/4.5" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
    %{buildroot}/etc/xml/docbook
    
if [ ! -e %{buildroot}/etc/xml/catalog ]; then
    xmlcatalog --noout --create %{buildroot}/etc/xml/catalog
fi &&
xmlcatalog --noout --add "delegatePublic" \
    "-//OASIS//ENTITIES DocBook XML" \
    "file:///etc/xml/docbook" \
    %{buildroot}/etc/xml/catalog &&
xmlcatalog --noout --add "delegatePublic" \
    "-//OASIS//DTD DocBook XML" \
    "file:///etc/xml/docbook" \
    %{buildroot}/etc/xml/catalog &&
xmlcatalog --noout --add "delegateSystem" \
    "http://www.oasis-open.org/docbook/" \
    "file:///etc/xml/docbook" \
    %{buildroot}/etc/xml/catalog &&
xmlcatalog --noout --add "delegateURI" \
    "http://www.oasis-open.org/docbook/" \
    "file:///etc/xml/docbook" \
    %{buildroot}/etc/xml/catalog
    
for DTDVERSION in 4.1.2 4.2 4.3 4.4
do
  xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML V$DTDVERSION//EN" \
    "http://www.oasis-open.org/docbook/xml/$DTDVERSION/docbookx.dtd" \
    %{buildroot}/etc/xml/docbook
  xmlcatalog --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/$DTDVERSION" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
    %{buildroot}/etc/xml/docbook
  xmlcatalog --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/$DTDVERSION" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
    %{buildroot}/etc/xml/docbook
  xmlcatalog --noout --add "delegateSystem" \
    "http://www.oasis-open.org/docbook/xml/$DTDVERSION/" \
    "file:///etc/xml/docbook" \
    %{buildroot}/etc/xml/catalog
  xmlcatalog --noout --add "delegateURI" \
    "http://www.oasis-open.org/docbook/xml/$DTDVERSION/" \
    "file:///etc/xml/docbook" \
    %{buildroot}/etc/xml/catalog
done
%{_fixperms} %{buildroot}/*

%check

%post


 
%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_datadir}/*
%{_sysconfdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
