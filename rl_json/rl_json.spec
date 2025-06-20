%{!?tcl_version: %global tcl_version %((echo 8.6; echo 'puts $tcl_version' | tclsh) | tail -1)}
%global _tcl_libdir %{_libdir}/tcl%{tcl_version}
%global _pure_package_name rl_json

Name:       tcl-%{_pure_package_name}
Version:    0.15.3
Release:    2%{?dist}
Summary:    Tcl_Objtype support for JSON
URL:        https://github.com/RubyLane/rl_json
License:    TCL
Source0:    https://github.com/RubyLane/rl_json/archive/refs/tags/%{version}.tar.gz
Source1:    teabase@b293fee.tar.gz
Source2:    tclconfig@683a8da67.tar.gz
Patch1:     rl_json-gcc14.patch
Patch2:     rl_json-inttype.patch
Patch3:     rl_json-dlopen.patch
BuildRequires: autoconf automake libtool
BuildRequires: make, gcc, tcl-devel >= %{tcl_version}
Requires: tcl(abi) >= %{tcl_version}

%description
This package adds a command [json] to the interpreter, and defines a
new Tcl_Obj type to store the parsed JSON document. The [json] command
directly manipulates values whose string representation is valid JSON,
in a similar way to how the [dict] command directly manipulates values
whose string representation is a valid dictionary. It is similar to
[dict] in performance.

%prep
%setup -q -n %{_pure_package_name}-%{version}

tar xvf %{SOURCE1}
tar xvf %{SOURCE2}

%patch 1 -p1
%patch 2 -p1
%patch 3 -p1

%build
autoreconf -fvi

./configure --with-tcl=%{_tcl_libdir} --libdir=%{_tcl_libdir} \
            --enable-symbols
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%make_install INSTALL_LIBRARY="%{__install} -p -m 755"
# INSTALL_LIBRARY='${INSTALL} -m 644' is BAD for find-debuginfo!
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Debuginfo/
# find-debuginfo.sh processes only files that are executable when it’s run

# To avoid filename confliction with tcllib's json.n
mv $RPM_BUILD_ROOT/%{_mandir}/mann/json.n $RPM_BUILD_ROOT/%{_mandir}/mann/rl_json.n

%files
%{_includedir}/*
%{_tcl_libdir}/%{_pure_package_name}%{version}/*
%license LICENSE
%doc
%{_mandir}/mann/*

%changelog
* Tue Jun 17 16:59:50 JST 2025 hkoba <buribullet@gmail.com> - 0.15.3-1
- First build (for Fedora42, Tcl9)
