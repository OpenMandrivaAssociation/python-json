Name:           python-json
Version:        3.4
%define version_munge %(sed 's/\\./_/g' <<< %{version})
Release:        1
Summary:        A JSON reader and writer for Python

Group:          Development/Python
License:        LGPLv2+
URL:            https://sourceforge.net/projects/json-py/
Source0:        http://dl.sourceforge.net/json-py/json-py-%{version_munge}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  python-devel

%description
json.py is an implementation of a JSON (http://json.org) reader and writer in
Python.

%prep
%setup -q -c
chmod a-x *

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}
install -p -m 0644 json.py minjson.py $RPM_BUILD_ROOT%{python_sitelib}
%py_compile $RPM_BUILD_ROOT%{python_sitelib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc changes.txt jsontest.py license.txt readme.txt
%{python_sitelib}/*.py
%{python_sitelib}/*.py[co]

