Summary:	GPE editor
Summary(pl.UTF-8):	Edytor GPE
Name:		gpe-edit
Version:	0.40
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	26bca78fb1619de3a36b6b242997339b
URL:		http://gpe.linuxtogo.org/
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libgpewidget-devel
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE text editor, for embedded devices.

%description -l pl.UTF-8
Edytor tekstu GPE dla urządzeń wbudowanych.

%prep
%setup -q

%build
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
%{_sysconfdir}/mime-handlers/gpe-edit.mime
%attr(755,root,root) %{_bindir}/gpe-edit
%{_datadir}/application-registry/gpe-edit.applications
%{_desktopdir}/gpe-edit.desktop
%{_pixmapsdir}/gpe-edit.png
