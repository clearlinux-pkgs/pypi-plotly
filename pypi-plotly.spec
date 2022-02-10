#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-plotly
Version  : 5.6.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/62/76/a5e28be21a1ee99fefde6ccf7d714d42f885fac0d903b2c3c9ce8275f71b/plotly-5.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/76/a5e28be21a1ee99fefde6ccf7d714d42f885fac0d903b2c3c9ce8275f71b/plotly-5.6.0.tar.gz
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
BuildRequires : pypi(six)
BuildRequires : pypi(tenacity)
BuildRequires : pypi(wheel)

%description
<table>
            <tr>
                <td>Latest Release</td>
                <td>

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
Requires: pypi(six)
Requires: pypi(tenacity)

%description python3
python3 components for the pypi-plotly package.


%prep
%setup -q -n plotly-5.6.0
cd %{_builddir}/plotly-5.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644514564
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-plotly
cp %{_builddir}/plotly-5.6.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-plotly/c340b1b30a740d882e192d6d38588465417cfdc4
cp %{_builddir}/plotly-5.6.0/jupyterlab_plotly/labextension/static/478.8d7dac7cd42ef2fc1360.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-plotly/502fa657dd5f79d91bf30b9683e9df3562405e51
cp %{_builddir}/plotly-5.6.0/jupyterlab_plotly/nbextension/index.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-plotly/f3e379e00b9963b93f1e16ac14cb1866635caed5
cp %{_builddir}/plotly-5.6.0/recipe/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-plotly/c340b1b30a740d882e192d6d38588465417cfdc4
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/etc/jupyter/nbconfig/notebook.d/jupyterlab-plotly.json

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/labextensions/jupyterlab-plotly/package.json
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/133.0099ada2d4521140e754.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/423.8409ad662b0daea3de31.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/478.8d7dac7cd42ef2fc1360.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/478.8d7dac7cd42ef2fc1360.js.LICENSE.txt
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/486.52aa9063b291ec574154.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/486.52aa9063b291ec574154.js.LICENSE.txt
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/657.1d0f2334e566f6677fe2.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/879.f9562768266c9160e2f2.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/remoteEntry.f372bf1de02fb50ae6e0.js
/usr/share/jupyter/labextensions/jupyterlab-plotly/static/style.js
/usr/share/jupyter/nbextensions/jupyterlab-plotly/extension.js
/usr/share/jupyter/nbextensions/jupyterlab-plotly/index.js
/usr/share/jupyter/nbextensions/jupyterlab-plotly/index.js.LICENSE.txt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-plotly/502fa657dd5f79d91bf30b9683e9df3562405e51
/usr/share/package-licenses/pypi-plotly/c340b1b30a740d882e192d6d38588465417cfdc4
/usr/share/package-licenses/pypi-plotly/f3e379e00b9963b93f1e16ac14cb1866635caed5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
