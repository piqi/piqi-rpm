%global commit ded745779a8216b838302e1e1ae4e5f5adacd3b0
%global shortcommit %(echo %{commit} | cut -c 1-7)

Name:		piqi
Version:	0.6.6
Release:	1%{?dist}
Summary:	Universal schema language for JSON, XML, Protocol Buffers

Group:	Development/Languages

License:	ASL 2.0
URL:		http://piqi.org
Source0:	https://github.com/alavrik/piqi/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4-devel
BuildRequires:	ocaml-findlib

# For building documentation
BuildRequires:	pandoc

# For 'make check'
BuildRequires:	protobuf-devel

%description
Piqi is a universal schema language and a collection of tools built
around it.

The Piqi language can be used to define schemas for JSON, XML, Google
Protocol Buffers and some other data formats.

This package includes "piqi" command-line program that exposes some
of the tools:

- for validating, pretty-printing and converting data between JSON,
  XML, Protocol Buffers and Piq formats.

- for working with the schemas, such as converting definitions between
  Piqi (.piqi) and Protocol Buffes (.proto), and "compiling" Piqi
  definitions into one of the supported portable data representation
  formats (JSON, XML, Protocol Buffers).

Other Piqi sub-projects include:

- A multi-format (JSON, XML, Protocol Buffers) data serialization
  system for Erlang and OCaml.

- Piq -- a human-friendly typed data representation language. It is
  designed to be more convenient for viewing and editing data compared
  to JSON, XML, CSV, S-expressions and other formats.

- Piqi-RPC -- an RPC-over-HTTP system for Erlang. It provides a simple
  way to expose Erlang services via JSON, XML and Protocol Buffers
  over HTTP.

The Piqi project was inspired by Google Protocol Buffers and designed to
be largely compatible with it. Like Protocol Buffers, Piqi relies on
type definitions and supports schema evolution. The main differences is
that Piqi has a richer data model, high-level modules, standard mappings
to JSON and XML, and comes with a powerful data representation format
(Piq). Also, Piqi is a lot more extensible.


%prep
%setup -qn %{name}-%{commit}


%build
export OCAMLPATH=
./configure --prefix=/usr
make deps
make
make doc


%check
. ./setenv.sh
make -C tests


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/piqi
%{_mandir}/man1/piqi.1.gz
%doc doc/*.html


%changelog

* Tue Apr 01 2014 Anton Lavrik <alavrik@piqi.org> 0.6.6-1
- Bump upstream 0.6.5 -> 0.6.6
- Remove piqi.1 manpage installation step as it is now installed as a part of
  "make install"

* Thu Nov 14 2013 Anton Lavrik <alavrik@piqi.org> 0.6.5-2
- Cosmetic changes

* Thu Nov 7 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.5-1
- Bump upstream 0.6.4 -> 0.6.5

* Fri Apr 21 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.4-1
- Bump upstream 0.6.3 -> 0.6.4

* Fri Apr 15 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.3-4
- Stand-alone HTML documentation files

* Fri Apr 15 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.3-3
- Remove patch "default values in record definitions"
- Add documentation
- Add manual page

* Fri Apr 5 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.3-2
- [patch] Default values in record definitions

* Fri Apr 5 2013 Motiejus Jakštys <motiejus.jakstys@spilgames.com> 0.6.3-1
- Initial version with /usr/bin/piqi and /usr/bin/piqic
