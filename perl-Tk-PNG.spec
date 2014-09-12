#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	PNG
Summary:	Tk::PNG Perl module - PNG loader for Tk::Photo
Summary(pl.UTF-8):	Moduł Perla Tk::PNG - obsługa plików PNG dla Tk::Photo
Name:		perl-Tk-PNG
Version:	2.005
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tk/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe66f970f97775f405db0604a52892cb
URL:		http://search.cpan.org/dist/Tk-PNG/
BuildRequires:	libpng-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Tk-devel >= 800.005
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::PNG Perl extension which supplies PNG format loader for Photo
image type.

%description -l pl.UTF-8
Rozszerzenie Perla Tk::PNG pozwalające na odczyt plików PNG do typu
obrazu Photo.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Tk/PNG.pm
%dir %{perl_vendorarch}/auto/Tk/PNG
%attr(755,root,root) %{perl_vendorarch}/auto/Tk/PNG/*.so
%{_mandir}/man3/*
