Summary:	Perl Compatible Regular Expression libraries
Name:		pcre
Version:	8.36
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/pcre
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description
The PCRE package contains Perl Compatible Regular Expression libraries.
These are useful for implementing regular expression pattern matching
using the same syntax and semantics as Perl 5.

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"              \
	CXXFLAGS="%{optflags}"            \
	--prefix=%{_prefix}               \
	--disable-static                  \
        --docdir=%{_docdir}/pcre-8.36     \
        --enable-unicode-properties       \
        --enable-pcre16                   \
        --enable-pcre32                   \
        --enable-pcregrep-libz            \
        --enable-pcregrep-libbz2          \
        --enable-pcretest-libreadline
make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install

%post
mv -v /usr/lib/libpcre.so.* /lib &&
ln -sfv ../../lib/$(readlink /usr/lib/libpcre.so) /usr/lib/libpcre.so

%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_docdir}/*
%{_mandir}/*


%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
