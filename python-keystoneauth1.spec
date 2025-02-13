Name:		python-keystoneauth1
Version:	5.9.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/k/keystoneauth1/keystoneauth1-%{version}.tar.gz
Summary:	Authentication Library for OpenStack Identity
URL:		https://pypi.org/project/keystoneauth1/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pbr)
BuildSystem:	python
BuildArch:	noarch

%description
Authentication Library for OpenStack Identity

%files
%{py_sitedir}/keystoneauth1
%{py_sitedir}/keystoneauth1-*.*-info
