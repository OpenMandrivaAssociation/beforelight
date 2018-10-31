Summary:	Sample screen saver
Name:		beforelight
Version:	1.0.5
Release:	10
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xt)

%description
The beforelight program is a sample implementation of a screen saver for
X servers supporting the MIT-SCREEN-SAVER extension.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/%{name}
%{_datadir}/X11/app-defaults/Beforelight
%{_mandir}/man1/beforelight.*

