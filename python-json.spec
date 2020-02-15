%define upstream_name python-json
%define upstream_version 3_4

Name:           python-json
Version:        3.4
Release:        12
Summary:        JSON reader and writer in Python
Group:          Development/Python
License:        LGPL
URL:            http://sourceforge.net/projects/json-py/
Source0:        http://sourceforge.net/projects/json-py/files/json-py/3_4/json-py-%{upstream_version}.zip
BuildArch:      noarch

%description
json.py is an implementation of a JSON (http://json.org) reader
and writer in Python.

#------------------------------------------------

%package -n     python2-json
Summary:        JSON reader and writer in Python 2
Group:          Development/Python
BuildArch:      noarch
BuildRequires:	pkgconfig(python2)

Obsoletes:      python-json < 3.4-9
Provides:       python-json = %{version}-%{release}
Provides:       pythonegg(2)(json) = %{version}-%{release}

%description -n python2-json
json.py is an implementation of a JSON (http://json.org) reader
and writer in Python 2.

#------------------------------------------------

%prep
%setup -q -c
chmod 644 *.txt

%build

%install
install -D -m 644 json.py %{buildroot}%{python2_sitelib}/json.py

%files -n python2-json
%doc *.txt
%{python2_sitelib}/json.py*
