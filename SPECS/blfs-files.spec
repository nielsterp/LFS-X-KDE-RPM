Summary:	Setting up basic files for BLFS
Name:		blfs-files
Version:	20130905
Release:	1
License:	GPLv3
Group:		System Environment/Base
Vendor:		Bildanet
URL:		http://www.linuxfromscratch.org
Distribution:	Octothorpe
BuildArch: 	noarch
Source0:	http://www.linuxfromscratch.org/blfs/downloads/svn/blfs-bootscripts-20150304.tar.bz2
Source1:	http://sourceforge.net/projects/lsb/files/lsb_release/1.4/lsb-release-1.4.tar.gz

%description
The blfs-files package is implementing the files from BLFS chapter II - 3, setting up 
a basic /etc/skel directory and utility scripts.
%prep
tar xf %{SOURCE0}
tar xf %{SOURCE1}
%build

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
install -vdm 755 %{buildroot}/etc/skel
install -vdm 755 %{buildroot}/etc/profile.d
install -vdm 755 %{buildroot}/usr/sbin
install -vdm 755 %{buildroot}/usr/bin
install -vdm 755 %{buildroot}/root
install -vdm 755 %{buildroot}/usr/share/man/man1
install -vdm 755 %{buildroot}/etc/init.d

cat >> %{buildroot}/etc/profile << "EOF"
# Begin /etc/profile
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>
# modifications by Dagmar d'Surreal <rivyqntzne@pbzpnfg.arg>

# System wide environment variables and startup programs.

# System wide aliases and functions should go in /etc/bashrc.  Personal
# environment variables and startup programs should go into
# ~/.bash_profile.  Personal aliases and functions should go into
# ~/.bashrc.

# Function to allow normal users to execute MAKE INSTALL as root. Uses SUDO, so
# users should be given permission to use SUDO without a password.
as_root()
{
  if   [ $EUID = 0 ];        then $*
  elif [ -x /usr/bin/sudo ]; then sudo $*
  else                            su -c \\"$*\\"
  fi
}

export -f as_root

# Functions to help us manage paths.  Second argument is the name of the
# path variable to be modified (default: PATH)
pathremove () {
        local IFS=':'
        local NEWPATH
        local DIR
        local PATHVARIABLE=${2:-PATH}
        for DIR in ${!PATHVARIABLE} ; do
                if [ "$DIR" != "$1" ] ; then
                  NEWPATH=${NEWPATH:+$NEWPATH:}$DIR
                fi
        done
        export $PATHVARIABLE="$NEWPATH"
}

pathprepend () {
        pathremove $1 $2
        local PATHVARIABLE=${2:-PATH}
        export $PATHVARIABLE="$1${!PATHVARIABLE:+:${!PATHVARIABLE}}"
}

pathappend () {
        pathremove $1 $2
        local PATHVARIABLE=${2:-PATH}
        export $PATHVARIABLE="${!PATHVARIABLE:+${!PATHVARIABLE}:}$1"
}

export -f pathremove pathprepend pathappend

# Set the initial path
export PATH=/bin:/usr/bin

if [ $EUID -eq 0 ] ; then
        pathappend /sbin:/usr/sbin
        unset HISTFILE
fi

# Setup some environment variables.
export HISTSIZE=1000
export HISTIGNORE="&:[bf]g:exit"

# Set some defaults for graphical systems
export XDG_DATA_DIRS=/usr/share/
export XDG_CONFIG_DIRS=/etc/xdg/
export XORG_PREFIX="/usr"
export XORG_CONFIG="--prefix=$XORG_PREFIX --sysconfdir=/etc --localstatedir=/var --disable-static"
export QT4LINK=/usr
export KDE_PREFIX=/usr

# Setup a red prompt for root and a green one for users.
NORMAL="\[\e[0m\]"
RED="\[\e[1;31m\]"
GREEN="\[\e[1;32m\]"
if [[ $EUID == 0 ]] ; then
  PS1="$RED\u [ $NORMAL\w$RED ]# $NORMAL"
else
  PS1="$GREEN\u [ $NORMAL\w$GREEN ]\$ $NORMAL"
fi

