%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Mount plugin for the Xfce panel
Name:		xfce4-mount-plugin
Version:	0.6.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mount-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
#BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4ui-1)
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


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 0.5.5-9mdv2012.0
+ Revision: 791557
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.5.5-8
+ Revision: 790073
- Rebuild for xfce 4.10

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.5-7mdv2011.0
+ Revision: 615606
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.5-6mdv2010.1
+ Revision: 543431
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.5.5-5mdv2010.0
+ Revision: 446104
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.5-4mdv2009.1
+ Revision: 349471
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.5-3mdv2009.1
+ Revision: 295001
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.5.5-2mdv2009.0
+ Revision: 269787
- rebuild early 2009.0 package (before pixel changes)

* Mon May 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.5-1mdv2009.0
+ Revision: 208958
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4-2mdv2008.1
+ Revision: 110124
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- use upstream name

* Mon Sep 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4-1mdv2008.0
+ Revision: 92666
- new version
- new version

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-1mdv2008.0
+ Revision: 33449
- new version

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-2mdv2008.0
+ Revision: 33229
- add macros to %%post and %%postun
- spec file clean
- update url

