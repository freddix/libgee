Summary:	GObject collections library
Name:		libgee
Version:	0.10.4
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgee/0.10/%{name}-%{version}.tar.xz
# Source0-md5:	20e3d082077ce1af2c0446bb2acec9ac
URL:		http://live.gnome.org/Libgee
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	vala
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	0.8

%description
libgee is a collections library providing GObject-based interfaces and
classes for commonly used data structures.

%package devel
Summary:	Header files for libgee library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgee library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgee-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libgee-%{apiver}.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgee-%{apiver}.so
%{_pkgconfigdir}/gee-%{apiver}.pc
%{_includedir}/gee-%{apiver}
%{_datadir}/gir-1.0/Gee-%{apiver}.gir
%{_datadir}/vala/vapi/gee-%{apiver}.vapi

