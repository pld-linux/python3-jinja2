#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests

%define		module	jinja2
Summary:	Template engine Jinja2 for Python 3.x
Summary(pl.UTF-8):	Silnik szablonów Jinja2 dla Pythona 3.x
Name:		python3-%{module}
Version:	3.1.6
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/Jinja2
Source0:	https://files.pythonhosted.org/packages/source/J/Jinja2/jinja2-%{version}.tar.gz
# Source0-md5:	66d4c25ff43d1deaf9637ccda523dec8
URL:		https://jinja.palletsprojects.com/en/3.1.x/
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
%if %{with tests}
BuildRequires:	python3-babel >= 2.7
BuildRequires:	python3-markupsafe >= 2.0
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-trio
%endif
%if %{with doc}
BuildRequires:	python3-pallets-sphinx-themes >= 1.2.0
BuildRequires:	python3-sphinxcontrib-log-cabinet >= 1.0.1
BuildRequires:	python3-sphinx_issues >= 1.2.0
BuildRequires:	sphinx-pdg-3 >= 2.1.2
%endif
BuildArch:	noarch
Requires:	python3-modules >= 1:3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small but fast and easy to use stand-alone template engine written
in pure Python. Provides a Django inspired non-XML syntax but supports
inline expressions and an optional sandboxed environment.

%description -l pl.UTF-8
Mały ale szybki i łatwy w użyciu samodzielny silnik szablonów napisany
w czystym Pythonie. Udostępnia podobne do Django, o odmiennej od XML-a
składni i kompilowane do kodu Pythona szablony w opcjonalnie
ograniczonym środowisku.

%package apidoc
Summary:	Jinja2 template engine API documentation
Summary(pl.UTF-8):	Dokumentacja API silnika szablonów Jinja2
Group:		Development/Languages/Python

%description apidoc
API documentation for Jinja2 template engine.

%description apidoc -l pl.UTF-8
Dokumentacja API silnika szablonów Jinja2.

%prep
%setup -q -n jinja2-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs -j1 html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/jinja2-%{version}.dist-info

%if %{with doc}
%files apidoc
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
