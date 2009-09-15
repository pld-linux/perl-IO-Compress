#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Compress
Summary:	IO::Compress - Base Class for IO::Compress modules
Summary(pl.UTF-8):	IO::Compress - klasa bazowa dla modułów IO::Compress
Name:		perl-IO-Compress
Version:	2.021
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	126adb25479f656a2907ec7f40249c0a
URL:		http://search.cpan.org/dist/IO-Compress/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?with_tests}
BuildRequires:	perl(Compress::Raw::Bzip2) >= 2.021
BuildRequires:	perl(Compress::Raw::Zlib) >= 2.021
%endif
Obsoletes:	perl-Compress-Zlib
Obsoletes:	perl-IO-Compress-Base
Obsoletes:	perl-IO-Compress-Zlib
Obsoletes:	perl-IO-Compress-Bzip2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is not intended for direct use in application code. Its
sole purpose if to to be sub-classed by IO::Compress and
IO::Uncompress modules.

%description -l pl.UTF-8
Ten moduł nie jest przeznaczony do bezpośredniego użycia w
aplikacjach. Jedynym jego celem jest tworzenie podklas w modułach
IO::Compress i IO::Uncompress.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	INST_LIB=blib/lib
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/IO/{Compress,Uncompress}/Adapter

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Compress/Zlib.pm
%{perl_vendorlib}/File/GlobMapper.pm
%dir %{perl_vendorlib}/IO/Compress
%{perl_vendorlib}/IO/Compress/*.pm
%dir %{perl_vendorlib}/IO/Compress/Adapter
%{perl_vendorlib}/IO/Compress/Adapter/*.pm
%dir %{perl_vendorlib}/IO/Compress/Base
%{perl_vendorlib}/IO/Compress/Base/Common.pm
%dir %{perl_vendorlib}/IO/Compress/Gzip
%{perl_vendorlib}/IO/Compress/Gzip/Constants.pm
%dir %{perl_vendorlib}/IO/Compress/Zip
%{perl_vendorlib}/IO/Compress/Zip/Constants.pm
%dir %{perl_vendorlib}/IO/Compress/Zlib
%{perl_vendorlib}/IO/Compress/Zlib/*.pm
%dir %{perl_vendorlib}/IO/Uncompress
%{perl_vendorlib}/IO/Uncompress/*.pm
%dir %{perl_vendorlib}/IO/Uncompress/Adapter
%{perl_vendorlib}/IO/Uncompress/Adapter/*.pm
%{_mandir}/man3/*
