%global pixmapdir %{_datadir}/pixmaps

%define _version 3.9.1
%global _mlterm_rel rel-%(echo %{_version} | tr . _)

Summary:       MultiLingual TERMinal emulator on X
Name:          mlterm
Version:       %{_version}
Release:       hk%{?_dist}
License:       BSD and LGPLv2+ and MIT
Group:         User Interface/X
URL:           https://github.com/arakiken/mlterm
Source0:       %{url}/archive/%{_mlterm_rel}/%{name}-%{_mlterm_rel}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gtk3-devel gtk2-devel libssh2-devel libXft-devel gettext
BuildRequires: gtk2-devel libssh2-devel
#BuildRequires: chrpath
BuildRequires: desktop-file-utils
Requires(postun): /sbin/ldconfig
Requires(post): /sbin/ldconfig


%description
mlterm is a multilingual terminal emulator written from
scratch, which supports various charactersets and encodings
in the world.  It also supports various unique feature such as
anti-alias using FreeType, multiple windows, scroll-bar API,
scroll by mouse wheel, automatic selection of encoding,
and so on. Multiple xims are also supported. 
You can dynamically change various xims.

%prep
%autosetup -n %{name}-%{_mlterm_rel}
%build
%configure \
    --enable-fribidi --with-type-engines=xft,xcore,cairo \
    --enable-utmp --enable-ssh2

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# fix encoding to silence rpmlint
iconv -f EUC-JP -t utf8 doc/ja/README.aafont > doc/ja/README.aafont.utf8 &&
  mv doc/ja/README.aafont.utf8 doc/ja/README.aafont

make DESTDIR=$RPM_BUILD_ROOT INSTALL_OPT="-m 755" install

# remove static files
find $RPM_BUILD_ROOT -name '*.la' -delete
# remove -devel files
find $RPM_BUILD_ROOT -name '*.a' -delete
#rm $RPM_BUILD_ROOT%{_libdir}/libkik.so $RPM_BUILD_ROOT%{_libdir}/libmkf.so

## fix standard rpath
# chrpath --delete \
#     $RPM_BUILD_ROOT%{_bindir}/mlterm \
#     $RPM_BUILD_ROOT%{_libexecdir}/*

SRCDIR=$RPM_BUILD_DIR/%{name}-%{_mlterm_rel}

mkdir -p $RPM_BUILD_ROOT%{pixmapdir}
install -m 644 $SRCDIR/doc/icon/mlterm* \
    $RPM_BUILD_ROOT%{pixmapdir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
cp contrib/icon/mlterm-icon.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/mlterm.svg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat <<EOF >$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Multilingual Terminal
Name[ar]=الطرفية متعددة اللغات
Comment=Use the command line with Arabic support
Comment[ar]=استعمل سطر الأوامر مع دعم اللغة العربية
TryExec=mlterm
Exec=mlterm
Icon=mlterm
Type=Application
Categories=Utility;TerminalEmulator;System;
StartupNotify=true
EOF
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


echo -e "scrollbar_view_name = mozmodern\nuse_anti_alias = true" > $RPM_BUILD_ROOT/etc/mlterm/main
echo -e "DEFAULT = 16,Monospace 16\n" > $RPM_BUILD_ROOT/etc/mlterm/aafont.tmp
cat $RPM_BUILD_ROOT/etc/mlterm/aafont.tmp etc/aafont > $RPM_BUILD_ROOT/etc/mlterm/aafont
rm $RPM_BUILD_ROOT/etc/mlterm/aafont.tmp


%find_lang mlconfig
%post
/sbin/ldconfig

touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
/sbin/ldconfig

touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mlconfig.lang
%defattr(-,root,root,-)
%doc ChangeLog LICENCE README doc/{en,ja}
%config(noreplace) %{_sysconfdir}/mlterm/
%attr(2755,-,utmp) %{_bindir}/mlterm
%{_bindir}/mlcc
%{_bindir}/mlclient
%{_bindir}/mlclientx
%{_bindir}/mlfc
%{_libdir}/libmlterm_core*.so
%{_libdir}/libpobl.*
%{_libdir}/libmef.*
%{_libdir}/mef/libmef_*
%{_libdir}/mlterm/
%{_libexecdir}/*
%{_mandir}/man1/mlcc.1.gz
%{_mandir}/man1/mlclient.1.gz
%{_mandir}/man1/mlterm.1.gz
%{pixmapdir}/mlterm*
%{_datadir}/applications/mlterm.desktop
%{_datadir}/icons/hicolor/scalable/apps/mlterm.svg
%{_datadir}/mlterm/*

%changelog
* Fri May 14 2021 Hiroaki Kobayashi <buribullet@gmail.com> - 4.9.1
- for copr

* Mon Apr 19 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 3.0.0-2
- review process release bump

* Mon Apr 12 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 3.0.0-1
- update to 3.0.0

* Sun Jul 19 2009 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 2.9.4-2
- fix building and replace fribidi-config with pkg-config

* Fri Nov 30 2007 Seiichi SATO <me@seiichisato.jp> - 2.9.4
- Source version 2.9.4

* Tue Nov 13 2001 Araki Ken <j00v0113@ip.media.kyoto-u.ac.jp> - 1.9.42pl6
- Source version 1.9.42pl6
