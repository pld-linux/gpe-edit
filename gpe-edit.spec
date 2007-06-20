Summary:	GPE editor
Summary(pl.UTF-8):	Edytor GPE
Name:		gpe-edit
Version:	0.40
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	26bca78fb1619de3a36b6b242997339b
Source1:	%{name}.pl.po
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	intltool >= 0.23
BuildRequires:	libgpewidget-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE text editor, for embedded devices.

%description -l pl.UTF-8
Edytor tekstu GPE dla urządzeń wbudowanych.

%prep
%setup -q

cp %{SOURCE1} po/pl.po
sed -i -e 's/nl pt_BR/nl pl pt_BR/' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/gpe-edit.html
%attr(755,root,root) %{_bindir}/gpe-edit
%{_sysconfdir}/mime-handlers/gpe-edit.mime
%{_datadir}/application-registry/gpe-edit.applications
%{_desktopdir}/gpe-edit.desktop
%{_pixmapsdir}/gpe-edit.png
