Summary:	Menu data files for LXDE
Name:		lxmenu-data
Version:	0.1.5
Release:	2
Url:		http://lxde.sourceforge.net/
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Graphical desktop/Other
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(lxqt-globalkeys)

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

This package provides files required to build freedesktop.org menu
spec-compliant desktop menus for LXDE.

The files are originally taken from gnome-menus, and some minor
modifications were made.

%files
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxde-applications.menu

#---------------------------------------------------------------------------

%prep
%setup -q

%build
[ -e autogen.sh ] && ./autogen.sh
%configure
%make

%install
%makeinstall_std

