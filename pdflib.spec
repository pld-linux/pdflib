
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.python

Summary:	Portable C library for dynamically generating PDF files
Summary(pl):	Przeno�na biblioteka C do dynamicznego generowania plik�w PDF
Name:		pdflib
Version:	4.0.3
Release:	8
License:	Aladdin Free Public License
Group:		Libraries
Source0:	http://www.pdflib.com/pdflib/download/%{name}-%{version}.tar.gz
# Source0-md5: 1b9e0d16f3e695902301aa26b6e92513
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shared-libs.patch
Patch2:		%{name}-perl_paths.patch
Patch3:		%{name}-pdflib_pl_pm_VERSION.patch
URL:		http://www.pdflib.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 0:1.4.2-9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	tcl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define tcl_ver %(echo `echo "puts [info tclversion]" | tclsh`)

%description
PDFlib is a C library for generating PDF files. It offers a graphics
API with support for drawing, text, fonts, images, and hypertext. Call
PDFlib routines from within your client program and voila: dynamic PDF
files! For detailed instructions on PDFlib programming and the
associated API, see the PDFlib Programming Manual, included in PDF
format in the PDFlib distribution.

%description -l pl
PDFlib to biblioteka w C do generowania plik�w PDF. Oferuje ona API do
obs�ugi grafiki ze wsparciem dla rysowania, tekst�w, font�w, obrazk�w
oraz hipertekstu.

%package devel
Summary:	Header file for pdflib
Summary(pl):	Pliki nag��wkowe dla %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the files needed for compiling programs using
the PDF library.

%description devel -l pl
Pakiet zawiera pliki potrzebne do kompilacji program�w u�ywaj�cych
biblioteki PDF.

%package perl
Summary:	Perl bindings for pdflib
Summary(pl):	Dowi�zania Perla do pdflib
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Provides:	perl(pdflib_pl) = 4.0
Obsoletes:	%{name}-perl5

%description perl
Perl bindings for pdflib.

%description perl -l pl
Dowi�zania Perla do pdflib.

%package tcl
Summary:	Tcl bindings for pdflib
Summary(pl):	Dowi�zania Tcl do pdflib
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-tcl8.0

%description tcl
Tcl bindings for pdflib.

%description tcl -l pl
Dowi�zania TCL dla pdflib.

%package python
Summary:	Python bindings for pdflib
Summary(pl):	Dowi�zania pythona dla pdflib
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python
Obsoletes:	%{name}-python1.5

%description python
Python bindings for pdflib.

%description python -l pl
Dowi�zania pythona dla pdflib.

%package static
Summary:	Static libraries for pdflib
Summary(pl):	Statyczna biblioteka pdflib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for pdflib.

%description static -l pl
Statyczna biblioteka pdflib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} --output=config/aclocal.m4
%{__autoconf}
%configure \
	--enable-cxx \
	--enable-shared-pdflib \
	--with-py=%{py_sitedir} --with-pyincl=%{py_incdir} \
	--with-perl=%{__perl} \
	--with-perlincl=%{perl_archlib}/CORE \
	--with-tcl=%{_bindir}/tclsh \
	--with-tclpkg=%{_libdir}/tcl%{tcl_ver} \
	--with-zlib \
	--with-pnglib \
	--with-tifflib

%{__make} CPPFLAGS="$CPPFLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ./bind/cpp/pdflib.hpp $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt doc/{changes,compatibility,readme_unix}.txt
%doc doc/aladdin-license.pdf
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/PDFlib-manual.pdf
%attr(755,root,root) %{_bindir}/pdflib-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/pdflib.h
%{_includedir}/pdflib.hpp

%files perl
%defattr(644,root,root,755)
%{perl_vendorarch}/pdflib_pl.pm
%attr(755,root,root) %{perl_vendorarch}/pdflib_pl.so*

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tcl*/pdflib/pdflib_tcl.so.*
%{_libdir}/tcl*/pdflib/pkgIndex.tcl

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{py_libdir}/lib-dynload/pdflib_py.so.*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpdf.a
%{perl_vendorarch}/pdflib_pl.a
%{_libdir}/tcl*/pdflib/pdflib_tcl.a
%{py_libdir}/lib-dynload/pdflib_py.a
