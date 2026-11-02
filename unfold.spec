Name:		unfold
Version:	1.0.3
Release:	1
Summary:	Archive manager for Linux desktops
License:        GPL-3+
URL:            https://github.com/xapp-project/unfold
Source0:	https://github.com/xapp-project/unfold/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildSystem:    meson

BuildRequires:	desktop-file-utils
BuildRequires:  gettext
BuildRequires:	lib64glib2.0-devel
BuildRequires:	lib64gio-gir2.0
BuildRequires:	lib64gtk3_0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python

Requires:	7zip
Requires:       lib64gtk-gir3.0
Requires:       lib64xapp-gir3.2
Requires:       python
Requires:       python-gi
Requires:       python-setproctitle
Requires:       python-xapp
Requires:       xapp-symbolic-icons

%description
Archive manager for Linux desktops

%prep
%autosetup -p1

%files
%license LICENSES/*
%doc README.md
%{_bindir}/unfold
%{python_sitelib}/unfold/
%{_datadir}/applications/org.x.unfold.desktop
%{_datadir}/icons/hicolor/scalable/apps/unfold.svg
%{_datadir}/nemo/actions/
%{_datadir}/unfold/unfold.svg
