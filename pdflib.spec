%define version 2.01
%define name pdflib
Name:		%{name}
Version:	%{version}
Release:	1
License:	GPL
Source:		http://www.ifconnection.de/~tm/pdflib/pdflib-2.01.tar.gz
Patch:		pdflib-2.01.soname.patch
BuildRoot:	/tmp/%{name}-%{version}-root
Packager:	Henrik Seidel <Henrik.Seidel@gmx.de>
Group:		Libraries
Provides:	libpdf2.01.so libpdf.so
Summary:	Portable C library for dynamically generating PDF files.
%description
PDFlib is a C library for generating PDF files. It offers a graphics API 
with support for drawing, text, fonts, images, and hypertext. Call PDFlib 
routines from within your client program and voila: dynamic PDF files! For 
detailed instructions on PDFlib programming and the associated API, see the 
PDFlib Programming Manual, included in PDF format in the PDFlib 
distribution.   

%package devel
Group:		Libraries
Summary:	Header file for pdflib
%description devel
This package contains the files needed for compiling programs using the PDF 
library.   
