%global tcl_version 8.6
%global _tcl_libdir %{_libdir}/tcl%{tcl_version}
%global _pure_package_name tdbcpostgres

Name:       tcl-%{_pure_package_name}
Version:    1.1.10
Release:    2%{?dist}
Summary:    TDBC PostgreSQL driver
URL:        https://tdbc.tcl.tk/
License:    TCL
Source0:    https://sourceforge.net/projects/tcl/files/Tcl/8.6.16/%{_pure_package_name}%{version}.tar.gz
BuildRequires: make, gcc, tcl-devel >= %{tcl_version}
BuildRequires: tcl-tdbc
BuildRequires: postgresql-private-devel, postgresql-private-libs
Requires: tcl(abi) >= %{tcl_version}

%description
TDBC PostgreSQL driver

%prep
%setup -q -n %{_pure_package_name}%{version}

%build
./configure --with-tcl=%{_tcl_libdir} --libdir=%{_tcl_libdir} \
            --with-tdbc=%{_tcl_libdir}/tdbc%{version} \
            --enable-symbols
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install INSTALL_LIBRARY="%{__install} -p -m 755"

%files
%{_tcl_libdir}/%{_pure_package_name}%{version}/*
%license license.terms
%{_includedir}/*
%doc
%{_mandir}/mann/*

%changelog
* Sat Mar 29 18:58:45 JST 2025 Hiroaki Kobayashi <buribullet@gmail.com> - 1.1.10-2
- Build with debuginfo
