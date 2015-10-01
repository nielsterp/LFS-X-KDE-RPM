Summary:	The ALSA Tools package contains advanced tools for certain sound cards.
Name:		alsa-tools
Version:	1.0.28
Release:	1
License:	GPL
URL:		http://alsa.cybermirror.org/tools/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2

%description

%prep
%setup -q

%build
rm -rf qlo10k1 Makefile gitcompile
for tool in *
do
  case $tool in
    seq )
      tool_dir=seq/sbiload
    ;;
    * )
      tool_dir=$tool
    ;;
  esac

  pushd $tool_dir
    ./configure --prefix=%{_prefix}
    make
  popd

done
unset tool tool_dir

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*


for tool in *
do
  case $tool in
    seq )
      tool_dir=seq/sbiload
    ;;
    * )
      tool_dir=$tool
    ;;
  esac

  pushd $tool_dir
    make DESTDIR=%{buildroot} install
  popd

done
unset tool tool_dir

%{_fixperms} %{buildroot}/*

%check

%post
/sbin/ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version