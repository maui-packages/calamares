# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       calamares

# >> macros
# << macros

Summary:    The distribution-independent installer framework
Version:    0.1.0
Release:    1
Group:      System/Base
License:    GPLv3+
URL:        https://github.com/calamares/calamares.git
Source0:    %{name}-%{version}.tar.xz
Source1:    settings.conf
Source2:    locale.conf
Source3:    unpackfs.conf
Source100:  calamares.yaml
Requires:   parted
Requires:   udisks2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libparted)
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  kcoreaddons-devel
BuildRequires:  kconfig-devel
BuildRequires:  solid-devel
BuildRequires:  ki18n-devel
BuildRequires:  libudisks2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  python3-devel
BuildRequires:  boost-devel >= 1.54.0

%description
The distribution-independent installer framework.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DWITH_PARTITIONMANAGER=1 \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
install -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/calamares/settings.conf
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/calamares/modules/locale.conf
install -D -m644 %{SOURCE3} %{buildroot}%{_datadir}/calamares/modules/unpackfs.conf
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/calamares
%{_datadir}/calamares
%{_libdir}/*.so.*
%{_libdir}/libcalapm.so
%{_libdir}/calamares/modules
%{_datadir}/calamares
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%exclude %{_libdir}/libcalapm.so
%{_libdir}/calamares/*.so
%{_libdir}/cmake/Calamares
%{_includedir}/libcalamares
# >> files devel
# << files devel
