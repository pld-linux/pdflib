Summary:	Portable C library for dynamically generating PDF files.
Name:		pdflib
Version:	2.01
Release:	1
License:	GPL
Group:		Libraries
Source:		http://www.ifconnection.de/~tm/pdflib/pdflib-2.01.tar.gz
Patch:		pdflib-soname.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDFlib is a C library for generating PDF files. It offers a graphics API
with support for drawing, text, fonts, images, and hypertext. Call PDFlib
routines from within your client program and voila: dynamic PDF files! For
detailed instructions on PDFlib programming and the associated API, see the
PDFlib Programming Manual, included in PDF format in the PDFlib
distribution.

%package devel
Summary:	Header file for pdflib
Group:		Libraries

%description devel
This package contains the files needed for compiling programs using the PDF 
library.   

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
install -d $RPM_BUILD_ROOT/usr/{include,lib/perl5/site_perl/i386-linux}
install -d $RPM_BUILD_ROOT/usr/lib/{python,tcl8.0/pdflib}
cd pdflib
/usr/bin/install -c pdflib.h $RPM_BUILD_ROOT/usr/include
/usr/bin/install -c libpdf2.01.so $RPM_BUILD_ROOT/usr/lib
make libpdf2.01.a
/usr/bin/install -c libpdf2.01.a $RPM_BUILD_ROOT/usr/lib
ln -s libpdf2.01.so $RPM_BUILD_ROOT/usr/lib/libpdf.so
cd ../bind/perl
/usr/bin/install -c pdflib.so $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/i386-linux
/usr/bin/install -c pdflib.pm $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/i386-linux
cd ../python
/usr/bin/install -c pdflib.so $RPM_BUILD_ROOT/usr/lib/python
cd ../tcl
/usr/bin/install -c pdflib.so $RPM_BUILD_ROOT/usr/lib/tcl8.0/pdflib
/usr/bin/install -c pkgIndex.tcl $RPM_BUILD_ROOT/usr/lib/tcl8.0/pdflib
cd ../..

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc readme.txt doc/*
/usr/lib/libpdf2.01.so
/usr/lib/libpdf.so
/usr/lib/perl5/site_perl/i386-linux/pdflib.so
/usr/lib/perl5/site_perl/i386-linux/pdflib.pm
/usr/lib/python/pdflib.so
/usr/lib/tcl8.0/pdflib

%files devel
/usr/include/pdflib.h
/usr/lib/libpdf2.01.a
