### workaround for Clang 15+
%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:           g4music
Version:        4.3
Release:        1
Summary:        Fast fluent lightweight music player written in GTK4
Group:          Sound
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/neithern/g4music
Source0:        https://gitlab.gnome.org/neithern/g4music/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala
 
Requires:       dbus-common
Requires:       hicolor-icon-theme

Provides: gapless = %{version}-%{release}
 
%description
G4Music is a fast fluent lightweight music player written in GTK4, with
a beautiful and adaptive user interface.  It focuses on high performance
for large music collections.
 
Features:
- Supports most music file types, samba and any other remote protocol
  (depends on GIO and GStreamer).
- Fast loading and parsing thousands of music files in a few seconds,
  monitors local changes.
- Low memory usage for large music collections with album covers
  (embedded and external), no thumbnail caches to store.
- Groups and sorts by album/artist/title, shuffle list, full-text
  searching.
- Gaussian blurred cover as background, follows GNOME light/dark mode.
- Drag-drop from GNOME Files, showing music in Files.
- Supports audio peaks visualizer.
- Supports gapless playback.
- Supports normalizing volume with ReplayGain.
- Supports pipewire and other audio sinks.
- Supports MPRIS control.
 
%prep
%autosetup -n %{name}-v%{version} -p1
 
# From fedora - only requires that appstream-util pass at the validate-relax level
sed -i "s/'validate'/'validate-relax'/" data/meson.build
 
%build
%meson --buildtype=release
%meson_build

%install
%meson_install
%find_lang %{name}
 
%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/g4music
%{_datadir}/applications/com.github.neithern.g4music.desktop
%{_datadir}/dbus-1/services/com.github.neithern.g4music.service
%{_datadir}/glib-2.0/schemas/com.github.neithern.g4music.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.neithern.g4music.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.neithern.g4music-symbolic.svg
%{_metainfodir}/com.github.neithern.g4music.metainfo.xml
 
