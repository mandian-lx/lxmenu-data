Summary:	Menu data files for LXDE
Name:     	lxmenu-data
Version:	0.1.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRequires:	intltool
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package provides files required to build freedesktop.org menu
spec-compliant desktop menus for LXDE.

The files are originally taken from gnome-menus, and some minor
modifications were made.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxde-applications.menu


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 693008
- update to 0.1.2

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-2mdv2011.0
+ Revision: 620282
- the mass rebuild of 2010.0 packages

* Thu Oct 01 2009 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2010.0
+ Revision: 451942
- New version 0.1.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.1-2mdv2010.0
+ Revision: 439689
- rebuild

* Wed Dec 10 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.1
+ Revision: 312481
- import lxmenu-data


