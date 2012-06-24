%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	PNG
Summary:	Tk::PNG Perl module - PNG loader for Tk::Photo
Summary(pl):	Modu� Perla Tk::PNG - obs�uga plik�w PNG dla Tk::Photo
Name:		perl-Tk-PNG
Version:	2.005
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	libpng-devel
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk >= 800.005
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::PNG Perl extension which supplies PNG format loader for Photo
image type.

%description -l pl
Rozszerzenie Perla Tk::PNG pozwalaj�ce na odczyt plik�w PNG do typu
obrazu Photo.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%patch -p1
#rm -f jpeg/Makefile.PL

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/Tk/PNG.pm
%dir %{perl_sitearch}/auto/Tk/PNG
%{perl_sitearch}/auto/Tk/PNG/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Tk/PNG/*.so
%{_mandir}/man3/*
