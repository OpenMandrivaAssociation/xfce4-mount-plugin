Summary:	Mount plugin for the Xfce panel
Name:		xfce-mount-plugin
Version:	0.5.4
Release:	%mkrel 1
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
Source0:	xfce4-mount-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3
BuildRequires:	xfce-panel-devel >= 4.3
BuildRequires:	libxfcegui4-devel >= 4.3.0 
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A mount panel plugin for the Xfce Desktop Environment.

%prep
%setup -q -n xfce4-mount-plugin-%{version}

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
%doc README ChangeLog COPYING AUTHORS
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/scalable/apps/*.svg
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/xfce4-mount-plugin.mo
