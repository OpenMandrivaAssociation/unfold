Name:		unfold
Version:	1.0.5
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
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	typelib(Gio)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python

Requires:	7zip
Requires:       typelib(Gtk)
Requires:       typelib(XApp)
Requires:       python
Requires:       python-gi
Requires:       python-setproctitle
Requires:       python-xapp
Requires:       xapp-symbolic-icons

%description
Archive manager for Linux desktops

%prep
%autosetup -p1

%build
%meson_build
 
%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/unfold
%{python_sitelib}/unfold/
%{_datadir}/applications/org.x.unfold.desktop
%{_datadir}/icons/hicolor/scalable/apps/unfold.svg
%{_datadir}/nemo/actions/
%{_datadir}/unfold/unfold.svg
