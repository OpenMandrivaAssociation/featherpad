Name:		featherpad
Summary:	Lightweight Qt6 Plain-Text Editor for Linux
Version:	1.6.1
Release:	1
Group:		Editors
License:	GPLv3
URL:		https://github.com/tsujan/FeatherPad
Source0:	https://github.com/tsujan/FeatherPad/archive/V%{version}/FeatherPad-%{version}.tar.gz

BuildRequires:	pkgconfig(hunspell)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake
BuildRequires:  qmake-qt6

%description
FeatherPad (by Pedram Pourang, a.k.a. Tsu Jan <tsujan2000@gmail.com>)
is a lightweight Qt5 plain-text editor for Linux. It is independent
of any desktop environment.

%prep
%setup -q -n FeatherPad-%{version}

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc README.md ChangeLog NEWS
%license COPYING
%{_bindir}/%{name}
%{_bindir}/fpad
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/featherpad.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help
%{_datadir}/%{name}/translations/
