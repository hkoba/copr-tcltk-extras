%define cfgdir %{_sysconfdir}/httpd/conf.d
%define master_conf %{cfgdir}/../conf/httpd.conf

#
# In RedHat, /etc/httpd/logs is symlink to /var/log/httpd and it is not 
# readable/chdir-able to httpd! So, we should move ipcdir to 
# /var/run/fastcgi
#
%define ipcdir %{_var}/run/fastcgi

Summary: Apache module for the FastCGI protocol.
Name: mod_fastcgi
Version: 2.4.7.1
Release: 2h4
Group: System Environment/Daemons
License: Original (See LICENSE.TERMS)
URL: https://github.com/FastCGI-Archives/mod_fastcgi
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: fastcgi.conf
#NoSource: 0
Buildroot: /var/tmp/%{name}-%{version}-root
Requires: coreutils, grep, httpd
BuildRequires: httpd-devel, make, gcc

%description
This Apache module provides support for the FastCGI protocol. FastCGI
is a language independent, scalable, open extension to CGI that
provides high performance and persistence without the limitations of
server specific APIs.

FastCGI applications are not limited to a particular development
language (the protocol is open). FastCGI application libraries
currently exist for Perl, C/ C++, Java, Python, TCL, SmallEiffel, and
Smalltalk.

FastCGI applications use TCP or Unix sockets to communicate with the
web server. This scalable architecture allows applications to run on
the same platform as the web server or on many machines scattered
across an enterprise network.

See the FastCGI http://www.fastcgi.com/ for more information.

%prep
%setup -q -n %{name}-%{version}

%build
cp Makefile.AP2 Makefile
make top_dir=%{_libdir}/httpd


%install
make top_dir=%{_libdir}/httpd MKINSTALLDIRS='mkdir -p'\
	install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{cfgdir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{cfgdir}/fastcgi.conf
mkdir -p $RPM_BUILD_ROOT%{ipcdir}/dynamic


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES *.md docs/*
%{_libdir}/httpd/modules/*
%{cfgdir}/*
%attr(0700,apache,apache) %{ipcdir}
%attr(0700,apache,apache) %{ipcdir}/*

%changelog
* Mon May 16 2021 Hiroaki Kobayashi <buribullet@gmail.com> - 2.4.7.1-2h4
- lastconf -> conf
