#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Astro
%define		pnam	FITS-CFITSIO
Summary:	Astro::FITS::CFITSIO - Perl extension for using the cfitsio library
Summary(pl):	Astro::FITS::CFITSIO - rozszerzenie Perla do korzystania z biblioteki cfitsio
Name:		perl-Astro-FITS-CFITSIO
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	97524288840884f27e905026c44c6988
BuildRequires:	cfitsio-devel >= 2.470
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	cfitsio >= 2.470
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Astro::FITS::CFITSIO is a Perl interface to William Pence's cfitsio
subroutine library.
 
This module attempts to provide a wrapper for nearly every cfitsio
routine, while retaining as much cfitsio behavior as possible. As
such, one should be aware that it is still somewhat low-level, in the
sense that handing an array which is not the correct size to a routine
like fits_write_img() may cause SIGSEGVs.

The goal is to eventually use these routines to build a more Perl-like
interface to many common tasks such as reading and writing of images
and ASCII and binary tables.

%description -l pl
Astro::FITS::CFITSIO jest perlowym interfejsem do biblioteki cfitsio
Williama Pence'a.

Ten modu³ jest prób± dostarczenia obudowania dla prawie wszystkich
funkcji cfitsio przy zachowaniu mo¿liwie najbli¿szym cfitsio. Przez to
trzeba mieæ na uwadze, ¿e dostêp jest nieco niskopoziomowy, w tym
sensie, ¿e przekazanie tablicy o z³ym rozmiarze do funkcji typu
fits_write_img() mo¿e powodowaæ SIGSEGV.

Celem autora jest ewentualne wykorzystanie tych funkcji to stworzenia
bardziej perlowego interfejsu do wielu ogólnych zadañ, takich jak
odczyt i zapis obrazów oraz tablic binarnych i ASCII.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE NOTES README TODO announce

%{perl_vendorarch}/Astro/FITS
%dir %{perl_vendorarch}/auto/Astro/FITS
%dir %{perl_vendorarch}/auto/Astro/FITS/CFITSIO
%{perl_vendorarch}/auto/Astro/FITS/CFITSIO/CFITSIO.bs
%{perl_vendorarch}/auto/Astro/FITS/CFITSIO/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Astro/FITS/CFITSIO/CFITSIO.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/INDEX
%{_examplesdir}/%{name}-%{version}/*.fits.*
