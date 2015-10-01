Summary:	Fast distributed version control system
Name:		git
Version:	2.3.0
Release:	1
License:	GPLv2
URL:		http://git-scm.com/
Group:		BLFS/Programming
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://git-core.googlecode.com/files/%{name}-%{version}.tar.xz

%description
Git is a free and open source, distributed version control system 
designed to handle everything from small to very large projects with
speed and efficiency. Every Git clone is a full-fledged repository 
with complete history and full revision tracking capabilities, not 
dependent on network access or a central server. Branching and 
merging are fast and easy to do. Git is used for version control of
files, much like tools such as Mercurial, Bazaar, 
Subversion-1.7.8, CVS-1.11.23, Perforce, and Team Foundation Server.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--libexec=%{_libexecdir} \
	--with-gitconfig=/etc/gitconfig
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%find_lang %{name}
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post
git config --system http.sslCAPath /etc/ssl/certs
exit 0
%clean
rm -rf %{buildroot}/*
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/perl5/*
# %{_libdir}/python2.7/site-packages/*
%{_libexecdir}/*
%{_mandir}/man3/*
%{_datarootdir}/git-core/*
%{_datarootdir}/git-gui/*
%{_datarootdir}/gitk/*
%{_datarootdir}/gitweb/*
%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se> 2.3.0
*	Thu Oct 31 2013 nielsterp <nielsterp@comhem.se> 1.8.4-1
-	Updated to ver. 1.8.4
*	Wed May 29 2013 baho-utot <baho-utot@columbus.rr.com> 1.8.2.3-1
-	Initial build.	First version
