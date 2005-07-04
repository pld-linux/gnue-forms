Summary:	GNUe Forms - a data-aware user-interface generator
#Summary(pl):	
Name:		gnue-forms
Version:	0.5.11
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.gnue.org/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	24e4ea106769345f68b38ba95560b7a5
URL:		http://www.gnue.org/
BuildRequires:	gnue-common
BuildRequires:	python
BuildRequires:	python-devel
Requires:	gnue-common
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUe Forms is a data-aware user-interface generator. In more specific
terms, Forms, using a clean XML-based definition, can display the same
functional user interface in various physical mediums, whether GUI,
HTML, console, or via a telephone-response system. Forms is designed
from the ground up to describe a functional, database-backed interface,
with no emphasis on particular widget sets. A form should be equally
usable in a console/text-based environment as it is in a GUI setting.

#%description -l pl

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO doc/*.* doc/technotes
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/gnue/forms
%{_datadir}/gnue/dialogs
%{_datadir}/gnue/images/forms
%{_mandir}/man?/*
