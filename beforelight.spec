%define name	beforelight
%define version	1.0.2
%define release	%mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Sample screen saver
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
Patch0: beforelight-1.0.1-use-xaw8.patch
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: libxscrnsaver-devel >= 1.0.1
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: autoconf

%description
The beforelight program is a sample implementation of a screen saver for
X servers supporting the MIT-SCREEN-SAVER extension.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .xaw8

rm -f configure && autoconf

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}		
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# I have no idea why the path gets doubled, but it's just one file and
# it's easier to move it manually than figure out what's wrong with 
# the build process. -AdamW 2007/06

mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
mv %{buildroot}%{buildroot}%{_datadir}/X11/app-defaults/Beforelight %{buildroot}%{_datadir}/X11/app-defaults/Beforelight

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/X11/app-defaults/Beforelight
%{_mandir}/man1/beforelight.*
