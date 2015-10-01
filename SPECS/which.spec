Summary:	Utility to find executable
Name:		which
Version:	2.20
Release:	1
License:	GPLv3
URL:		http://www.gnu.org
Group:		BLFS/System-Utilities
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz
%description
GNU which - is a utility that is used to find which executable 
(or alias or shell function) is executed when entered on the 
shell prompt.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir}
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/which.1.gz
%changelog
*	Sun May 19 2013 baho-utot <baho-utot@columbus.rr.com> 2.20-1
-	Initial build.	First version
