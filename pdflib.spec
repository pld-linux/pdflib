# TODO
# - where to install libpdf_java.so? %{_libdir} does not seem to be good
#   choice. BTW what is standard java.library.path in other distros?
# - do we really need to package libpdf_(binding).so.*? libpdf_(binding).so
#   should be enough for python, perl and tcl. -- patch linking with -avoid-version
# - fix install so that executable perms are preserved
#
# Conditional build:
%bcond_without	java	# Java binding

%ifnarch i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine       with_java
%endif

%define		skip_post_check_so	pdflib_pl.so.0.0.0 pdflib_tcl.so.0.0.0 pdflib_py.so.0.0.0

%include	/usr/lib/rpm/macros.perl
Summary:	Portable C library for dynamically generating PDF files
Summary(pl.UTF-8):	Przenośna biblioteka C do dynamicznego generowania plików PDF
Name:		pdflib
Version:	4.0.3
Release:	22
License:	Aladdin Free Public License
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	1b9e0d16f3e695902301aa26b6e92513
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shared-libs.patch
Patch2:		%{name}-perl_paths.patch
Patch3:		%{name}-pdflib_pl_pm_VERSION.patch
Patch4:		%{name}-ac.patch
Patch5:		%{name}-build.patch
Patch6:		%{name}-libpng.patch
URL:		http://www.pdflib.com/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_java:BuildRequires:	jdk >= 1.4}
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
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

%description -l pl.UTF-8
PDFlib to biblioteka w C do generowania plików PDF. Oferuje ona API do
obsługi grafiki ze wsparciem dla rysowania, tekstów, fontów, obrazków
oraz hipertekstu.

%package devel
Summary:	Header file for pdflib
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pdflib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpng-devel >= 1.0.8
Requires:	libtiff-devel

%description devel
This package contains the files needed for compiling programs using
the PDF library.

%description devel -l pl.UTF-8
Pakiet zawiera pliki potrzebne do kompilacji programów używających
biblioteki PDF.

%package static
Summary:	Static pdflib library
Summary(pl.UTF-8):	Statyczna biblioteka pdflib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pdflib library.

%description static -l pl.UTF-8
Statyczna biblioteka pdflib.

%package java
Summary:	Java bindings for pdflib
Summary(pl.UTF-8):	Dowiązania Javy do pdflib
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description java
Java bindings for pdflib.

%description java -l pl.UTF-8
Dowiązania Javy do pdflib.

%package perl
Summary:	Perl bindings for pdflib
Summary(pl.UTF-8):	Dowiązania Perla do pdflib
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pdflib-perl5

%description perl
Perl bindings for pdflib.

%description perl -l pl.UTF-8
Dowiązania Perla do pdflib.

%package tcl
Summary:	Tcl bindings for pdflib
Summary(pl.UTF-8):	Dowiązania Tcl do pdflib
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pdflib-tcl8.0

%description tcl
Tcl bindings for pdflib.

%description tcl -l pl.UTF-8
Dowiązania Tcl dla pdflib.

%package python
Summary:	Python bindings for pdflib
Summary(pl.UTF-8):	Dowiązania pythona dla pdflib
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python
Obsoletes:	pdflib-python1.5

%description python
Python bindings for pdflib.

%description python -l pl.UTF-8
Dowiązania pythona dla pdflib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-cxx \
	--enable-shared-pdflib \
	%{?with_java:--with-java=%{java_home}}%{!?with_java:--without-java} \
	--with-py=%{py_sitedir} \
	--with-pyincl=%{py_incdir} \
	--with-perl=%{__perl} \
	--with-perlincl=%{perl_archlib}/CORE \
	--with-tcl=%{_bindir}/tclsh \
	--with-tclpkg=%{_libdir}/tcl%{tcl_ver} \
	--with-zlib \
	--with-pnglib \
	--with-tifflib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p bind/cpp/pdflib.hpp $RPM_BUILD_ROOT%{_includedir}

%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadir}
cp -p bind/java/pdflib.jar $RPM_BUILD_ROOT%{_javadir}
rm -f $RPM_BUILD_ROOT%{_libdir}/libpdf_java.{la,a}
%endif

rm -f $RPM_BUILD_ROOT{%{perl_vendorarch},%{_libdir}/tcl*/pdflib,%{py_libdir}/lib-dynload}/pdflib*.{la,a}

# ensure soname deps are generated
find $RPM_BUILD_ROOT -name '*.so*' | xargs chmod +x

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	java -p /sbin/ldconfig
%postun	java -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt doc/{changes,compatibility,readme_unix}.txt
%doc doc/aladdin-license.pdf
%attr(755,root,root) %{_libdir}/libpdf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpdf.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/PDFlib-manual.pdf
%attr(755,root,root) %{_bindir}/pdflib-config
%attr(755,root,root) %{_libdir}/libpdf.so
%{_libdir}/libpdf.la
%{_includedir}/pdflib.h
%{_includedir}/pdflib.hpp

%files static
%defattr(644,root,root,755)
%{_libdir}/libpdf.a

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpdf_java.so
%attr(755,root,root) %{_libdir}/libpdf_java.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpdf_java.so.0
%{_javadir}/pdflib.jar
%endif

%files perl
%defattr(644,root,root,755)
%{perl_vendorarch}/pdflib_pl.pm
%attr(755,root,root) %{perl_vendorarch}/pdflib_pl.so*

%files tcl
%defattr(644,root,root,755)
%dir %{_libdir}/tcl*/pdflib
%attr(755,root,root) %{_libdir}/tcl*/pdflib/pdflib_tcl.so*
%{_libdir}/tcl*/pdflib/pkgIndex.tcl

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{py_libdir}/lib-dynload/pdflib_py.so*
