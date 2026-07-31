%define module keystoneauth1

Name:		python-keystoneauth1
Version:	5.15.0
Release:	1
Summary:	Authentication Library for OpenStack Identity
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/keystoneauth1/
Source0:	https://files.pythonhosted.org/packages/source/k/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Authentication Library for OpenStack Identity.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
