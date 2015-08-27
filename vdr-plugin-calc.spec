%define plugin	calc
%define tarversion 0[1].0.1-%rcver
%define rcver	rc5

Summary:	VDR plugin: VDR mini calculator
Name:		vdr-plugin-%plugin
Version:	0.0.1
Release:	0.%rcver.21
Group:		Video
License:	GPL
URL:		http://www.vdrcalc.bmschneider.de/index2.html
Source:		http://www.vdrcalc.bmschneider.de/dateien/vdr-%plugin-%tarversion.tar.bz2
Patch1:		calc-0.0.1-rc5-extra-qualification.patch
Patch2:		calc-02_pathes.dpatch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
Requires:	bc

%description
This is a small calculator plugin for the VDR.
It supports the 4 basic mathematic functions plus a memory, just
like your pocket calculator. It now has also the basic trigonometric
functions.

%prep
%setup -q -n %plugin-%{version}-%rcver
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY



