%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	PNG
Summary:	Tk::PNG Perl module - PNG loader for Tk::Photo
Summary(pl):	Modu³ Perla Tk::PNG - obs³uga plików PNG dla Tk::Photo
Name:		perl-Tk-PNG
Version:	2.005
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	libpng-devel
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk >= 800.005
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::PNG Perl extension which supplies PNG format loader for Photo
image type.

%description -l pl
Rozszerzenie Perla Tk::PNG pozwalaj±ce na odczyt plików PNG do typu
obrazu Photo.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%patch -p1
#rm -f jpeg/Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
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
%{perl_vendorarch}/Tk/PNG.pm
%dir %{perl_vendorarch}/auto/Tk/PNG
%{perl_vendorarch}/auto/Tk/PNG/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Tk/PNG/*.so
%{_mandir}/man3/*
