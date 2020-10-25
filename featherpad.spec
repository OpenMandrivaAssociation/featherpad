Name:		featherpad
Summary:	Lightweight Qt5 Plain-Text Editor for Linux
Version:	0.15.0
Release:	%mkrel 1
Group:		Editors
License:	GPLv3
URL:		https://github.com/tsujan/FeatherPad
Source0:	https://github.com/tsujan/FeatherPad/archive/V%{version}/FeatherPad-%{version}.tar.gz
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	cmake

%description
FeatherPad (by Pedram Pourang, a.k.a. Tsu Jan <tsujan2000@gmail.com>)
is a lightweight Qt5 plain-text editor for Linux. It is independent
of any desktop environment.

%prep
%setup -q -n FeatherPad-%{version}

%build
%cmake_qt5
%cmake_build

%install
%cmake_install

%files
%doc README.md ChangeLog NEWS
%license COPYING
%{_bindir}/%{name}
%{_bindir}/fpad
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help
%{_datadir}/%{name}/help_ja
%{_datadir}/%{name}/translations/
