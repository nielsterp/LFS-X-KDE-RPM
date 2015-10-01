Summary:	Math libraries
Name:		gperf
Version:	3.0.4
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/gperf
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.gnu.org/software/gperf/%{name}-%{version}.tar.gz

%description
Gperf generates a perfect hash function from a key set. 

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --docdir=%{_docdir}/doc/gperf-3.0.4
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post	-p /sbin/ldconfig

%postun	-p /sbin/ldconfig

%files
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version