for script in /etc/profile.d/*.sh ; do
        if [ -r $script ] ; then
                . $script
        fi
done

unset script RED GREEN NORMAL

# End /etc/profile
EOF

install --directory --mode=0755 --owner=root --group=root /etc/profile.d

cat > %{buildroot}/etc/profile.d/dircolors.sh << "EOF"
# Setup for /bin/ls and /bin/grep to support color, the alias is in /etc/bashrc.
if [ -f "/etc/dircolors" ] ; then
        eval $(dircolors -b /etc/dircolors)
fi

if [ -f "$HOME/.dircolors" ] ; then
        eval $(dircolors -b $HOME/.dircolors)
fi

alias ls='ls --color=auto'
alias grep='grep --color=auto'
EOF

cat > %{buildroot}/etc/profile.d/extrapaths.sh << "EOF"
if [ -d /usr/local/lib/pkgconfig ] ; then
        pathappend /usr/local/lib/pkgconfig PKG_CONFIG_PATH
fi
if [ -d /usr/local/bin ]; then
        pathprepend /usr/local/bin
fi
if [ -d /usr/local/sbin -a $EUID -eq 0 ]; then
        pathprepend /usr/local/sbin
fi

# Set some defaults before other applications add to these paths.
pathappend /usr/share/man  MANPATH
pathappend /usr/share/info INFOPATH
EOF

cat > %{buildroot}/etc/profile.d/readline.sh << "EOF"
# Setup the INPUTRC environment variable.
if [ -z "$INPUTRC" -a ! -f "$HOME/.inputrc" ] ; then
        INPUTRC=/etc/inputrc
fi
export INPUTRC
EOF

cat > %{buildroot}/etc/profile.d/umask.sh << "EOF"
# By default, the umask should be set.
if [ "$(id -gn)" = "$(id -un)" -a $EUID -gt 99 ] ; then
  umask 002
else
  umask 022
fi
EOF

cat > %{buildroot}/etc/profile.d/i18n.sh << "EOF"
# Set up i18n variables
export LANG=da_DK.ISO_8859-1
EOF

cat > %{buildroot}/etc/bashrc << "EOF"
# Begin /etc/bashrc
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>
# updated by Bruce Dubbs <bdubbs@linuxfromscratch.org>

# System wide aliases and functions.

# System wide environment variables and startup programs should go into
# /etc/profile.  Personal environment variables and startup programs
# should go into ~/.bash_profile.  Personal aliases and functions should
# go into ~/.bashrc

# Provides colored /bin/ls and /bin/grep commands.  Used in conjunction
# with code in /etc/profile.

alias ls='ls --color=auto'
alias grep='grep --color=auto'

# Provides prompt for non-login shells, specifically shells started
# in the X environment. [Review the LFS archive thread titled
# PS1 Environment Variable for a great case study behind this script
# addendum.]

NORMAL="\[\e[0m\]"
RED="\[\e[1;31m\]"
GREEN="\[\e[1;32m\]"
if [[ $EUID == 0 ]] ; then
  PS1="$RED\u [ $NORMAL\w$RED ]# $NORMAL"
else
  PS1="$GREEN\u [ $NORMAL\w$GREEN ]\$ $NORMAL"
fi

unset RED GREEN NORMAL

# End /etc/bashrc
EOF

cat > %{buildroot}/etc/skel/.bash_profile << "EOF"
# Begin ~/.bash_profile
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>
# updated by Bruce Dubbs <bdubbs@linuxfromscratch.org>

# Personal environment variables and startup programs.

# Personal aliases and functions should go in ~/.bashrc.  System wide
# environment variables and startup programs are in /etc/profile.
# System wide aliases and functions are in /etc/bashrc.

if [ -f "$HOME/.bashrc" ] ; then
  source $HOME/.bashrc
fi

if [ -d "$HOME/bin" ] ; then
  pathprepend $HOME/bin
fi

# Having . in the PATH is dangerous
#if [ $EUID -gt 99 ]; then
#  pathappend .
#fi

# End ~/.bash_profile
EOF

cat > %{buildroot}/root/.bash_profile << "EOF"
# Begin ~/.bash_profile
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>
# updated by Bruce Dubbs <bdubbs@linuxfromscratch.org>

# Personal environment variables and startup programs.

# Personal aliases and functions should go in ~/.bashrc.  System wide
# environment variables and startup programs are in /etc/profile.
# System wide aliases and functions are in /etc/bashrc.

if [ -f "$HOME/.bashrc" ] ; then
  source $HOME/.bashrc
fi

if [ -d "$HOME/bin" ] ; then
  pathprepend $HOME/bin
fi

# Having . in the PATH is dangerous
#if [ $EUID -gt 99 ]; then
#  pathappend .
#fi

# End ~/.bash_profile
EOF

cat > %{buildroot}/etc/skel/.bashrc << "EOF"
# Begin ~/.bashrc
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>

# Personal aliases and functions.

# Personal environment variables and startup programs should go in
# ~/.bash_profile.  System wide environment variables and startup
# programs are in /etc/profile.  System wide aliases and functions are
# in /etc/bashrc.

if [ -f "/etc/bashrc" ] ; then
  source /etc/bashrc
fi

/usr/bin/ccache/ccache -M 2G


# End /etc/skel/.bashrc

# End ~/.bashrc
EOF



cat > %{buildroot}/root/.bashrc << "EOF"
# Begin ~/.bashrc
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>

# Personal aliases and functions.

# Personal environment variables and startup programs should go in
# ~/.bash_profile.  System wide environment variables and startup
# programs are in /etc/profile.  System wide aliases and functions are
# in /etc/bashrc.

if [ -f "/etc/bashrc" ] ; then
  source /etc/bashrc
fi

/usr/bin/ccache/ccache -M 2G


# End /etc/skel/.bashrc

# End ~/.bashrc
EOF

cat > %{buildroot}/etc/skel/.bash_logout << "EOF"
# Begin ~/.bash_logout
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>

# Personal items to perform on logout.

# End ~/.bash_logout
EOF

cat > %{buildroot}/root/.bash_logout << "EOF"
# Begin ~/.bash_logout
# Written for Beyond Linux From Scratch
# by James Robertson <jameswrobertson@earthlink.net>

# Personal items to perform on logout.

# End ~/.bash_logout
EOF

dircolors -p > %{buildroot}/etc/dircolors

cat > %{buildroot}/etc/skel/.vimrc << "EOF"
" Begin .vimrc

set columns=80
set wrapmargin=8
set ruler

" End .vimrc
EOF

cat > %{buildroot}/root/.vimrc << "EOF"
" Begin .vimrc

set columns=80
set wrapmargin=8
set ruler

" End .vimrc
EOF

export LANG=da_DK.ISO-8859-1

cat > %{buildroot}/etc/shells << "EOF"
# Begin /etc/shells

/bin/sh
/bin/bash

# End /etc/shells
EOF

cat > %{buildroot}/root/.xinitrc << EOF
# Begin .xinitrc

exec ck-launch-session dbus-launch --exit-with-session startkde

# End .xinitrc
EOF

cat > %{buildroot}/etc/skel/.xinitrc << EOF
# Begin .xinitrc

exec ck-launch-session dbus-launch --exit-with-session startkde

# End .xinitrc
EOF


pushd blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-random
popd


%files
%defattr(-,root,root)
%dir /etc/skel
%dir /etc/profile.d
%config(noreplace) /etc/profile
%config(noreplace) /etc/shells
%config(noreplace) /etc/skel/.xinitrc
%config(noreplace) /etc/profile.d/dircolors.sh
%config(noreplace) /etc/profile.d/extrapaths.sh
%config(noreplace) /etc/profile.d/readline.sh
%config(noreplace) /etc/profile.d/umask.sh
%config(noreplace) /etc/profile.d/i18n.sh
%config(noreplace) /etc/bashrc
%config(noreplace) /etc/skel/.bash_profile
%config(noreplace) /root/.bash_profile
%config(noreplace) /root/.xinitrc
%config(noreplace) /etc/skel/.bashrc
%config(noreplace) /root/.bashrc
%config(noreplace) /etc/skel/.bash_logout
%config(noreplace) /root/.bash_logout
%config(noreplace) /etc/dircolors
%config(noreplace) /etc/skel/.vimrc
%config(noreplace) /root/.vimrc
%config(noreplace) /etc/rc.d/init.d/random
%config(noreplace) /etc/rc.d/rc0.d/K45random
%config(noreplace) /etc/rc.d/rc1.d/S25random
%config(noreplace) /etc/rc.d/rc2.d/S25random
%config(noreplace) /etc/rc.d/rc3.d/S25random
%config(noreplace) /etc/rc.d/rc4.d/S25random
%config(noreplace) /etc/rc.d/rc5.d/S25random
%config(noreplace) /etc/rc.d/rc6.d/K45random

%clean
rm -rf %{buildroot}

%post

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version