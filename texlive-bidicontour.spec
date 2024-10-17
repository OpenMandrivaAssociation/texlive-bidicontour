Name:		texlive-bidicontour
Version:	34631
Release:	2
Summary:	Bidi-aware coloured contour around text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bidicontour
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidicontour.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidicontour.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a re-implementation of the contour package,
making it bidi-aware, and adding support of the xdvipdfmx (when
the outline option of the package is used).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/bidicontour
%doc %{_texmfdistdir}/doc/xelatex/bidicontour

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
