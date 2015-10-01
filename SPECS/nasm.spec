Summary:	NASM (Netwide Assembler) is an 80x86 assembler designed for portability and modularity
Name:		nasm
Version:	2.11.06
Release:	1
License:	GPL
URL:		http://www.nasm.us/pub/nasm/releasebuilds/2.10.09
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
%description

%prep
%setup -q
tar -xf ../../SOURCES/nasm-2.11.06-xdoc.tar.xz --strip-components=1
%build
./configure --prefix=%{_prefix}
make
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make prefix=%{buildroot}/usr install 
install -m755 -d	 %{buildroot}/usr/share/info/
install -m755 -d         %{buildroot}/usr/share/doc/nasm-2.10.09/html  &&
cp -v doc/html/*.html    %{buildroot}/usr/share/doc/nasm-2.10.09/html  &&
cp -v doc/*.{txt,ps,pdf} %{buildroot}/usr/share/doc/nasm-2.10.09       &&
cp -v doc/info/*         %{buildroot}/usr/share/info                   &&
install-info %{buildroot}/usr/share/info/nasm.info %{buildroot}/usr/share/info/dir
%{_fixperms} %{buildroot}/*

%post



%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
