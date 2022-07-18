%global debug_package %{nil}

Name: python-distlib
Epoch: 100
Version: 0.3.3
Release: 1%{?dist}
BuildArch: noarch
Summary: Low-level components of distutils2/packaging, augmented with higher-level APIs
License: Python-2.0
URL: https://bitbucket.org/pypa/distlib/downloads/?tab=tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Distlib contains the implementations of the packaging PEPs and other
low-level features which relate to packaging, distribution and
deployment of Python software. If Distlib can be made genuinely useful,
then it is possible for third-party packaging tools to transition to
using it. Their developers and users then benefit from standardised
implementation of low-level functions, time saved by not having to
reinvent wheels, and improved interoperability between tools.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-distlib
Summary: Low-level components of distutils2/packaging, augmented with higher-level APIs
Requires: python3
Provides: python3-distlib = %{epoch}:%{version}-%{release}
Provides: python3dist(distlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-distlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(distlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-distlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(distlib) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-distlib
Distlib contains the implementations of the packaging PEPs and other
low-level features which relate to packaging, distribution and
deployment of Python software. If Distlib can be made genuinely useful,
then it is possible for third-party packaging tools to transition to
using it. Their developers and users then benefit from standardised
implementation of low-level functions, time saved by not having to
reinvent wheels, and improved interoperability between tools.

%files -n python%{python3_version_nodots}-distlib
%license LICENSE.txt
%{python3_sitelib}/distlib*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-distlib
Summary: Low-level components of distutils2/packaging, augmented with higher-level APIs
Requires: python3
Provides: python3-distlib = %{epoch}:%{version}-%{release}
Provides: python3dist(distlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-distlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(distlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-distlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(distlib) = %{epoch}:%{version}-%{release}

%description -n python3-distlib
Distlib contains the implementations of the packaging PEPs and other
low-level features which relate to packaging, distribution and
deployment of Python software. If Distlib can be made genuinely useful,
then it is possible for third-party packaging tools to transition to
using it. Their developers and users then benefit from standardised
implementation of low-level functions, time saved by not having to
reinvent wheels, and improved interoperability between tools.

%files -n python3-distlib
%license LICENSE.txt
%{python3_sitelib}/distlib*
%endif

%changelog
