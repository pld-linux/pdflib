Summary:	Portable C library for dynamically generating PDF files
Name:		pdflib
Version:	2.01
Release:	1
License:	GPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.ifconnection.de/~tm/pdflib/%{name}-%{version}.tar.gz
Patch0:		pdflib-soname.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDFlib is a C library for generating PDF files. It offers a graphics
API with support for drawing, text, fonts, images, and hypertext. Call
PDFlib routines from within your client program and voila: dynamic PDF
files! For detailed instructions on PDFlib programming and the
associated API, see the PDFlib Programming Manual, included in PDF
format in the PDFlib distribution.

%package devel
Summary:	Header file for pdflib
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki

%description devel
This package contains the files needed for compiling programs using
the PDF library.

%prep
%setup -q
%patch -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,lib/perl5/site_perl/i386-linux} \
	$RPM_BUILD_ROOT%{_libdir}/{python,tcl8.0/pdflib}

cd pdflib
install -c pdflib.h $RPM_BUILD_ROOT%{_includedir}
install -c libpdf2.01.so $RPM_BUILD_ROOT%{_libdir}
%{__make} libpdf2.01.a
install -c libpdf2.01.a $RPM_BUILD_ROOT%{_libdir}
ln -s libpdf2.01.so $RPM_BUILD_ROOT%{_libdir}/libpdf.so
cd ../bind/perl
install -c pdflib.so $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl/i386-linux
install -c pdflib.pm $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl/i386-linux
cd ../python
install -c pdflib.so $RPM_BUILD_ROOT%{_libdir}/python
cd ../tcl
install -c pdflib.so $RPM_BUILD_ROOT%{_libdir}/tcl8.0/pdflib
install -c pkgIndex.tcl $RPM_BUILD_ROOT%{_libdir}/tcl8.0/pdflib
cd ../..

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt doc/*
%{_libdir}/libpdf2.01.so
%{_libdir}/libpdf.so
%{_libdir}/perl5/site_perl/i386-linux/pdflib.so
%{_libdir}/perl5/site_perl/i386-linux/pdflib.pm
%{_libdir}/python/pdflib.so
%{_libdir}/tcl8.0/pdflib

%files devel
%defattr(644,root,root,755)
%{_includedir}/pdflib.h
%{_libdir}/libpdf2.01.a
