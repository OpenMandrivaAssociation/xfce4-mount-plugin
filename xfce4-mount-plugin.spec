%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	Mount plugin for the Xfce panel
Name:		xfce4-mount-plugin
Version:	1.1.6
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mount-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-mount-plugin

%description
A mount panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files 
%doc README* ChangeLog AUTHORS
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_libdir}/xfce4/panel/plugins/*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/xfce4-mount-plugin.mo
