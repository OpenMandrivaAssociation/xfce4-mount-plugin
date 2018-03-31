%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	Mount plugin for the Xfce panel
Name:		xfce4-mount-plugin
Version:	1.1.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mount-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2) >= 4.11
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-mount-plugin

%description
A mount panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files 
%doc README ChangeLog AUTHORS
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_libdir}/xfce4/panel/plugins/*
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/xfce4-mount-plugin.mo
