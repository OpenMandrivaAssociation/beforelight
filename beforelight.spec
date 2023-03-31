Summary:	Sample screen saver
Name:		beforelight
Version:	1.0.6
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xt)

%description
The beforelight program is a sample implementation of a screen saver for
X servers supporting the MIT-SCREEN-SAVER extension.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_datadir}/X11/app-defaults/Beforelight
%doc %{_mandir}/man1/beforelight.*
