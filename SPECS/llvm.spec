Summary:	Low Level Virtual Machine.
Name:		llvm
Version:	3.5.1.src
Release:	1
License:	GPL
URL:		http://llvm.org/releases/3.3/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.xz
Source1:	http://llvm.org/releases/3.5/cfe-3.5.1.src.tar.xz
Source2:	http://llvm.org/releases/3.5/compiler-rt-3.5.1.src.tar.xz

%description
The LLVM package contains a collection of modular and reusable compiler
and toolchain technologies. The Low Level Virtual Machine (LLVM) Core
libraries provide a modern source and target-independent optimizer,
along with code generation support for many popular CPUs (as well as
some less common ones!). These libraries are built around a well
specified code representation known as the LLVM intermediate
representation ("LLVM IR").

The optional Clang and Compiler RT packages provide a new C, C++,
Objective C and Objective C++ front-ends and runtime libraries for the
LLVM.

%prep
%setup -q
tar -xf ../../SOURCES/cfe-3.5.1.src.tar.xz -C tools &&
tar -xf ../../SOURCES/compiler-rt-3.5.1.src.tar.xz -C projects
mv tools/cfe-3.5.1.src tools/clang
mv projects/compiler-rt-3.5.1.src projects/compiler-rt

%build
sed -e "s:/docs/llvm:/share/doc/llvm-3.5.1:" -i Makefile.config.in
CC=gcc 
CXX=g++
./configure --prefix=%{_prefix}          \
            --sysconfdir=%{_sysconfdir}  \
            --enable-libffi              \
            --enable-optimized           \
            --enable-shared              \
            --enable-targets=all         \
            --disable-assertions         \
            --disable-debug-runtime      \
            --disable-expensive-checks   \
            --enable-experimental-targets=R600
make	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -dm755 %{buildroot}/usr/lib/clang-analyzer
for prog in scan-build scan-view
do
  cp -rfv tools/clang/tools/$prog %{buildroot}/usr/lib/clang-analyzer/
  ln -sfv ../lib/clang-analyzer/$prog/$prog %{buildroot}/usr/bin/
done 
ln -sfv /usr/bin/clang %{buildroot}/usr/lib/clang-analyzer/scan-build/
mv -v %{buildroot}/usr/lib/clang-analyzer/scan-build/scan-build.1 %{buildroot}/usr/share/man/man1/
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
