Summary:	Mount plugin for the Xfce panel
Name:		xfce4-mount-plugin
Version:	0.6.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-mount-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.9.0
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libxfce4ui-devel >= 4.9.0
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
%{_iconsdir}/hicolor/*/apps/*.*g
%{_libdir}/xfce4/panel/plugins/libmout.so
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/xfce4-mount-plugin.mo
