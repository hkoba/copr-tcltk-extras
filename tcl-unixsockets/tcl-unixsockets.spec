%if "%{dist}" == ".el7"
%global tcl_version 8.5
%else
%global tcl_version 8.6
%endif
%global _tcldir /usr/lib64/tcl%{tcl_version}

%global name tcl-unixsockets
%global version 0.2
%global release 1h

Summary: unix_sockets for Tcl
Name: %{name}
Version: %{version}
Release: %{release}
URL: https://sourceforge.net/projects/tcl-unixsockets/
Source0: ftp://tcl-unixsockets.sourceforge.net/pub/tcl-unixsockets/%{name}_%{version}.tar.gz
License: BSD
Group: System/Libraries
# Automatically added by buildreq on Thu Apr 26 2001
# BuildRequires: libreadline-devel ncurses-devel tcl-devel tk XFree86-devel XFree86-libs
BuildRequires: autoconf automake libtool
BuildRequires: tcl, tcl-devel >= %{tcl_version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This package contains unix_sockets for tcl.
 
%prep
%setup -q -n %{name}_%{version}

%build

autoreconf -fvi

%configure --with-tcl=%{_tcldir}

make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install \
     pkglibdir=%{_tcldir}/%{name}%{version}

%clean

%files
%{_tcldir}/%{name}%{version}/*
%{_mandir}/mann/unix_sockets.n*

 
%changelog
* Tue Aug  2 2011 KOBAYASHI Hiroaki <hkoba@ssri.co.jp> - 2.1.0-2h
- Init
