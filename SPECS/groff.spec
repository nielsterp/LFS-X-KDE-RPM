Summary:	Programs for processing and formatting text
Name:		groff
Version:	1.22.3
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/groff
Group:		Applications/Text
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
%description
The Groff package contains programs for processing
and formatting text.
%prep
%setup -q
%build
PAGE=A4 ./configure --prefix=%{_prefix} 
make
%install
install -vdm 755 %{_defaultdocdir}/%{name}-1.22/pdf
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_infodir}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_datarootdir}/%{name}/*
%{_mandir}/*/*
%changelog
*	Sun Mar 29 2015 Niels Terp <nielsterp@comhem.se> 1.22.3
-	Upgrade version
