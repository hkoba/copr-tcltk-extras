%if "%{dist}" == ".el7"
%global tcl_version 8.5
%else
%global tcl_version 8.6
%endif
%global tcl_sitelib %{_datadir}/tcl%{tcl_version}

%global version	 0.4
%global _micro_version 0

Summary:   FastCGI interface for Tcl 8
Name:      tcl-fcgi
Version:   %{version}
Group:     Development/Languages/Tcl
URL:       https://www.nyx.net/~tpoindex/tcl.html#Fcgi
Release:   4h
Source:    ftp://ftp.procplace.com/pub/tcl/sorted/packages-7.6/net/fcgi.tcl-0.4/fcgi.tcl-%{version}.tar.gz
Patch0: tcl-fcgi-rename.patch
License:   BSD
Packager:  hkoba <hkoba@users.sourceforge.net>
Buildroot: %{_tmppath}/%{name}-%{version}
Requires:  tcl, tclx
BuildRequires: tcl
BuildArch:  noarch

%description
Fcgi.tcl is a Tcl interface for the FastCGI protocol.  Fcgi.tcl is designed to
work with Tcl 8.0. Although original Fcgi.tcl contains a Tcl C extension version,
this package provides only a Tcl source version which is written in 100% pure Tcl.

%prep

%setup -n fcgi.tcl-%{version}
%patch0 -p0

%build

sed -e s/@FCGI_VERSION_FULL@/%{version}.%{_micro_version}/ tcl-src/fcgi.tcl.in \
    > tcl-src/fcgi.tcl

sed -e s/@FCGI_VERSION@/%{version}/ tcl-src/pkgIndex.tcl.in \
    > tcl-src/pkgIndex.tcl

#==========================================
%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/share/man

./mkinstalldirs 

SCRIPTDIR=%{tcl_sitelib}/Fcgi%{version}

./mkinstalldirs ${RPM_BUILD_ROOT}$SCRIPTDIR ${RPM_BUILD_ROOT}%{_mandir}/mann/

cp -v tcl-src/fcgi.tcl ${RPM_BUILD_ROOT}$SCRIPTDIR
cp -v tcl-src/pkgIndex.tcl ${RPM_BUILD_ROOT}$SCRIPTDIR

cp -v doc/fcgi.tcl.man ${RPM_BUILD_ROOT}%{_mandir}/mann/fcgi.tcl.n



# make install-tcl-src prefix=${RPM_BUILD_ROOT}%{_prefix} \
#    MANN_DIR=${RPM_BUILD_ROOT}/usr/share/man
#==========================================

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc HISTORY  INSTALL  LICENSE.TERMS  NOTES  README
%{tcl_sitelib}/*
%{_mandir}/mann/*

%changelog
