# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate domain
%global forgeurl0 https://github.com/NLnetLabs/domain

Name:           rust-domain
Version:        0.7.2
Release:        %autorelease
Summary:        DNS library for Rust

License:        BSD-3-Clause
URL:            https://crates.io/crates/domain
VCS:            git:%{forgeurl0}
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          domain-fix-metadata-auto.diff

# https://bugzilla.redhat.com/show_bug.cgi?id=1869980
ExcludeArch: %{power64} s390 s390x

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A DNS library for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/Changelog.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bytes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytes-devel %{_description}

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%files       -n %{name}+bytes-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ci-test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ci-test-devel %{_description}

This package contains library source intended for building other packages which
use the "ci-test" feature of the "%{crate}" crate.

%files       -n %{name}+ci-test-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-devel %{_description}

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%files       -n %{name}+futures-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+heapless-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+heapless-devel %{_description}

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%files       -n %{name}+heapless-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+interop-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+interop-devel %{_description}

This package contains library source intended for building other packages which
use the "interop" feature of the "%{crate}" crate.

%files       -n %{name}+interop-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+master-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+master-devel %{_description}

This package contains library source intended for building other packages which
use the "master" feature of the "%{crate}" crate.

%files       -n %{name}+master-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+random-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+random-devel %{_description}

This package contains library source intended for building other packages which
use the "random" feature of the "%{crate}" crate.

%files       -n %{name}+random-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+resolv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+resolv-devel %{_description}

This package contains library source intended for building other packages which
use the "resolv" feature of the "%{crate}" crate.

%files       -n %{name}+resolv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+resolv-sync-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+resolv-sync-devel %{_description}

This package contains library source intended for building other packages which
use the "resolv-sync" feature of the "%{crate}" crate.

%files       -n %{name}+resolv-sync-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ring-devel %{_description}

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%files       -n %{name}+ring-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sign-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sign-devel %{_description}

This package contains library source intended for building other packages which
use the "sign" feature of the "%{crate}" crate.

%files       -n %{name}+sign-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+smallvec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+smallvec-devel %{_description}

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%files       -n %{name}+smallvec-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tsig-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tsig-devel %{_description}

This package contains library source intended for building other packages which
use the "tsig" feature of the "%{crate}" crate.

%files       -n %{name}+tsig-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+validate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+validate-devel %{_description}

This package contains library source intended for building other packages which
use the "validate" feature of the "%{crate}" crate.

%files       -n %{name}+validate-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
