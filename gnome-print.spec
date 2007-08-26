Summary:	GNOME print programs
Summary(es.UTF-8):	Sistema de impresión de GNOME
Summary(ko.UTF-8):	GNOME Print - 그놈을 위한 인쇄 라이브러리
Summary(pl.UTF-8):	GNOME print - biblioteki infrastruktury drukowania w środowisku GNOME
Summary(pt_BR.UTF-8):	O sistema de impressão do GNOME
Summary(ru.UTF-8):	Библиотеки печати для GNOME
Summary(uk.UTF-8):	Бібліотеки друку для GNOME
Summary(zh_CN.UTF-8):	GNOME打印工具
Name:		gnome-print
Version:	0.37
Release:	6
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-print/0.37/%{name}-%{version}.tar.bz2
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
Obsoletes:	libgnomeprint15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Basic programs and libraries that are virtually required for any GNOME
installation. GNOME is the GNU Network Object Model Environment.
That's a fancy name but really GNOME is a nice GUI desktop
environment. It makes using your computer easy, powerful, and easy to
configure.

%description -l es.UTF-8
gnome-print incluye las bibliotecas que se necesitan para que los
programas GNOME puedan imprimir.

%description -l pl.UTF-8
GNOME print - biblioteki infrastruktury drukowania w środowisku GNOME.

%description -l pt_BR.UTF-8
O gnome-print inclui as bibliotecas necessárias para que programas
GNOME possam imprimir.

%description -l ru.UTF-8
Пакет gnome-print содержит библиотеки и шрифты, необходимые для
программ, которые поддерживают печать средствами GNOME.

%description -l uk.UTF-8
Пакет gnome-print містить бібліотеки та шрифти, необхідні для програм,
які підтримують друк засобами GNOME.

%package devel
Summary:	GNOME print libraries, includes, etc
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión de GNOME print
Summary(ko.UTF-8):	GNOME print를 사용하는 응용프로그램을 개발하기 위한 라이브러리와 헤더파일
Summary(pl.UTF-8):	GNOME print - pliki nagłówkowe itp
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão do GNOME print
Summary(ru.UTF-8):	Хедеры и другие файлы для разработки приложений GNOME
Summary(uk.UTF-8):	Хедери та інші файли для розробки програм GNOME
Summary(zh_CN.UTF-8):	GNOME打印工具开发库
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	freetype-devel
Requires:	gdk-pixbuf-devel
Requires:	gnome-libs-devel
Requires:	libxml-devel
Obsoletes:	libgnomeprint15-devel

%description devel
Header files for GNOME print.

%description devel -l es.UTF-8
Este paquete contiene las bibliotecas y los archivos de encabezamiento
que se necesitan para compilar las aplicaciones que usan GNOME print.

%description devel -l pl.UTF-8
Pliki nagłówkowe itp. do GNOME print.

%description devel -l pt_BR.UTF-8
Esse pacote contém as bibliotecas e os arquivos de cabeçalho
necessários para compilar aplicações que usam o gnome-print.

%description devel -l ru.UTF-8
Пакет gnome-print-devel включает хедеры, необходимые для разработки
приложений под GNOME, использующих средства печати GNOME.

%description devel -l uk.UTF-8
Пакет gnome-print-devel включає хедери, потрібні для розробки програм,
що використовують можливості друку GNOME.

%package static
Summary:	GNOME print static libraries
Summary(es.UTF-8):	Static libraries for gnome-print development
Summary(pl.UTF-8):	Biblioteki statyczne GNOME print
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com o gnome-print
Summary(ru.UTF-8):	Статические библиотеки для разработки приложений под GNOME
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм під GNOME
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GNOME print static libraries.

%description static -l es.UTF-8
Static libraries for gnome-print development.

%description static -l pl.UTF-8
Biblioteki statyczne z funkcjami do drukowania w GNOME.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com o gnome-print.

%description static -l ru.UTF-8
Статические библиотеки для разработки приложений, использующих
средства печати GNOME.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки програм, що використовують можливості
друку GNOME.

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
rm -f acinclude.m4
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
