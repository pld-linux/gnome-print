Summary:	GNOME print programs
Summary(pl):	GNOME print - biblioteki infrastruktury drukowania w �rodowisku GNOME
Name:		gnome-print
Version:	0.16
Release:	1
License:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		gnome-print-gnome-font-install.patch
Icon:		gnome-print.gif
URL:		http://www.levien.com/gnome/print-arch.html
# Package urw-fonts contains required Type1 fonts
Requires:       urw-fonts
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define         _fonts_dir      /usr/share/fonts
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
Basic programs and libraries that are virtually required for any GNOME
installation.  GNOME is the GNU Network Object Model Environment. That's a
fancy name but really GNOME is a nice GUI desktop environment. It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
GNOME print - biblioteki infrastruktury drukowania w �rodowisku GNOME.

%package devel
Summary:	GNOME print libraries, includes, etc
Summary(pl):	GNOME print - pliki nag��wkowe, etc
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for GNOME print.

%description -l pl devel
Pliki nag��wkowe etc do GNOME print.

%package static
Summary:	GNOME print static libraries
Summary(pl):	Biblioteki statyczne GNOME print
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME print static libraries.

%description -l pl static
Biblioteki statyczne z funkcjami do drukowania w GNOME.

%prep
%setup -q
%patch0 -p1

%build
gettextize --copy --force
automake
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure  \
	--without-included-gettext
make

gzip -9nf AUTHORS ChangeLog NEWS README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fonts_dir}/Type1/afm
make DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%{_datadir}/fonts/afms/adobe \
   $RPM_BUILD_ROOT%{_fonts_dir}/Type1/afm
install fonts/*.font   $RPM_BUILD_ROOT%{_fonts_dir}
   

strip --strip-unneeded $RPM_BUILD_ROOT%{_prefix}/lib/lib*.so.*.*

%find_lang %{name} --with-gnome

%post
/sbin/ldconfig
if [ -f %{_fonts_dir}/fontmap ]; then
      cp -p %{_fonts_dir}/fontmap "%{_fonts_dir}/fontmap-`date +"%d-%m-%Y-%T"`"
fi

%{_bindir}/gnome-font-install --system --scan --no-copy \
      --afm-path=%{_fonts_dir}/Type1/afm \
      --pfb-path=%{_fonts_dir}/Type1 \
      --fontmap-path=%{_fonts_dir} \
      --pfb-assignment=ghostscript,%{_fonts_dir}/default/ghostscript \
      --pfb-assignment=ghostscript,%{_fonts_dir}/default/Type1 \
      --afm-assignment=ghostscript,%{_fonts_dir}/default/ghostscript \
      --afm-assignment=ghostscript,%{_fonts_dir}/default/Type1 \
      %{_fonts_dir}

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_fonts_dir}/*.font
%{_fonts_dir}/Type1/afm/adobe
%{_datadir}/gnome-print

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/libgnomeprint

%files static
%attr(644,root,root) %{_libdir}/lib*.a