Summary:	GNOME print programs
Summary(es):	Sistema de impresi�n de GNOME
Summary(ko):	GNOME Print - �׳��� ���� �μ� ���̺귯��
Summary(pl):	GNOME print - biblioteki infrastruktury drukowania w �rodowisku GNOME
Summary(pt_BR):	O sistema de impress�o do GNOME
Summary(ru):	���������� ������ ��� GNOME
Summary(uk):	��̦����� ����� ��� GNOME
Summary(zh_CN):	GNOME��ӡ����
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
GNOME print - biblioteki infrastruktury drukowania w �rodowisku GNOME.

%description -l pt_BR
O gnome-print inclui as bibliotecas necess�rias para que programas
GNOME possam imprimir.

%description -l ru
����� gnome-print �������� ���������� � ������, ����������� ���
��������, ������� ������������ ������ ���������� GNOME.

%description -l uk
����� gnome-print ͦ����� ¦�̦����� �� ������, ����Ȧ�Φ ��� �������,
�˦ Ц��������� ���� �������� GNOME.

%package devel
Summary:	GNOME print libraries, includes, etc
Summary(es):	Bibliotecas y archivos de inclusi�n de GNOME print
Summary(ko):	GNOME print�� ����ϴ� �������α׷��� �����ϱ� ���� ���̺귯���� �������
Summary(pl):	GNOME print - pliki nag��wkowe itp
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o do GNOME print
Summary(ru):	������ � ������ ����� ��� ���������� ���������� GNOME
Summary(uk):	������ �� ��ۦ ����� ��� �������� ������� GNOME
Summary(zh_CN):	GNOME��ӡ���߿�����
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
Pliki nag��wkowe itp. do GNOME print.

%description devel -l pt_BR
Esse pacote cont�m as bibliotecas e os arquivos de cabe�alho
necess�rios para compilar aplica��es que usam o gnome-print.

%description devel -l ru
����� gnome-print-devel �������� ������, ����������� ��� ����������
���������� ��� GNOME, ������������ �������� ������ GNOME.

%description devel -l uk
����� gnome-print-devel ������� ������, ���Ҧ�Φ ��� �������� �������,
�� �������������� ��������Ԧ ����� GNOME.

%package static
Summary:	GNOME print static libraries
Summary(es):	Static libraries for gnome-print development
Summary(pl):	Biblioteki statyczne GNOME print
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com o gnome-print
Summary(ru):	����������� ���������� ��� ���������� ���������� ��� GNOME
Summary(uk):	������Φ ¦�̦����� ��� �������� ������� Ц� GNOME
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
GNOME print static libraries.

%description static -l es
Static libraries for gnome-print development.

%description static -l pl
Biblioteki statyczne z funkcjami do drukowania w GNOME.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com o gnome-print.

%description static -l ru
����������� ���������� ��� ���������� ����������, ������������
�������� ������ GNOME.

%description static -l uk
������Φ ¦�̦����� ��� �������� �������, �� �������������� ��������Ԧ
����� GNOME.

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
