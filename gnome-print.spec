Summary:	GNOME print programs
Summary(es):	Sistema de impresión de GNOME
Summary(ko):	GNOME Print - ±×³ðÀ» À§ÇÑ ÀÎ¼â ¶óÀÌºê·¯¸®
Summary(pl):	GNOME print - biblioteki infrastruktury drukowania w ¶rodowisku GNOME
Summary(pt_BR):	O sistema de impressão do GNOME
Summary(ru):	âÉÂÌÉÏÔÅËÉ ÐÅÞÁÔÉ ÄÌÑ GNOME
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ ÄÒÕËÕ ÄÌÑ GNOME
Summary(zh_CN):	GNOME´òÓ¡¹¤¾ß
Name:		gnome-print
Version:	0.37
Release:	6
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	f9e13f4f17b04baceec1cdeed0f88eae
Patch0:		%{name}-gnome-font-install.patch
Patch1:		%{name}-am15.patch
Patch2:		%{name}-ac_fixes.patch
Patch3:		%{name}-am17.patch
Patch4:		%{name}-ft2build_h.patch
Patch5:		%{name}-locale_names.patch
URL:		http://www.levien.com/gnome/print-arch.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.12-3
BuildRequires:	libtool
BuildRequires:	libxml-devel
Requires(post):	/sbin/ldconfig
# for gnome-font-install to work
Requires(post):	gnome-libs
Requires(post):	libxml
# Package ghostscript-fonts-std contains required Type1 fonts
Requires:	ghostscript-fonts-std
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgnomeprint15

%define		_sysconfdir	/etc/X11/GNOME

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

%description -l ru
ðÁËÅÔ gnome-print ÓÏÄÅÒÖÉÔ ÂÉÂÌÉÏÔÅËÉ É ÛÒÉÆÔÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ
ÐÒÏÇÒÁÍÍ, ËÏÔÏÒÙÅ ÐÏÄÄÅÒÖÉ×ÁÀÔ ÐÅÞÁÔØ ÓÒÅÄÓÔ×ÁÍÉ GNOME.

%description -l uk
ðÁËÅÔ gnome-print Í¦ÓÔÉÔØ Â¦ÂÌ¦ÏÔÅËÉ ÔÁ ÛÒÉÆÔÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÐÒÏÇÒÁÍ,
ÑË¦ Ð¦ÄÔÒÉÍÕÀÔØ ÄÒÕË ÚÁÓÏÂÁÍÉ GNOME.

%package devel
Summary:	GNOME print libraries, includes, etc
Summary(es):	Bibliotecas y archivos de inclusión de GNOME print
Summary(ko):	GNOME print¸¦ »ç¿ëÇÏ´Â ÀÀ¿ëÇÁ·Î±×·¥À» °³¹ßÇÏ±â À§ÇÑ ¶óÀÌºê·¯¸®¿Í Çì´õÆÄÀÏ
Summary(pl):	GNOME print - pliki nag³ówkowe itp
Summary(pt_BR):	Bibliotecas e arquivos de inclusão do GNOME print
Summary(ru):	èÅÄÅÒÙ É ÄÒÕÇÉÅ ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ GNOME
Summary(uk):	èÅÄÅÒÉ ÔÁ ¦ÎÛ¦ ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ GNOME
Summary(zh_CN):	GNOME´òÓ¡¹¤¾ß¿ª·¢¿â
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	freetype-devel
Requires:	gdk-pixbuf-devel
Requires:	gnome-libs-devel
Requires:	libxml-devel
Obsoletes:	libgnomeprint15-devel

%description devel
Header files for GNOME print.

%description devel -l es
Este paquete contiene las bibliotecas y los archivos de encabezamiento
que se necesitan para compilar las aplicaciones que usan GNOME print.

%description devel -l pl
Pliki nag³ówkowe itp. do GNOME print.

%description devel -l pt_BR
Esse pacote contém as bibliotecas e os arquivos de cabeçalho
necessários para compilar aplicações que usam o gnome-print.

%description devel -l ru
ðÁËÅÔ gnome-print-devel ×ËÌÀÞÁÅÔ ÈÅÄÅÒÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ
ÐÒÉÌÏÖÅÎÉÊ ÐÏÄ GNOME, ÉÓÐÏÌØÚÕÀÝÉÈ ÓÒÅÄÓÔ×Á ÐÅÞÁÔÉ GNOME.

%description devel -l uk
ðÁËÅÔ gnome-print-devel ×ËÌÀÞÁ¤ ÈÅÄÅÒÉ, ÐÏÔÒ¦ÂÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ,
ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ ÍÏÖÌÉ×ÏÓÔ¦ ÄÒÕËÕ GNOME.

%package static
Summary:	GNOME print static libraries
Summary(es):	Static libraries for gnome-print development
Summary(pl):	Biblioteki statyczne GNOME print
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com o gnome-print
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ ÐÏÄ GNOME
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ð¦Ä GNOME
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
GNOME print static libraries.

%description static -l es
Static libraries for gnome-print development.

%description static -l pl
Biblioteki statyczne z funkcjami do drukowania w GNOME.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com o gnome-print.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ, ÉÓÐÏÌØÚÕÀÝÉÈ
ÓÒÅÄÓÔ×Á ÐÅÞÁÔÉ GNOME.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ ÍÏÖÌÉ×ÏÓÔ¦
ÄÒÕËÕ GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

mv -f po/{no,nb}.po

%build
rm -f missing acinclude.m4
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure  \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aliasdir=%{_datadir}/gnome/fonts \
	mapdir=%{_datadir}/gnome/fonts

install fonts/*.font $RPM_BUILD_ROOT%{_datadir}/gnome/fonts

:> $RPM_BUILD_ROOT%{_fontsdir}/fontmap2

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
echo "Generating %{_datadir}/fonts/fontmap2 file"
%{_bindir}/gnome-font-install \
	--aliases=%{_datadir}/gnome/fonts/adobe-urw.font \
	--target=%{_datadir}/fonts/fontmap2 \
	--recursive \
	--clean \
	%{_datadir}/fonts/Type1 \
	%{_datadir}/fonts/TTF

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%ghost %{_fontsdir}/fontmap2
%{_datadir}/gnome-print
%{_datadir}/gnome/fonts

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/gnome-1.0/libgnomeprint

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
