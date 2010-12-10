Summary:	Menu data files for LXDE
Name:     	lxmenu-data
Version:	0.1.1
Release:	%mkrel 2
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
