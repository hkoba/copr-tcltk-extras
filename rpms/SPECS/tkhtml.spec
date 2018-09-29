%global commit 80afcc8fecd5f86f138ebd0065ba6785a48e5721
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _github_owner hkoba
%define _github_project tkhtml3

%define tcl_version 8.6
%define tcl_libdir %{_libdir}/tcl%{tcl_version}
%define tkhtml_major 3
%define pure_name tkhtml

Summary: HTML widget for Tcl/Tk
Name: tkhtml3
Version: %{tkhtml_major}.0
Release: 6hk
Group: Development/Languages
License: LGPL2
Source0: https://github.com/%{_github_owner}/%{_github_project}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires: /usr/bin/gcc, tk-devel >= %{tcl_version}, libXt-devel
Requires: tk >= %{tcl_version}
Buildroot: /var/tmp/%{name}-%{version}-root

%description
TkHTML is a tk widget for Tcl. This module provides basic HTML rendering and
browsing functionarity.

%prep
echo PREP start
%setup -q -n %{pure_name}%{tkhtml_major}-%{commit}

%build
./configure --with-tcl=%{_libdir} --with-tk=%{_libdir} \
   --mandir=%{_mandir} --libdir=%{tcl_libdir} \
   %{?_with_thread: --enable-threads} --enable-shared

make CFLAGS="-fPIC %{optflags}"

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc COPYRIGHT README
%{_libdir}/tcl%{tcl_version}/Tkhtml3.0/*
%{_mandir}/mann/*


%changelog
