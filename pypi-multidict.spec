#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-multidict
Version  : 6.0.4
Release  : 56
URL      : https://files.pythonhosted.org/packages/4a/15/bd620f7a6eb9aa5112c4ef93e7031bcd071e0611763d8e17706ef8ba65e0/multidict-6.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/4a/15/bd620f7a6eb9aa5112c4ef93e7031bcd071e0611763d8e17706ef8ba65e0/multidict-6.0.4.tar.gz
Summary  : multidict implementation
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-multidict-filemap = %{version}-%{release}
Requires: pypi-multidict-lib = %{version}-%{release}
Requires: pypi-multidict-license = %{version}-%{release}
Requires: pypi-multidict-python = %{version}-%{release}
Requires: pypi-multidict-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=========
multidict
=========
.. image:: https://github.com/aio-libs/multidict/workflows/CI/badge.svg
:target: https://github.com/aio-libs/multidict/actions?query=workflow%3ACI
:alt: GitHub status for master branch

%package filemap
Summary: filemap components for the pypi-multidict package.
Group: Default

%description filemap
filemap components for the pypi-multidict package.


%package lib
Summary: lib components for the pypi-multidict package.
Group: Libraries
Requires: pypi-multidict-license = %{version}-%{release}
Requires: pypi-multidict-filemap = %{version}-%{release}

%description lib
lib components for the pypi-multidict package.


%package license
Summary: license components for the pypi-multidict package.
Group: Default

%description license
license components for the pypi-multidict package.


%package python
Summary: python components for the pypi-multidict package.
Group: Default
Requires: pypi-multidict-python3 = %{version}-%{release}

%description python
python components for the pypi-multidict package.


%package python3
Summary: python3 components for the pypi-multidict package.
Group: Default
Requires: pypi-multidict-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(multidict)

%description python3
python3 components for the pypi-multidict package.


%prep
%setup -q -n multidict-6.0.4
cd %{_builddir}/multidict-6.0.4
pushd ..
cp -a multidict-6.0.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672291107
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-multidict
cp %{_builddir}/multidict-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-multidict/02821ffe00e8c771ad89722cbe98e5d74ba36369 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-multidict

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-multidict/02821ffe00e8c771ad89722cbe98e5d74ba36369

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
