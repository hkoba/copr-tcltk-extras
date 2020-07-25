%if "%{dist}" == ".el7"
%global tcl_version 8.5
%else
%global tcl_version 8.6
%endif
%global tcl_libpath %{_datadir}/%{tcl_version}
%global ver 1.0

Summary: tkIcons(ICONS) is a cross platform icon library facility for Tcl/Tk programmers.
Name: tkIcons
Version: %ver
Release: 3
License: Original
Vendor: Adrian Davis (adrian@satisoft.com)
Group: System Environment/Libraries
Url: http://www.satisoft.com/tcltk/icons/
Source: http://www.satisoft.com/tcltk/icons/icons.zip
Source1: http://www.satisoft.com/tcltk/icons/icons-crystal.zip
Source2: http://www.satisoft.com/tcltk/icons/icons-klassic.zip
Source3: http://www.satisoft.com/tcltk/icons/icons-slick.zip
Requires: tk
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: ed

%description

%prep
%setup -n icons2 -a 1 -a 2 -a 3
ed viewIcons.tcl <<END
1i
#!/usr/bin/wish
.
/set INITIALDIR
/
c
set INITIALDIR [file join [info library] tkIcons]
.
p
wq
END


%build

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{tcl_libpath}/%{name}

cp -va * %{buildroot}/%{tcl_libpath}/%{name}

%files
%defattr(-,root,root)
%{tcl_libpath}/%{name}

%changelog
