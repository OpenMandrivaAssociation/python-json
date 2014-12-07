Name:		python-json
Version:	3.4
%define version_munge %(sed 's/\\./_/g' <<< %{version})
Release:	7
Summary:	A JSON reader and writer for Python

Group:		Development/Python
License:	LGPLv2+
URL:		https://sourceforge.net/projects/json-py/
Source0:	http://dl.sourceforge.net/json-py/json-py-%{version_munge}.zip
BuildArch:	noarch
BuildRequires:	python-devel

%description
json.py is an implementation of a JSON (http://json.org) reader and writer in
Python.

%prep
%setup -q -c
chmod a-x *

%build

%install
mkdir -p %{buildroot}%{python_sitelib}
install -p -m 0644 json.py minjson.py %{buildroot}%{python_sitelib}
%py_compile %{buildroot}%{python_sitelib}


%files
%doc changes.txt jsontest.py license.txt readme.txt
%{python_sitelib}/*.py
