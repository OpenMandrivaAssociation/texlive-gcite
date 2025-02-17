Name:		texlive-gcite
Version:	15878
Release:	2
Summary:	Citations in a reader-friendly style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/exptl/gcite
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gcite.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gcite.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gcite.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows citations in the German style, which is
considered by many to be particularly reader-friendly. The
citation provides a small amount of bibliographic information
in a footnote on the page where each citation is made. It
combines a desire to eliminate unnecessary page-turning with
the look-up efficiency afforded by numeric citations. The
package makes use of the (still experimental) BibLaTeX package,
and is itself also considered experimental; comment is invited.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gcite/gcite.sty
%doc %{_texmfdistdir}/doc/latex/gcite/CHANGES
%doc %{_texmfdistdir}/doc/latex/gcite/README
%doc %{_texmfdistdir}/doc/latex/gcite/gcite.bib
%doc %{_texmfdistdir}/doc/latex/gcite/gcite.pdf
#- source
%doc %{_texmfdistdir}/source/latex/gcite/gcite.dtx
%doc %{_texmfdistdir}/source/latex/gcite/gcite.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
