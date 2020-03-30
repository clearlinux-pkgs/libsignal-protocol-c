#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsignal-protocol-c
Version  : 2.3.3
Release  : 2
URL      : https://github.com/signalapp/libsignal-protocol-c/archive/v2.3.3/libsignal-protocol-c-2.3.3.tar.gz
Source0  : https://github.com/signalapp/libsignal-protocol-c/archive/v2.3.3/libsignal-protocol-c-2.3.3.tar.gz
Summary  : Signal Protocol C Library
Group    : Development/Tools
License  : GPL-3.0
Requires: libsignal-protocol-c-lib = %{version}-%{release}
Requires: libsignal-protocol-c-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : openssl-dev

%description
# Overview
This is a ratcheting forward secrecy protocol that works in synchronous and asynchronous messaging
environments. See the [Java library](https://github.com/whispersystems/libsignal-protocol-java) for more details.

%package dev
Summary: dev components for the libsignal-protocol-c package.
Group: Development
Requires: libsignal-protocol-c-lib = %{version}-%{release}
Provides: libsignal-protocol-c-devel = %{version}-%{release}
Requires: libsignal-protocol-c = %{version}-%{release}

%description dev
dev components for the libsignal-protocol-c package.


%package lib
Summary: lib components for the libsignal-protocol-c package.
Group: Libraries
Requires: libsignal-protocol-c-license = %{version}-%{release}

%description lib
lib components for the libsignal-protocol-c package.


%package license
Summary: license components for the libsignal-protocol-c package.
Group: Default

%description license
license components for the libsignal-protocol-c package.


%prep
%setup -q -n libsignal-protocol-c-2.3.3
cd %{_builddir}/libsignal-protocol-c-2.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585588440
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1585588440
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libsignal-protocol-c
cp %{_builddir}/libsignal-protocol-c-2.3.3/LICENSE %{buildroot}/usr/share/package-licenses/libsignal-protocol-c/a6adc13d0c809ab8cb68e6e3b6eb7571bd0e2920
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/signal/curve.h
/usr/include/signal/device_consistency.h
/usr/include/signal/fingerprint.h
/usr/include/signal/group_cipher.h
/usr/include/signal/group_session_builder.h
/usr/include/signal/hkdf.h
/usr/include/signal/key_helper.h
/usr/include/signal/protocol.h
/usr/include/signal/ratchet.h
/usr/include/signal/sender_key.h
/usr/include/signal/sender_key_record.h
/usr/include/signal/sender_key_state.h
/usr/include/signal/session_builder.h
/usr/include/signal/session_cipher.h
/usr/include/signal/session_pre_key.h
/usr/include/signal/session_record.h
/usr/include/signal/session_state.h
/usr/include/signal/signal_protocol.h
/usr/include/signal/signal_protocol_types.h
/usr/lib64/libsignal-protocol-c.so
/usr/lib64/pkgconfig/libsignal-protocol-c.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsignal-protocol-c.so.2
/usr/lib64/libsignal-protocol-c.so.2.3.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsignal-protocol-c/a6adc13d0c809ab8cb68e6e3b6eb7571bd0e2920
