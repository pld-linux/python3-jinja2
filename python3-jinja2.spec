%bcond_without	doc
%define module jinja2
Summary:	Template engine
Summary(pl.UTF-8):	Silnik szablonów
Name:		python3-%{module}
Version:	2.3.1
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
# Source0-md5:	391c7dd06c62dfe7e30ebaad7af0a401
URL:		http://pypi.python.org/pypi/Jinja2
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
%pyrequires_eq	python3-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small but fast and easy to use stand-alone template engine written
in pure python. Provides a Django inspired non-XML syntax but supports
inline expressions and an optional sandboxed environment.


%description -l pl.UTF-8
Mały ale szybkie i łatwy w użyciu samodzielny silnik szablonów
napisany w czystym Pythonie. Dostarcza podobne do Django, o odmiennej
od XMLa składni i kompliowane do kodu Pythona szablony w opcjonalnie
ograniczonym środowisku.

%prep
%setup -q -n Jinja2-%{version}

%build
%{__python3} setup.py build
%if %{with doc}
cd docs
make html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py3_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO AUTHORS CHANGES
%if %{with doc}
%doc docs/_build/html
%endif
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*Jinja*.egg*
