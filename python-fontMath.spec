#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Set of objects for performing math operations on font data
Summary(pl.UTF-8):	Zbiór obiektów do wykonywania operacji matematycznych na danych fontów
Name:		python-fontMath
Version:	0.8.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/fontpens/
Source0:	https://files.pythonhosted.org/packages/source/f/fontmath/fontMath-%{version}.zip
# Source0-md5:	86560af85a530245e456835b37994a16
URL:		https://pypi.org/project/fontmath/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-fonttools >= 3.32.0
BuildRequires:	python-pytest >= 3.0.3
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-fonttools >= 3.32.0
BuildRequires:	python3-pytest >= 3.0.3
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of objects that implement fast font, glyph, etc. math.

%description -l pl.UTF-8
Zbiór obiektów implementujących szybkie operacje matematyczne na
fontach, glifach itp.

%package -n python3-fontMath
Summary:	Set of objects for performing math operations on font data
Summary(pl.UTF-8):	Zbiór obiektów do wykonywania operacji matematycznych na danych fontów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-fontMath
A collection of objects that implement fast font, glyph, etc. math.

%description -n python3-fontMath -l pl.UTF-8
Zbiór obiektów implementujących szybkie operacje matematyczne na
fontach, glifach itp.

%prep
%setup -q -n fontMath-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest Lib/fontMath
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest Lib/fontMath
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/fontMath/test
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/fontMath/test
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc License.txt README.md
%{py_sitescriptdir}/fontMath
%{py_sitescriptdir}/fontMath-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-fontMath
%defattr(644,root,root,755)
%doc License.txt README.md
%{py3_sitescriptdir}/fontMath
%{py3_sitescriptdir}/fontMath-%{version}-py*.egg-info
%endif
