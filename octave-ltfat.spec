%define octpkg ltfat

Summary:	The Large Time-Frequency Analysis Toolbox
Name:		octave-%{octpkg}
Version:	2.3.1
Release:	1
Url:		https://octave.sourceforge.io/%{octpkg}/
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://github.com/ltfat/ltfat/pull/116
Patch0:		%{name}-2.3.1-fix_typo.patch
License:	GPLv3+
Group:		Sciences/Mathematics

BuildRequires:	octave-devel > 3.8.0
BuildRequires:	libfftw-devel
BuildRequires:	pkgconfig(portaudio-2.0)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Large Time/Frequency Analysis Toolbox (LTFAT) is a Matlab/Octave toolbox
for working with time-frequency analysis, wavelets and signal processing. It
is intended both as an educational and a computational tool. The toolbox
provides a large number of linear transforms including Gabor and wavelet
transforms along with routines for constructing windows (filter prototypes)
and routines for manipulating coefficients.

This package is part of external Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

