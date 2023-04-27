%global octpkg ltfat

Summary:	The Large Time-Frequency Analysis Toolbox for Octave
Name:		octave-ltfat
Version:	2.5.0
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/ltfat/
Url:		https://github.com/ltfat/ltfat/
Source0:	https://github.com/ltfat/ltfat/releases/download/v%{version}/ltfat-%{version}-of.tar.gz

BuildRequires:  octave-devel >= 5.0.0
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(portaudio-2.0)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Large Time/Frequency Analysis Toolbox (LTFAT) is a Matlab/Octave
toolbox for working with time-frequency analysis and synthesis. It is
intended both as an educational and a computational tool. The toolbox
provides a large number of linear transforms including Gabor and
wavelet transforms along with routines for constructing windows
(filter prototypes) and routines for manipulating coefficients.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

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

