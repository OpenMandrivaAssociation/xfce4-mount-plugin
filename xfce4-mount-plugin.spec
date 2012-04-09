Summary:	Mount plugin for the Xfce panel
Name:		xfce4-mount-plugin
Version:	0.5.5
Release:	%mkrel 8
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-mount-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-mount-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A mount panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang xfce4-mount

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f xfce4-mount.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/scalable/apps/*.svg
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/xfce4-mount-plugin.mo
