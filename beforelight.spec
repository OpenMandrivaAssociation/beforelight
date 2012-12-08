%define name	beforelight
%define version	1.0.4
%define release	%mkrel 4

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Sample screen saver
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
Patch0: beforelight-1.0.1-xprint.patch
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
#patch0 -p1 -b .xprint

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/X11/app-defaults/Beforelight
%{_mandir}/man1/beforelight.*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 663320
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 591906
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5mdv2010.1
+ Revision: 522196
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdv2010.0
+ Revision: 413169
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 1.0.3-3mdv2009.1
+ Revision: 364710
- xprint patch is not needed

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 220481
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

* Mon Oct 22 2007 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2008.1
+ Revision: 101321
- kill no more needed hack
- new release
- better description
- fix man pages extension

* Mon Jun 18 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 41046
- new release 1.0.2; rebuild for 2008; hack for file install location oddness


* Mon Aug 14 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-14 14:42:23 (55975)
- Use libxaw8 instead of old legacy library

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:22:43 (31741)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 21:42:39 (27452)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

