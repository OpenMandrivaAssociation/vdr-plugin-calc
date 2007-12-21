
%define plugin	calc
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define tarversion 0[1].0.1-%rcver
%define rcver	rc5
%define rel	13
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
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
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


