# revision 15878
# category Package
# catalog-ctan /macros/latex/exptl/gcite
# catalog-date 2009-07-04 21:47:31 +0200
# catalog-license lppl1.3
# catalog-version 1.0.1
Name:		texlive-gcite
Version:	1.0.1
Release:	1
Summary:	Citations in a reader-friendly style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/exptl/gcite
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gcite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gcite.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gcite.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows citations in the German style, which is
considered by many to be particularly reader-friendly. The
citation provides a small amount of bibliographic information
in a footnote on the page where each citation is made. It
combines a desire to eliminate unnecessary page-turning with
the look-up efficiency afforded by numeric citations. The
package makes use of the (still experimental) BibLaTeX package,
and is itself also considered experimental; comment is invited.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
