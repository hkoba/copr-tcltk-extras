%global commit ae2e673a6abcb5c82d5b4fd426cb310993ede4c8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global _github_owner hkoba
%global _github_project tkhtml3

%if "%{dist}" == ".el7"
%global tcl_version 8.5
%else
%global tcl_version 8.6
%endif
%global tcl_libdir %{_libdir}/tcl%{tcl_version}
%global tkhtml_major 3
%global pure_name tkhtml

Summary: HTML widget for Tcl/Tk
Name: tkhtml3
Version: %{tkhtml_major}.0
Release: 8hk
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
