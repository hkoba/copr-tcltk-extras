%global tcl_version 8.6
%global _tcl_libdir %{_libdir}/tcl%{tcl_version}
%global _pure_package_name tdbc


Name:       tcl-%{_pure_package_name}
Version:    1.1.10
Release:    1%{?dist}
Summary:    Tcl DataBase Connectivity
URL:        https://tdbc.tcl.tk/
License:    TCL
Source0:    https://sourceforge.net/projects/tcl/files/Tcl/8.6.16/tdbc1.1.10.tar.gz
BuildRequires: make, gcc, tcl-devel >= %{tcl_version}
Requires: tcl(abi) >= %{tcl_version}


%description
TDBC is an acronym for Tcl Database Connectivity, an interface
standard for SQL databases and connectivity that aims to make it easy
to write portable and secure Tcl scripts that access SQL databases.

%prep
%setup -q -n %{_pure_package_name}%{version}

%build
./configure --with-tcl=%{_tcl_libdir} --libdir=%{_tcl_libdir} \
            --enable-symbols
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%{_tcl_libdir}/%{_pure_package_name}%{version}/*
%license license.terms
%{_includedir}/*
%doc
%{_mandir}/man3/*
%{_mandir}/mann/*

%changelog
* Sat Mar 29 12:17:00 JST 2025 Hiroaki Kobayashi <buribullet@gmail.com> - 1.1.10-1
- Initial build
