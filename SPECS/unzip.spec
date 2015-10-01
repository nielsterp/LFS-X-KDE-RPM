Summary:	The UnZip package contains ZIP extraction utilities
Name:		unzip
Version:	60
Release:	1
License:	GPL
URL:		http://downloads.sourceforge.net/infozip
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}%{version}.tar.gz
%description

%prep
%setup -q -n unzip60

%build

case `uname -m` in
  i?86)
    sed -i -e 's/DASM"/DASM -DNO_LCHMOD"/' unix/Makefile
    make -f unix/Makefile linux
    ;;
  *)
    sed -i -e 's/CFLAGS="-O -Wall/& -DNO_LCHMOD/' unix/Makefile
    make -f unix/Makefile linux_noasm
    ;;
esac

# make %{?_smp_mflags}
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} prefix=%{buildroot}/usr install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
/usr/man/man1/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
