
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.python

Summary:	Portable C library for dynamically generating PDF files
Summary(pl):	Przeno¶na biblioteka C do dynamicznej generacji plików PDF
Name:		pdflib
Version:	4.0.2
Release:	1
License:	Alladin Free Public License
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Aðgerðasöfn
Group(it):	Librerie
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(sl):	Knji¾nice
Group(sv):	Bibliotek
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	http://www.pdflib.com/pdflib/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shared-libs.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	tcl-devel
BuildRequires:	zlib-devel
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
PDFlib to biblioteka w C do generowania plików PDF. Oferuje ona API do
obs³ugi grafiki ze wsparciem dla rysowania, tekstów, fontów, obrazków
oraz hipertekstu.

%package devel
Summary:	Header file for pdflib
Summary(pl):	Pliki nag³ówkowe dla %{name}
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
This package contains the files needed for compiling programs using
the PDF library.

%description -l pl devel
Pakiet zawiera pliki potrzebne do kompilacji programów u¿ywaj±cych
biblioteki PDF.

%package perl
Summary:	Perl bindings for pdflib
Summary(pl):	Dowi±zania Perla do pdflib
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	Þróunartól/Forritunarmál/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(no):	Utvikling/Programmeringsspråk/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Språk/Perl
Requires:	%{name} = %{version}
Obsoletes:	%{name}-perl5

%description perl
Perl bindings for pdflib.

%description -l pl perl
Dowi±zania Perla do pdflib.

%package tcl
Summary:	Tcl bindings for pdflib
Summary(pl):	Dowi±zania Tcl do pdflib
Group:		Development/Languages/Tcl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Tcl
Group(da):	Udvikling/Sprog/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(es):	Desarrollo/Lenguajes/Tcl
Group(fr):	Development/Langues/Tcl
Group(is):	Þróunartól/Forritunarmál/Tcl
Group(it):	Sviluppo/Linguaggi/Tcl
Group(ja):	³«È¯/¸À¸ì/Tcl
Group(no):	Utvikling/Programmeringsspråk/Tcl
Group(pl):	Programowanie/Jêzyki/Tcl
Group(pt):	Desenvolvimento/Linguagens/Tcl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Tcl
Group(sl):	Razvoj/Jeziki/Tcl
Group(sv):	Utveckling/Språk/Tcl
Requires:	%{name} = %{version}
Obsoletes:	%{name}-tcl8.0

%description tcl
Tcl bindings for pdflib.

%description -l pl tcl
Dowi±zania TCL dla pdflib.

%package python
Summary:	Python bindings for pdflib
Summary(pl):	Dowi±zania pythona dla pdflib
Group:		Development/Languages/Python
Group(cs):	Vývojové prostøedky/Programovací jazyky/Python
Group(da):	Udvikling/Sprog/Python
Group(de):	Entwicklung/Sprachen/Python
Group(es):	Desarrollo/Lenguajes/Python
Group(fr):	Development/Langues/Python
Group(is):	Þróunartól/Forritunarmál/Python
Group(it):	Sviluppo/Linguaggi/Python
Group(ja):	³«È¯/¸À¸ì/Python
Group(no):	Utvikling/Programmeringsspråk/Python
Group(pl):	Programowanie/Jêzyki/Python
Group(pt):	Desenvolvimento/Linguagens/Python
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Python
Group(sl):	Razvoj/Jeziki/Python
Group(sv):	Utveckling/Språk/Python
Requires:	%{name} = %{version}
%requires_eq	python
Obsoletes:	%{name}-python1.5

%description python
Python bindings for pdflib.

%description -l pl python
Dowi±zania pythona dla pdflib.

%package static
Summary:	Static libraries for pdflib
Summary(pl):	Statyczna biblioteka pdflib
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
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
	--with-py=%{py_sitedir} --with-pyincl=%{py_incdir} \
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
%attr(755,root,root) %{py_libdir}/lib-dynload/pdflib_py.so.*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpdf.a
%{perl_sitearch}/pdflib_pl.a
%{_libdir}/tcl*/pdflib/pdflib_tcl.a
%{py_libdir}/lib-dynload/pdflib_py.a
