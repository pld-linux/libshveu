Summary:	Library for controlling SH-Mobile VEU (Video Engine Unit)
Summary(pl.UTF-8):	Biblioteka do sterowania układem SH-Mobile VEU (Video Engine Unit)
Name:		libshveu
Version:	1.5.2
Release:	1
License:	LGPL v2+
Group:		Libraries
# trailing /%{name}-%{version}.tar.gz is a hack for df
Source0:	https://oss.renesas.com/modules/document/gate.php/?way=attach&refer=libshveu&openfile=%{name}-%{version}.tar.gz/%{name}-%{version}.tar.gz
# Source0-md5:	2196c0ca54ed0a90ba489e774329b0ac
Patch0:		%{name}-link.patch
URL:		https://oss.renesas.com/modules/document/?libshveu
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	libuiomux-devel >= 1.5.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
Requires:	libuiomux >= 1.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libshveu is a library for controlling SH-Mobile VEU (Video Engine
Unit). VEU handles colorspace conversion, rotation and scaling.

%description -l pl.UTF-8
Biblioteka do sterowania układem SH-Mobile VEU (Video Engine Unit).
VEU obsługuje konwersję przestrzeni kolorów oraz obracanie i
skalowanie obrazu.

%package devel
Summary:	Header files for libshveu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libshveu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libuiomux-devel >= 1.5.0

%description devel
Header files for libshveu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libshveu.

%package static
Summary:	Static libshveu library
Summary(pl.UTF-8):	Statyczna biblioteka libshveu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libshveu library.

%description static -l pl.UTF-8
Statyczna biblioteka libshveu.

%package apidocs
Summary:	libshveu API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libshveu
Group:		Documentation

%description apidocs
API and internal documentation for libshveu library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libshveu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	ncurses_lib="-lncurses -ltinfo"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig (with link patch)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libshveu.la
# HTML packaged in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libshveu

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/shveu-convert
%attr(755,root,root) %{_bindir}/shveu-display
%attr(755,root,root) %{_libdir}/libshveu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libshveu.so.3
%{_mandir}/man1/shveu-convert.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libshveu.so
%{_includedir}/shveu
%{_pkgconfigdir}/shveu.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libshveu.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/libshveu/html/*
