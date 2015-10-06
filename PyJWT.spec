#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyJWT
Version  : 1.4.0
Release  : 16
URL      : https://pypi.python.org/packages/source/P/PyJWT/PyJWT-1.4.0.tar.gz
Source0  : https://pypi.python.org/packages/source/P/PyJWT/PyJWT-1.4.0.tar.gz
Summary  : JSON Web Token implementation in Python
Group    : Development/Tools
License  : MIT
Requires: PyJWT-bin
Requires: PyJWT-python
BuildRequires : cov-core-python
BuildRequires : coverage-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-cov-python
BuildRequires : pytest-runner
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
# PyJWT
[![travis-status-image]][travis]
[![appveyor-status-image]][appveyor]
[![pypi-version-image]][pypi]
[![coveralls-status-image]][coveralls]

%package bin
Summary: bin components for the PyJWT package.
Group: Binaries

%description bin
bin components for the PyJWT package.


%package python
Summary: python components for the PyJWT package.
Group: Default
Provides: pyjwt-python

%description python
python components for the PyJWT package.


%prep
%setup -q -n PyJWT-1.4.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jwt

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
