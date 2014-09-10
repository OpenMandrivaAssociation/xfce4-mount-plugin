%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Mount plugin for the Xfce panel
Name:		xfce4-mount-plugin
Version:	0.6.7
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mount-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
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
