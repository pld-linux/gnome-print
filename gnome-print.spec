Summary:	GNOME print programs
Summary(pl):	GNOME print - biblioteki infrastruktury drukowania w ¶rodowisku GNOME
Name:		gnome-print
Version:	0.31
Release:	3
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-localeh.patch
Patch1:		%{name}-gnome-font-install.patch
Patch2:		%{name}-am15.patch
Icon:		gnome-print.gif
URL:		http://www.levien.com/gnome/print-arch.html
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	libxml-devel
BuildRequires:	libunicode-devel
BuildRequires:	gnome-libs-devel >= 1.2.12-3
# Package ghostscript-fonts-std contains required Type1 fonts
Requires:	ghostscript-fonts-std
Prereq:		/sbin/ldconfig
Prereq:		libxml
# that's sick - gnome-font-install requires packages below...
Prereq:		esound
Prereq:		audiofile
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgnomeprint11

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
Summary(pl):	GNOME print - pliki nag³ówkowe itp.
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	libunicode-devel
Requires:	gdk-pixbuf-devel
Requires:	gnome-libs-devel

%description devel
Header files for GNOME print.

%description -l pl devel
Pliki nag³ówkowe itp. do GNOME print.

%package static
Summary:	GNOME print static libraries
Summary(pl):	Biblioteki statyczne GNOME print
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
GNOME print static libraries.

%description -l pl static
Biblioteki statyczne z funkcjami do drukowania w GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing acinclude.m4
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
libtoolize --copy --force
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c
%configure  \
	--without-included-gettext
%{__make}

gzip -9nf AUTHORS ChangeLog NEWS README

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

:> $RPM_BUILD_ROOT%{_fonts_dir}/fontmap
:> $RPM_BUILD_ROOT%{_fonts_dir}/fontmap2

%find_lang %{name} --with-gnome

#%clean
#rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
echo "Generate /usr/share/fonts/fontmap file"
%{_bindir}/gnome-font-install -r -c -t /usr/share/fonts/fontmap2 /usr/share/fonts/

%postun -p /sbin/ldconfig

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
%{_includedir}/gnome-1.0/libgnomeprint

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
