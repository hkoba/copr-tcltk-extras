%if 0%{?fedora} >= 42
%global tcl_version 9.0
%else
%global tcl_version 8.6
%endif

%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Summary: Table/matrix widget extension to Tcl/Tk
Name: tktable
Version: 2.12
Release: 1hk1
License: TCL
Group: Development/Libraries
Source: https://chiselapp.com/user/bohagan/repository/TkTable/uv/tktable-%{version}.tar.gz
URL: http://tktable.sourceforge.net/
BuildRequires: /usr/bin/gcc, tk-devel >= %{tcl_version}, libXt-devel
Requires: tk >= %{tcl_version}
BuildRoot: %_tmppath/%name-%version-%release-root-%(%__id_u -n)

Requires: tcl(abi) >= %{tcl_version}

%description
Tktable provides a table/matrix widget for Tk programs. Features:
multi-line cells, embedded windows, variable width columns/height rows
(interactively resizable), scrollbar support, tag styles per row,
column or cell, in-cell editing, works on UNIX, Windows and MacIntosh,
Unicode support with Tk 8.1 and above.

%prep

%setup -q
# Silence a rpmlint warning
chmod -x ChangeLog

%build
# fix problem with the tcl.m4 file that came with earlier versions
# of Tcl (quoting bug in the file that was not exposed until bash
# 3.1 was packaged with FC5)
sed -i -e "s,relid',relid," configure
%configure --with-tcl=%_libdir --with-tk=%_libdir --x-libraries=%_libdir --x-includes=%_includedir/X11 --libdir=%{tcl_sitearch}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install INSTALL_LIBRARY="%{__install} -p -m 755"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README.txt license.txt doc/tkTable.html
%_mandir/mann/tkTable.*
%{tcl_sitearch}/Tktable*/*


%changelog
* Fri Jun 12 2015 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.
  Tue Oct 22 2003 --> Tue Oct 21 2003 or Wed Oct 22 2003 or Tue Oct 28 2003 or ....
  Tue Nov 16 2003 --> Tue Nov 11 2003 or Sun Nov 16 2003 or Tue Nov 18 2003 or ....
  Thu Nov 11 2005 --> Thu Nov 10 2005 or Fri Nov 11 2005 or Thu Nov 17 2005 or ....

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 09 2008 Wart <wart at kobold.org> 2.9-11
- Rebuild for gcc 4.3
- Clarify license tag

* Fri Jan 04 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.9-10
- Rebuilt for tcl 8.5
- Following PackagingDrafts/Tcl

* Wed Mar 1 2006 Jean-Luc Fontaine <jfontain@free.fr> 2.9-9
- fixed problem in configuration stage 

* Tue Feb 28 2006 Jean-Luc Fontaine <jfontain@free.fr> 2.9-8
- specified X11 includes path in configuration

* Tue Feb 28 2006 Jean-Luc Fontaine <jfontain@free.fr> 2.9-7
- require libXt-devel for building

* Tue Feb 28 2006 Jean-Luc Fontaine <jfontain@free.fr> 2.9-6
- specified X11 librairies and includes paths in configuration

* Tue Feb 28 2006 Jean-Luc Fontaine <jfontain@free.fr> 2.9-5
- rebuild for Fedora Extras 5

* Fri Nov 11 2005 Jean-Luc Fontaine <jfontain@free.fr> 2.9-4
  Thu Nov 11 2005 --> Thu Nov 10 2005 or Fri Nov 11 2005 or Thu Nov 17 2005 or ....
- only require tk and tk-devel for building

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.9-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Sep 20 2004 Jean-Luc Fontaine <jfontain@free.fr> 0:2.9-0.fdr.1
- Tktable version 2.9 new source release

* Mon Dec 8 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.8-0.fdr.10
- removed %%doc tag for manual page since rpm does it automatically

* Sun Dec 7 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.8-0.fdr.9
- changed license to BSD like
- removed redundant XFree86 libraries build requirement
- added SMP flags to make stage

* Sun Nov 16 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.8-0.fdr.8
  Tue Nov 16 2003 --> Tue Nov 11 2003 or Sun Nov 16 2003 or Tue Nov 18 2003 or ....
- in install stage, removed some useless manual installation of
  documentation files which left them in the BUILD directory

* Sun Nov 16 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.8-0.fdr.7
  Tue Nov 16 2003 --> Tue Nov 11 2003 or Sun Nov 16 2003 or Tue Nov 18 2003 or ....
- in build requirements, work around tcl-devel and tk-devel packages non
  existence in RH 8.0 and 9

* Thu Nov 6 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.8-0.fdr.6
- escaped percent characters in change log

* Tue Nov 4 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.8-0.fdr.5
- use "download.sourceforge.net/..." instead of
  "prdownloads.sourceforge.net/..." to make URLs directly downloadable
- removed AutoReqProv
- used "%%setup -q -n ..." to remove unnecessary cd's.
- added -p argument to install to preserve timestamps
- replaced %%__install by install
- no longer use RPM_OPT_FLAGS in CFLAGS as make argument as %%configure
  already handles it

* Sat Nov 1 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.8-0.fdr.4
- removed RCS line
- set Epoch to 0 and removed it from Release
- used a full macroless URL to the source tarball
- removed Packager (not used in Fedora)
- used rm instead of %%__rm macro
- use wildcards in manual pages files entry
- added epoch to build requirements

* Wed Oct 22 2003 Jean-Luc Fontaine <jfontain@free.fr> 0:2.8-0.fdr.3
  Tue Oct 22 2003 --> Tue Oct 21 2003 or Wed Oct 22 2003 or Tue Oct 28 2003 or ....
- checked with rpmlint and improved accordingly
- release 3 as previous non-fedora spec file release was 2
