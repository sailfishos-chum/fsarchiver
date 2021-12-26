Name:		fsarchiver
Version:	0.8.6
Release:	1%{?dist}
Summary:	Safe and flexible file-system backup/deployment tool

Group:		Applications/Archiving
License:	GPLv2
URL:		http://www.fsarchiver.org
Source0:  	https://github.com/fdupoux/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	e2fsprogs-devel => 1.41.4
BuildRequires:	libuuid-devel
BuildRequires:	libblkid-devel
BuildRequires:	e2fsprogs
BuildRequires:	libattr-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	lzo-devel
#BuildRequires:	lz4-devel
BuildRequires:	xz-devel
#BuildRequires:	libzstd-devel
BuildRequires:	libtool

%description
FSArchiver is a system tool that allows you to save the contents of a
filesystem to a compressed archive file. The filesystem contents can be
restored on a device which has a different size and it can be restored on a
different filesystem. Unlike tar/dar, FSArchiver also creates the
filesystem when it extracts the data to devices. Everything is checksummed
in the archive in order to protect the data. If the archive is corrupt, you
just lose the current file, not the whole archive.

PackageName: FSArchiver
Type: console-application
Custom:
  Repo: https://github.com/sailfishos-chum/fsarchiver

%prep
%setup -q -n %{name}-%{version}/fsarchiver

%build
./autogen.sh
%configure --disable-lz4 --disable-lzo --disable-zstd
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*
%doc COPYING README THANKS NEWS

%changelog
