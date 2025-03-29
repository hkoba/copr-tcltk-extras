%global debug_package %{nil}

%global tcl_major 8
%global tcl_version 8.6
%global _tcl_configdir %{_libdir}/tcl%{tcl_version}
%global _tcl_libdir    %{_datadir}/tcl%{tcl_major}/%{tcl_version}
%global _pure_package_name tdbcsqlite3

Name:       tcl-%{_pure_package_name}
Version:    1.1.10
Release:    1%{?dist}
Summary:    TDBC SQLite3 driver
URL:        https://tdbc.tcl.tk/
License:    TCL
Source0:    https://sourceforge.net/projects/tcl/files/Tcl/8.6.16/%{_pure_package_name}-%{version}.tar.gz
BuildRequires: make, gcc, tcl-devel >= %{tcl_version}
Requires: tcl(abi) >= %{tcl_version}

%description
TDBC SQLite3 driver

%prep
%setup -q -n %{_pure_package_name}-%{version}

%build
./configure --with-tcl=%{_tcl_configdir} --libdir=%{_datadir} \
            --with-tdbc=%{_tcl_configdir}/tdbc%{version} \
            --enable-symbols
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%{_tcl_libdir}/tdbc/sqlite3-%{version}*
%license license.terms
%doc
%{_mandir}/mann/*

%changelog
* Sat Mar 29 13:01:44 JST 2025 Hiroaki Kobayashi <buribullet@gmail.com> - 1.1.10-1
- Initial build

