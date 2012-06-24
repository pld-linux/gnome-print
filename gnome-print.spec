Summary:	GNOME print programs
Summary(pl):	Programy podstawowe GNOME'a 
Name:		gnome-print
Version:	0.10
Release:	1
License:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		gnome-print-gnome-font-install.patch
Icon:		gnome-print.gif
URL:		http://www.levien.com/gnome/print-arch.html
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
Basic programs and libraries that are virtually required for any GNOME
installation.  GNOME is the GNU Network Object Model Environment. That's a
fancy name but really GNOME is a nice GUI desktop environment. It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Podstawowe programy i biblioteki, kt�re s� niezb�dne przy ka�dej instlacji
GNOME.

%package devel
Summary:	GNOME print libraries, includes, etc
Summary(pl):	GNOME print - pliki nag��wkowe, etc
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for gnome-libs.

%description -l pl devel
Pliki nag��wkowe etc do GNOME core.

%package static
Summary:	GNOME print static libraries
Summary(pl):	Biblioteki statyczne GNOME print
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME print static libraries.

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
make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_prefix}/lib/lib*.so.*.*

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
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
