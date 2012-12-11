
%define plugin	calc
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define tarversion 0[1].0.1-%rcver
%define rcver	rc5
%define rel	19
%define release 0.%rcver.%rel

Summary:	VDR plugin: VDR mini calculator
Name:		%name
Version:	%version
Release:	%mkrel %release
Group:		Video
License:	GPL
URL:		http://www.vdrcalc.bmschneider.de/index2.html
Source:		http://www.vdrcalc.bmschneider.de/dateien/vdr-%plugin-%tarversion.tar.bz2
Patch1:		calc-0.0.1-rc5-extra-qualification.patch
Patch2:		calc-02_pathes.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
Requires:	bc

%description
This is a small calculator plugin for the VDR.
It supports the 4 basic mathematic functions plus a memory, just
like your pocket calculator. It now has also the basic trigonometric
functions.

%prep
%setup -q -n %plugin-%version-%rcver
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.19mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.18mdv2009.1
+ Revision: 359295
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.17mdv2009.0
+ Revision: 197907
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.16mdv2009.0
+ Revision: 197638
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- fix paths (P2 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.15mdv2008.1
+ Revision: 145044
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.14mdv2008.1
+ Revision: 144994
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.13mdv2008.1
+ Revision: 103070
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.12mdv2008.0
+ Revision: 49976
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.11mdv2008.0
+ Revision: 42063
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.10mdv2008.0
+ Revision: 22719
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.9mdv2007.0
+ Revision: 90898
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.8mdv2007.1
+ Revision: 73962
- rebuild for new vdr
- Import vdr-plugin-calc

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.7mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.3mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.2mdv2007.0
- rebuild for new vdr

* Sun Jun 04 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-0.rc5.1mdv2007.0
- initial Mandriva release

