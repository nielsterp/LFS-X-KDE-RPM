Summary:	Access control list utilities, libraries and headers
Name:		acl
Version:	2.2.52
Release:	1
License:	LGPL
URL:		http://savannah.nongnu.org/projects/acl
Group:		BLFS/Security
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://download.savannah.gnu.org/releases/acl/%{name}-%{version}.src.tar.gz
Provides:	libacl.so.1 = %{version}
Provides:	libacl.so.1(ACL_1.0) = %{version}
%description
The acl package contains utilities to administer Access Control Lists
which are used to define more fine-grained discretionary access 
rights for files and directories.
%prep
%setup -q 
sed -i -e 's|/@pkg_name@|&-@pkg_version@|' include/builddefs.in
%build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
INSTALL_USER=root  \
INSTALL_GROUP=root \
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir}
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DIST_ROOT=%{buildroot} install install-lib install-dev
find %{buildroot}/ -name '*.a' -delete
find %{buildroot}/ -name '*.la' -delete
%find_lang %{name}
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}/*
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_includedir}/*
%{_docdir}/%{name}-%{version}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version