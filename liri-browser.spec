%define major 0
%define snapshot 20170210
%define debug_packagr %nil

Summary:        A collection of core classes used throughout Liri
Name:           liri-browser
Version:        0.1.0
Release:        1
License:        LGPLv3
Url:            https://github.com/lirios
Source0:	liri-browser-%{version}-%{snapshot}.tar.xz
Patch0:		0001-add-missing-include-to-fix-src-main-main.cpp-72-25-e.patch

BuildRequires:  cmake(ECM)
BuildRequires:	slime-engine
BuildRequires:	cmake(Fluid)
BuildRequires:	qt5-qtwebengine-devel

%description
A collection of core classes used throughout Liri

%prep
%setup -qn %{name}-%{version}-%{snapshot}
%apply_patches

# fix prefix
sed -i 's!prefix = /usr/local!prefix = %{_prefix}!g' liri-browser.pro
%qmake_qt5 CONFIG+=QTWEBENGINE_ENABLED

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_bindir}/%{name}
