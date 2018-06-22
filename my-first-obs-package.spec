#
# spec file for package my-first-obs-package
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           my-first-obs-package
Version:        0.1.0
Release:        0
License:        GPL-3.0
Summary:        Example project for OBS documentation
Url:            https://github.com/openSUSE/example-obs
Group:          Development/Languages/Python
Source:         https://github.com/openSUSE/example-obs/release/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
Requires:       glibc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# BuildArch:

%description
This is an example project for the OBS documentation.

%prep
%setup -q -n %{name}-%{version}


%build
export CFLAGS="$RPM_OPT_FLAGS -DNDEBUG"
export CXXFLAGS="$RPM_OPT_FLAGS -DNDEBUG"

cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?jobs:-j%jobs}


%install
make install DESTDIR="$RPM_BUILD_ROOT"


%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/*

%changelog