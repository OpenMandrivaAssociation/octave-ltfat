%define octpkg ltfat

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	The Large Time-Frequency Analysis Toolbox
Name:		octave-%{octpkg}
Version:	2.2.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel > 3.8.0

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

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

