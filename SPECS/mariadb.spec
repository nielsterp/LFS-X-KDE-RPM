Summary:	MariaDB is a community-developed fork and a drop-in replacement for MySQL
Name:		mariadb 
Version:	10.0.16
Release:	1
License:	GPL
URL:		http://anduin.linuxfromscratch.org/sources/BLFS/7.7/m/mariadb-10.0.16.tar.gz
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
Source1:	blfs-bootscripts-20150304.tar.bz2

%description

%prep
%setup -q
tar xf %{SOURCE1}

%build
sed -i "s@data/test@\${INSTALL_MYSQLTESTDIR}@g"        sql/CMakeLists.txt       
sed -i "s/srv_buf_size/srv_sort_buf_size/"      storage/innobase/row/row0log.cc 

mkdir build 
cd build    

cmake -DCMAKE_BUILD_TYPE=Release                       \
      -DCMAKE_INSTALL_PREFIX=%{_prefix}                \
      -DINSTALL_DOCDIR=share/doc/mariadb-10.0.16       \
      -DINSTALL_DOCREADMEDIR=share/doc/mariadb-10.0.16 \
      -DINSTALL_MANDIR=share/man                       \
      -DINSTALL_MYSQLSHAREDIR=share/mysql              \
      -DINSTALL_MYSQLTESTDIR=share/mysql/test          \
      -DINSTALL_PLUGINDIR=lib/mysql/plugin             \
      -DINSTALL_SBINDIR=sbin                           \
      -DINSTALL_SCRIPTDIR=bin                          \
      -DINSTALL_SQLBENCHDIR=share/mysql/bench          \
      -DINSTALL_SUPPORTFILESDIR=share/mysql            \
      -DMYSQL_DATADIR=/srv/mysql                       \
      -DMYSQL_UNIX_ADDR=/run/mysqld/mysqld.sock        \
      -DWITH_EXTRA_CHARSETS=complex                    \
      -DWITH_EMBEDDED_SERVER=ON                        \
      -DTOKUDB_OK=0                                    \
      .. 
make
cd ..
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd build
make DESTDIR=%{buildroot} install

install -v -dm 755 %{buildroot}/etc/mysql
install -v -dm 755 %{buildroot}/run/mysqld

cat > %{buildroot}/etc/mysql/my.cnf << "EOF"
# Begin /etc/mysql/my.cnf

# The following options will be passed to all MySQL clients
[client]
#password       = your_password
port            = 3306
socket          = /run/mysqld/mysqld.sock

# The MySQL server
[mysqld]
port            = 3306
socket          = /run/mysqld/mysqld.sock
datadir         = /srv/mysql
skip-external-locking
key_buffer_size = 16M
max_allowed_packet = 1M
sort_buffer_size = 512K
net_buffer_length = 16K
myisam_sort_buffer_size = 8M

# Don't listen on a TCP/IP port at all.
skip-networking

# required unique id between 1 and 2^32 - 1
server-id       = 1

# Uncomment the following if you are using BDB tables
#bdb_cache_size = 4M
#bdb_max_lock = 10000

# Uncomment the following if you are using InnoDB tables
innodb_data_home_dir = /srv/mysqli nnodb_data_file_path = ibdata1:10M:autoextend
innodb_log_group_home_dir = /srv/mysql
# You can set .._buffer_pool_size up to 50 - 80 %
# of RAM but beware of setting memory usage too high
innodb_buffer_pool_size = 16M
innodb_additional_mem_pool_size = 2M
Set .._log_file_size to 25 % of buffer pool size
innodb_log_file_size = 5M
innodb_log_buffer_size = 8M
innodb_flush_log_at_trx_commit = 1
innodb_lock_wait_timeout = 50

[mysqldump]
quick
max_allowed_packet = 16M

[mysql]
no-auto-rehash
# Remove the next comment character if you are not familiar with SQL
#safe-updates

[isamchk]
key_buffer = 20M
sort_buffer_size = 20M
read_buffer = 2M
write_buffer = 2M

[myisamchk]
key_buffer_size = 20M
sort_buffer_size = 20M
read_buffer = 2M
write_buffer = 2M

[mysqlhotcopy]
interactive-timeout

# End /etc/mysql/my.cnf
EOF

pushd ../blfs-bootscripts-20150304
make DESTDIR=%{buildroot} install-mysql
popd

%{_fixperms} %{buildroot}/*

%check

%pre

egrep -i "^mysql" /etc/group
if [ $? -eq 0 ]; then
   echo "User $USERID exists in /etc/passwd"
else
groupadd -g 40 mysql 
useradd -c "MySQL Server" -d /srv/mysql -g mysql -s /bin/false -u 40 mysql
fi

%post

mysql_install_db --basedir=/usr --datadir=/srv/mysql --user=mysql
chown -R mysql:mysql /srv/mysql

install -v -m755 -o mysql -g mysql -d /var/run/mysqld &&
mysqld_safe --user=mysql 2>&1 >/dev/null &

mysqladmin -u root password 333jytte4444

mysqladmin -p shutdown


%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/mysql/*
%{_sysconfdir}/rc.d/*
%{_bindir}/*
%{_sbindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version