%define name	powerpc-utils
%define version	0.0.1
%define release %mkrel 4

Summary:	Maintenance utilities for PowerPC platforms
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		powerpc-utils-0.0.1-ofpathname-devfs.patch.bz2
Patch1:		powerpc-utils-0.0.1-emulate-ofpath.patch.bz2
License:	IBM Common Public License
Group:		System/Configuration/Hardware
Url:		http://powerpc-utils.ozlabs.org/
ExclusiveArch:	ppc ppc64
Requires:	bc

%description
The powerpc-utils package provides the utilities listed below which
are intended for the maintenance of PowerPC platforms.

   * nvram - NVRAM access utility
   * bootlist - boot configuration utility
   * ofpathname - translate logical device names to OF names
   * snap - system configuration snapshot

%prep
%setup -q
%patch0 -p1 -b .ofpathname-devfs
%patch1 -p1 -b .emulate-ofpath

%build
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%ifarch ppc64
# "ofpath" is obsolete but still provide compatible replacement
ln -s ofpathname $RPM_BUILD_ROOT%{_sbindir}/ofpath
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYRIGHT
%{_sbindir}/bootlist
%{_sbindir}/nvram
%ifarch ppc64
%{_sbindir}/ofpath
%endif
%{_sbindir}/ofpathname
%{_sbindir}/snap
%{_mandir}/man8/bootlist.8*
%{_mandir}/man8/nvram.8*
%{_mandir}/man8/ofpathname.8*
%{_mandir}/man8/snap.8*

