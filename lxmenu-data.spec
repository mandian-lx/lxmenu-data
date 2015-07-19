%define git 20140803
Summary:	Menu data files for LXDE
Name:		lxmenu-data
Version:	0.1.3
%if %{git}
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	3
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
%endif
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
BuildRequires:	intltool
BuildArch:	noarch

%description
This package provides files required to build freedesktop.org menu
spec-compliant desktop menus for LXDE.

The files are originally taken from gnome-menus, and some minor
modifications were made.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
[ -e autogen.sh ] && ./autogen.sh

%build
%configure
%make

%install
%makeinstall_std

%files
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxde-applications.menu

