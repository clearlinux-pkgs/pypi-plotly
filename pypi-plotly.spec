#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v18
# autospec commit: f35655a
#
Name     : pypi-plotly
Version  : 5.24.0
Release  : 57
URL      : https://files.pythonhosted.org/packages/33/d1/c802129c6e36e32dc549d05008c187c736800be2a521d5d92db9ccf66341/plotly-5.24.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/33/d1/c802129c6e36e32dc549d05008c187c736800be2a521d5d92db9ccf66341/plotly-5.24.0.tar.gz
Summary  : An open-source, interactive data visualization library for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-plotly-data = %{version}-%{release}
Requires: pypi-plotly-license = %{version}-%{release}
Requires: pypi-plotly-python = %{version}-%{release}
Requires: pypi-plotly-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jupyterlab)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# plotly.py
<table>
<tr>
<td>Latest Release</td>
<td>
<a href="https://pypi.org/project/plotly/"/>
<img src="https://badge.fury.io/py/plotly.svg"/>
</td>
</tr>
<tr>
<td>User forum</td>
<td>
<a href="https://community.plotly.com/"/>
<img src="https://img.shields.io/badge/help_forum-discourse-blue.svg"/>
</td>
</tr>
<tr>
<td>PyPI Downloads</td>
<td>
<a href="https://pepy.tech/project/plotly"/>
<img src="https://pepy.tech/badge/plotly/month"/>
</td>
</tr>
<tr>
<td>License</td>
<td>
<a href="https://opensource.org/licenses/MIT"/>
<img src="https://img.shields.io/badge/License-MIT-yellow.svg"/>
</td>
</tr>
</table>

%package data
Summary: data components for the pypi-plotly package.
Group: Data

%description data
data components for the pypi-plotly package.


%package license
Summary: license components for the pypi-plotly package.
Group: Default

%description license
license components for the pypi-plotly package.


%package python
Summary: python components for the pypi-plotly package.
Group: Default
Requires: pypi-plotly-python3 = %{version}-%{release}

%description python
python components for the pypi-plotly package.


%package python3
Summary: python3 components for the pypi-plotly package.
Group: Default
Requires: python3-core
Provides: pypi(plotly)
Requires: pypi(packaging)
Requires: pypi(tenacity)

%description python3
python3 components for the pypi-plotly package.


%prep
%setup -q -n plotly-5.24.0
cd %{_builddir}/plotly-5.24.0
pushd ..
cp -a plotly-5.24.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724965620
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-plotly
cp %{_builddir}/plotly-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-plotly/c340b1b30a740d882e192d6d38588465417cfdc4 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/etc/jupyter/nbconfig/notebook.d/jupyterlab-plotly.json
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/labextensions/jupyterlab-plotly/package.json
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/133.646c4ca84bf565e49a67.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/423.d0d3e2912c33c7566484.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/478.7f92220703a7ef35bd60.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/478.7f92220703a7ef35bd60.js.LICENSE.txt
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/486.6450efe6168c2f8caddb.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/486.6450efe6168c2f8caddb.js.LICENSE.txt
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/657.9b9bb7c49771a02e6168.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/855.323c80e7298812d692e7.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/remoteEntry.41e12212782f05d7d17b.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/style.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/third-party-licenses.json
/usr/share/jupyter/nbextensions/jupyterlab-plotly/extension.js
/usr/share/jupyter/nbextensions/jupyterlab-plotly/index.js
/usr/share/jupyter/nbextensions/jupyterlab-plotly/index.js.LICENSE.txt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-plotly/c340b1b30a740d882e192d6d38588465417cfdc4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
