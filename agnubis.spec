Summary:	The GNOME presentation tool
Summary(pl.UTF-8):	Narzędzie do prezentacji dla GNOME
Name:		agnubis
Version:	20031120
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.bz2
# Source0-md5:	5b0174a2a987a27fada0e950b3fb4b42
Patch0:		%{name}-gdome-pc.patch
Patch1:		%{name}-paned.patch
Patch2:		%{name}-determinism.patch
URL:		http://www.gnome.org/projects/agnubis/
BuildRequires:	bonobo-activation-devel >= 0.9.8
BuildRequires:	diacanvas-devel >= 0.6.0
BuildRequires:	gal-devel >= 1:0.0.3
BuildRequires:	gdome2-devel >= 0.7.2
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-common
BuildRequires:	gob2 >= 1.99.2
BuildRequires:	gtk+2-devel >= 1:2.0.1
BuildRequires:	intltool >= 0.25
BuildRequires:	libbonobo-devel >= 1.116.0
BuildRequires:	libbonoboui-devel >= 1.116.0
BuildRequires:	libglade2-devel >= 1:1.99.0
BuildRequires:	libgnomecanvas-devel >= 1.114.0
BuildRequires:	libgnomeui-devel >= 1.114.0
BuildRequires:	libtool >= 2:1.4.3
BuildRequires:	pkgconfig >= 1:0.14.0
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Agnubis is the GNOME Presentation Program comparable to such programs
as Microsoft PowerPoint or Corel Present. It has been developed and
designed for the GNOME 2 platform and is created to integrate well
with the rest of the components in the GNOME Office suite.

%description -l pl.UTF-8
Agnubis to program do prezentacji dla GNOME porównywalny do takich
narzędzi jak Microsoft PowerPoint czy Corel Present. Został stworzony
i zaprojektowany dla platformy GNOME 2 i jest tworzony tak, by dobrze
integrował się z resztą komponentów biurowych GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
echo '#' > demos/agn-demo/Makefile.am
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_libdir}/%{name}
# FIXME: we don't want all the stuff
%{_libdir}/lib*
%{_datadir}/%{name}
%{_datadir}/idl/*
# FIXME: not the right place
%{_datadir}/gnome/apps/*/*.desktop
%{_pixmapsdir}/*.???
%{_pixmapsdir}/%{name}
%{_datadir}/gnome-2.0/ui/*
