Summary:	S-Lang is an interpreted language that may be embedded into an application to make the application extensible
Name:		slang
Version:	2.2.4
Release:	1
License:	GPL
URL:		ftp://space.mit.edu/pub/davis/slang/v2.2
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} 
make 
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make install_doc_dir=/usr/share/doc/slang-2.2.4   \
     SLSH_DOC_DIR=/usr/share/doc/slang-2.2.4/slsh \
     DESTDIR=%{buildroot} install-all 


%{_fixperms} %{buildroot}/*

%post
chmod -v 755 /usr/lib/libslang.so.2.2.4 /usr/lib/slang/v2/modules/*.so
ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
