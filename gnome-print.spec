Summary:	GNOME core programs
Summary(pl):	Programy podstawowe GNOME'a 
Name:		gnome-print
Version:	0.2
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		gnome-print-gnome-font-install.patch
Patch1:		gnome-print-DESTDIR.patch
Icon:		gnome-print.gif
URL:		http://www.levien.com/gnome/print-arch.html
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Basic programs and libraries that are virtually required for any GNOME
installation.

GNOME is the GNU Network Object Model Environment. That's a fancy name but
really GNOME is a nice GUI desktop environment. It makes using your
computer easy, powerful, and easy to configure.

%description -l pl
Podstawowe programy i biblioteki, które s± niezbêdne przy ka¿dej instlacji
GNOME.

%package devel
Summary:     	GNOME core libraries, includes, etc
Summary(pl): 	GNOME core - pliki nag³ówkowe, etc
Group:       	X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:    	%{name} = %{version}

%description devel
Header files for gnome-libs.

%description -l pl devel
Pliki nag³ówkowe etc do GNOME core.

%package static
Summary:     	GNOME core static libraries
Summary(pl): 	Biblioteki statyczne GNOME core
Group:       	X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:    	%{name}-devel = %{version}

%description static
GNOME core static libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME \
	--without-included-gettext
make

gzip -9nf AUTHORS ChangeLog NEWS README

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*
/usr/X11R6/share/gnome-print

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/X11R6/lib/lib*.so
%attr(755,root,root) /usr/X11R6/lib/*.sh
/usr/X11R6/include/libgnomeprint

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.a
