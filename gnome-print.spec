Summary:	GNOME print programs
Summary(pl):	GNOME print - biblioteki infrastruktury drukowania w ¶rodowisku GNOME
Name:		gnome-print
Version:	0.24
Release:	2
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-gnome-font-install.patch
Patch1:		%{name}-no_gnome.patch
Icon:		gnome-print.gif
URL:		http://www.levien.com/gnome/print-arch.html
BuildRequires:	automake
# Package ghostscript-fonts-std contains required Type1 fonts
Requires:	ghostscript-fonts-std
Prereq:		libxml
BuildRequires:	libxml-devel
BuildRequires:	libunicode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _fonts_dir      /usr/share/fonts
%define		_datadir	/usr/share
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
Basic programs and libraries that are virtually required for any GNOME
installation. GNOME is the GNU Network Object Model Environment.
That's a fancy name but really GNOME is a nice GUI desktop
environment. It makes using your computer easy, powerful, and easy to
configure.

%description -l pl
GNOME print - biblioteki infrastruktury drukowania w ¶rodowisku GNOME.

%package devel
Summary:	GNOME print libraries, includes, etc
Summary(pl):	GNOME print - pliki nag³ówkowe, etc
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	libunicode-devel

%description devel
Header files for GNOME print.

%description -l pl devel
Pliki nag³ówkowe etc do GNOME print.

%package static
Summary:	GNOME print static libraries
Summary(pl):	Biblioteki statyczne GNOME print
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME print static libraries.

%description -l pl static
Biblioteki statyczne z funkcjami do drukowania w GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
automake
autoconf
%configure  \
	--without-included-gettext
%{__make}

gzip -9nf AUTHORS ChangeLog NEWS README

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

:> $RPM_BUILD_ROOT%{_fonts_dir}/fontmap

%find_lang %{name} --with-gnome

%post
/sbin/ldconfig
%{_bindir}/gnome-font-install --system --scan --no-copy

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%ghost %{_fonts_dir}/fontmap
%{_datadir}/gnome-print

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/libgnomeprint

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
