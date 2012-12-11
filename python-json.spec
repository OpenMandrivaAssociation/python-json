Name:           python-json
Version:        3.4
%define version_munge %(sed 's/\\./_/g' <<< %{version})
Release:        %mkrel 3
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



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 3.4-3mdv2010.0
+ Revision: 442198
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 3.4-2mdv2009.1
+ Revision: 323733
- rebuild

* Mon Nov 10 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 3.4-1mdv2009.1
+ Revision: 301831
- import python-json


* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 3.4-4
- fix license tag

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> 3.4-3
- Rebuild for python 2.5

* Fri Sep  8 2006 Luke Macken <lmacken@redhat.com> 3.4-2
- Rebuild for FC6

* Fri Dec 30 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 3.4-1
- Initial RPM release
