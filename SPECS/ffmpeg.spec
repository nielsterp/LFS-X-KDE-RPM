Summary:	FFmpeg is a solution to record, convert and stream audio and video
Name:		ffmpeg
Version:	2.5.4
Release:	1
License:	GPL
URL:		http://ffmpeg.org/releases
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
sed -i 's/-lflite"/-lflite -lasound"/' configure 
./configure --prefix=%{_prefix} \
            --enable-gpl        \
            --enable-version3   \
            --enable-nonfree    \
            --disable-static    \
            --enable-shared     \
            --disable-debug     \
            --enable-libass     \
            --enable-libfdk-aac \
            --enable-libmp3lame \
            --enable-libtheora  \
            --enable-libvorbis  \
            --enable-libvpx     \
            --enable-libx264    \
            --enable-x11grab    \
            --docdir=%{_docdir}/ffmpeg-2.5.4 
make 
gcc tools/qt-faststart.c -o tools/qt-faststart

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755    tools/qt-faststart %{buildroot}%{_bindir}
install -v -m644    doc/*.txt %{buildroot}%{_docdir}/ffmpeg-2.5.4
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
