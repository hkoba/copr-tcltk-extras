%if "%{dist}" == ".el7"
%define tcl_version 8.5
%else
%define tcl_version 8.6
%endif
%define _tcldir /usr/lib64/tcl%{tcl_version}

%define name tclreadline
%define version 2.1.0
%define release 7h

%define _tclrl_libdir %{_tcldir}/%{name}%{version}

Summary: GNU readline for TCL
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://tclreadline.sourceforge.net
Source0: https://downloads.sourceforge.net/project/tclreadline/tclreadline/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1: sample.tclshrc
Patch1:  tclreadline.c.encoding.patch
Patch2:  tclreadline-after-fix.patch
Patch3:  tclreadline-nobanghist.patch
Patch4:  tclreadline-threadsafe.patch
Patch5:  tclreadline-libdir.patch
Patch6:  tclreadline-catch.patch
Patch7:  tclreadline-snitcomplete.patch
License: BSD
Group: System/Libraries
# Automatically added by buildreq on Thu Apr 26 2001
# BuildRequires: libreadline-devel ncurses-devel tcl-devel tk XFree86-devel XFree86-libs
BuildRequires: autoconf automake libtool ncurses-devel readline-devel
BuildRequires: tcl-devel >= %{tcl_version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This package contains tclreadline library, which builds a connection
between tcl and the gnu readline.
 
%prep
%setup -q

for f in tclreadlineInit.tcl.in tclreadlineSetup.tcl.in pkgIndex.tcl.in; do
    sed -i.orig -e 's,^#!/usr/local/bin/tclsh,#!/usr/bin/tclsh,' $f
done

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build

autoreconf -fvi

%configure --with-tcl=%{_tcldir} --disable-tclshrl --disable-wishrl \
    TCLRL_LIBDIR=%{_tclrl_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install
rm $RPM_BUILD_ROOT%{_libdir}/libtclreadline*

sh ./libtool --mode=install /bin/install -c libtclreadline.la $RPM_BUILD_ROOT%{_tclrl_libdir}

cp %{SOURCE1} .

%clean

%files
%doc AUTHORS COPYING ChangeLog README TODO sample.tclshrc
%{_tclrl_libdir}
%{_mandir}/mann/tclreadline.n*

%{_includedir}/tclreadline.h

 
%changelog
* Tue Aug  2 2011 KOBAYASHI Hiroaki <hkoba@ssri.co.jp> - 2.1.0-2h
- Refresh

* Thu Apr 26 2001 Sergey Bolshakoff <s.bolshakov@belcaf.com>
- First spec for ALTLinux distribution
