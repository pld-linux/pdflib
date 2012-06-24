%include        /usr/lib/rpm/macros.perl

%define python_dir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3])"`)
%define python_include_dir %(echo `python -c "import sys; print (sys.prefix + '/include/python' + sys.version[:3])"`)

Summary:	Portable C library for dynamically generating PDF files
Summary(pl):	Przeno�na biblioteka C do dynamicznej generacji plik�w PDF
Name:		pdflib
Version:	4.0.1
Release:	2
License:	Alladin Free Public License
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Source0:	http://www.pdflib.com/pdflib/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shared-libs.patch
BuildRequires:	python-devel >= 2.1
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	tcl-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
URL:		http://www.pdflib.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
This package contains the files needed for compiling programs using
the PDF library.

%description -l pl devel
Pakiet zawiera pliki potrzebne do kompilacji program�w u�ywaj�cych
biblioteki PDF.

%package perl
Summary:	Perl bindings for pdflib
Summary(pl):	Dowi�zania Perla do pdflib
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Requires:	%{name} = %{version}
Obsoletes:	%{name}-perl5

%description perl
Perl bindings for pdflib.

%description -l pl perl
Dowi�zania Perla do pdflib.

%package tcl
Summary:	Tcl bindings for pdflib
Summary(pl):	Dowi�zania Tcl do pdflib
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Requires:	%{name} = %{version}
Obsoletes:	%{name}-tcl8.0

%description tcl
Tcl bindings for pdflib.

%description -l pl tcl
Dowi�zania TCL dla pdflib.

%package python
Summary:	Python bindings for pdflib
Summary(pl):	Dowi�zania pythona dla pdflib
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	%{name} = %{version}
Obsoletes:	%{name}-python1.5

%description python
Python bindings for pdflib.

%description -l pl python
Dowi�zania pythona dla pdflib.

%package static
Summary:	Static libraries for pdflib
Summary(pl):	Statyczna biblioteka pdflib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Static libraries for pdflib.

%description -l pl static
Statyczna biblioteka pdflib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal --output=config/aclocal.m4
autoconf

%configure \
	--enable-cxx \
	--enable-shared-pdflib \
	--with-py=%{python_dir} --with-pyincl=%{python_include_dir} \
	--with-perl=%{_bindir}/perl \
	--with-tcl=%{_bindir}/tclsh \
	--with-zlib \
	--with-pnglib \
	--with-tifflib
%{__make}
 
%install
rm -rf $RPM_BUILD_ROOT

# arrrghh!!! libtool 1.4 supports linking with non-installed library,
# but without DESTDIR! use hack to avoid "relinking" (which requires
# libpdf already installed in /usr/lib).
for f in bind/{perl/pdflib_pl,python/pdflib_py,tcl/pdflib_tcl}.la ; do
	sed -e '/^relink_command=/d' $f > $f.new
	mv -f $f.new $f
done

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install ./bind/cpp/pdflib.hpp $RPM_BUILD_ROOT%{_includedir}

rm -f doc/readme_{ebcdic,mac,win}.txt
gzip -9nf readme.txt doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/pdflib.h
%{_includedir}/pdflib.hpp

%files perl
%defattr(644,root,root,755)
%{perl_sitearch}/pdflib_pl.pm
%attr(755,root,root) %{perl_sitearch}/pdflib_pl.so*

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tcl*/pdflib/pdflib_tcl.so.*
%{_libdir}/tcl*/pdflib/pkgIndex.tcl

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{python_dir}/lib-dynload/pdflib_py.so.*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpdf.a
%{perl_sitearch}/pdflib_pl.a
%{_libdir}/tcl*/pdflib/pdflib_tcl.a
%{python_dir}/lib-dynload/pdflib_py.a
