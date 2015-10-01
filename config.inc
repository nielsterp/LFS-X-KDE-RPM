#	Editable variables follow
LFS=/mnt/lfs			# where to build LFS
BLFS=/mnt/blfs			# where to build BLFS
PARENT="/usr/src/Octothorpe"	# where build system lives
MKFLAGS="-j 4"	# how many processors on this host
#	Edit partition and mnt_point for the correct values.
#	Failing to do so will cause you grief as in overwriting your host system.
#	You have been warned!
DEVICE=sda3			#	device to create filesystem for LFS build
SWAP=sda1			#	device for SWAP filesystem
FILESYSTEM=ext4			#	filesystem type
LOGFILE="install.log"		#	this is where we log the build to 
USER=lfs			#	build user account
export FILESYSTEM
export SWAP
export DEVICE