Summary:	GNOME print programs
Summary(es):	Sistema de impresión de GNOME
Summary(pl):	GNOME print - biblioteki infrastruktury drukowania w ¶rodowisku GNOME
Summary(pt_BR):	O sistema de impressão do GNOME
Name:		gnome-print
Version:	0.35
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.bz2
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
Obsoletes:	libgnomeprint15

%define		_prefix		/usr/X11R6
%define         _fonts_dir      /usr/share/fonts
%define		_org_datadir	%{_prefix}/share
%define		_datadir	/usr/share
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
Basic programs and libraries that are virtually required for any GNOME
installation. GNOME is the GNU Network Object Model Environment.
That's a fancy name but really GNOME is a nice GUI desktop
environment. It makes using your computer easy, powerful, and easy to
configure.

%description -l es
gnome-print incluye las bibliotecas que se necesitan para que los
programas GNOME puedan imprimir.

%description -l pl
GNOME print - biblioteki infrastruktury drukowania w ¶rodowisku GNOME.

%description -l pt_BR
O gnome-print inclui as bibliotecas necessárias para que programas
GNOME possam imprimir.

%package devel
Summary:	GNOME print libraries, includes, etc
Summary(es):	Bibliotecas y archivos de inclusión de GNOME print
Summary(pl):	GNOME print - pliki nag³ówkowe itp.
Summary(pt_BR):	Bibliotecas e arquivos de inclusão do GNOME print
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	libunicode-devel
Requires:	gdk-pixbuf-devel
Requires:	gnome-libs-devel
Obsoletes:	libgnomeprint15-devel

%description devel
Header files for GNOME print.

%description -l es devel
Este paquete contiene las bibliotecas y los archivos de encabezamiento
que se necesitan para compilar las aplicaciones que usan GNOME print.

%description -l pl devel
Pliki nag³ówkowe itp. do GNOME print.

%description -l pt_BR devel
Esse pacote contém as bibliotecas e os arquivos de cabeçalho
necessários para compilar aplicações que usam o gnome-print.

%package static
Summary:	GNOME print static libraries
Summary(es):	Static libraries for gnome-print development
Summary(pl):	Biblioteki statyczne GNOME print
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com o gnome-print
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNOME print static libraries.

%description -l es static
Static libraries for gnome-print development.

%description -l pl static
Biblioteki statyczne z funkcjami do drukowania w GNOME.

%description -l pt_BR static
Bibliotecas estáticas para desenvolvimento com o gnome-print.

%prep
%setup -q
#%patch0 -p1
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aliasdir=%{_org_datadir}/gnome/fonts \
	mapdir=%{_org_datadir}/gnome/fonts

install fonts/*.font $RPM_BUILD_ROOT%{_org_datadir}/gnome/fonts

:> $RPM_BUILD_ROOT%{_fonts_dir}/fontmap2

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
echo "Generating %{_datadir}/fonts/fontmap2 file"
%{_bindir}/gnome-font-install \
	--aliases=%{_org_datadir}/gnome/fonts/adobe-urw.font \
	--target=%{_datadir}/fonts/fontmap2 \
	--recursive \
	--clean \
	%{_datadir}/fonts/Type1 \
	%{_datadir}/fonts/TTF

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%ghost %{_fonts_dir}/fontmap2
%{_datadir}/gnome-print
%{_org_datadir}/gnome/fonts

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
