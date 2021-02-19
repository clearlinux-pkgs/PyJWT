#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyJWT
Version  : 2.0.1
Release  : 51
URL      : https://files.pythonhosted.org/packages/ef/68/d610e2e10bc8336a033a6e0f0401341106ee9ed9cb0c1571b0d1a8eacf39/PyJWT-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/68/d610e2e10bc8336a033a6e0f0401341106ee9ed9cb0c1571b0d1a8eacf39/PyJWT-2.0.1.tar.gz
Summary  : JSON Web Token implementation in Python
Group    : Development/Tools
License  : MIT
Requires: PyJWT-license = %{version}-%{release}
Requires: PyJWT-python = %{version}-%{release}
Requires: PyJWT-python3 = %{version}-%{release}
Requires: cryptography
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-runner
BuildRequires : tox
BuildRequires : virtualenv

%description
=====

%package license
Summary: license components for the PyJWT package.
Group: Default

%description license
license components for the PyJWT package.


%package python
Summary: python components for the PyJWT package.
Group: Default
Requires: PyJWT-python3 = %{version}-%{release}
Provides: pyjwt-python

%description python
python components for the PyJWT package.


%package python3
Summary: python3 components for the PyJWT package.
Group: Default
Requires: python3-core
Provides: pypi(pyjwt)

%description python3
python3 components for the PyJWT package.


%prep
%setup -q -n PyJWT-2.0.1
cd %{_builddir}/PyJWT-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610998271
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyJWT
cp %{_builddir}/PyJWT-2.0.1/LICENSE %{buildroot}/usr/share/package-licenses/PyJWT/bc48b3f80bfc08458a1f78bb2b49c6de2b41010f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyJWT/bc48b3f80bfc08458a1f78bb2b49c6de2b41010f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
