Name: beforelight
Version: 1.0.1
Release: %mkrel 5
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
Beforelight is a sample screen saver.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .xaw8

rm -f configure && autoconf

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/beforelight
%{_datadir}/X11/app-defaults/Beforelight
%{_mandir}/man1/beforelight.1x.bz2


