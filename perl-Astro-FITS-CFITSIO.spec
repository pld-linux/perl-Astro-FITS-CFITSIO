%include	/usr/lib/rpm/macros.perl
%define		pdir	Astro
%define		pnam	FITS-CFITSIO
Summary:	Astro::FITS::CFITSIO Perl module
Summary(cs):	Modul Astro::FITS::CFITSIO pro Perl
Summary(da):	Perlmodul Astro::FITS::CFITSIO
Summary(de):	Astro::FITS::CFITSIO Perl Modul
Summary(es):	Módulo de Perl Astro::FITS::CFITSIO
Summary(fr):	Module Perl Astro::FITS::CFITSIO
Summary(it):	Modulo di Perl Astro::FITS::CFITSIO
Summary(ja):	Astro::FITS::CFITSIO Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Astro::FITS::CFITSIO ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Astro::FITS::CFITSIO
Summary(pl):	Modu³ Perla Astro::FITS::CFITSIO
Summary(pt):	Módulo de Perl Astro::FITS::CFITSIO
Summary(pt_BR):	Módulo Perl Astro::FITS::CFITSIO
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::CFITSIO
Summary(sv):	Astro::FITS::CFITSIO Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::CFITSIO
Summary(zh_CN):	Astro::FITS::CFITSIO Perl Ä£¿é
Name:		perl-Astro-FITS-CFITSIO
Version:	1.01
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	cfitsio-devel >= 2.400
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Astro::FITS::CFITSIO is a Perl interface to William Pence's cfitsio
subroutine library.

%description -l cs
Modul Astro::FITS::CFITSIO pro Perl.

%description -l da
Perlmodul Astro::FITS::CFITSIO.

%description -l de
Astro::FITS::CFITSIO Perl Modul.

%description -l es
Módulo de Perl Astro::FITS::CFITSIO.

%description -l fr
Module Perl Astro::FITS::CFITSIO.

%description -l it
Modulo di Perl Astro::FITS::CFITSIO.

%description -l ja
Astro::FITS::CFITSIO Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Astro::FITS::CFITSIO ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Astro::FITS::CFITSIO.

%description -l pl
Astro::FITS::CFITSIO jest perlowym interfejsem do biblioteki cfitsio
Williama Pence'a.

%description -l pt
Módulo de Perl Astro::FITS::CFITSIO.

%description -l pt_BR
Módulo Perl Astro::FITS::CFITSIO.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::CFITSIO.

%description -l sv
Astro::FITS::CFITSIO Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Astro::FITS::CFITSIO.

%description -l zh_CN
Astro::FITS::CFITSIO Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE NOTES README TODO announce

%{perl_sitearch}/Astro/FITS
%dir %{perl_sitearch}/auto/Astro/FITS
%dir %{perl_sitearch}/auto/Astro/FITS/CFITSIO
%{perl_sitearch}/auto/Astro/FITS/CFITSIO/CFITSIO.bs
%{perl_sitearch}/auto/Astro/FITS/CFITSIO/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Astro/FITS/CFITSIO/CFITSIO.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/INDEX
%{_examplesdir}/%{name}-%{version}/*.fits.*
