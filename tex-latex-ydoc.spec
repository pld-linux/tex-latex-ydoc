Summary:	Macros and environments to document LaTeX packages and classes
Summary(pl.UTF-8):	Makra i środowiska do dokumentowania pakietów i klas LaTeXa
Name:		tex-latex-ydoc
Version:	0.6alpha
Release:	1
License:	LaTeX Project Public License v1.3+
Group:		Applications/Publishing
Source0:	http://mirrors.ctan.org/macros/latex/contrib/ydoc.zip
# Source0-md5:	8602d89c031a60a7067003b07bac1cb4
URL:		https://sourceforge.net/projects/ydoc/
BuildRequires:	/usr/bin/tex
BuildRequires:	rpmbuild(macros) >= 1.751
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
# TODO: use generic
Requires:	texlive
# for ydoc itself; not needed for just ydocstrip
#Requires:	tex(svn-prov)
Provides:	tex(ydoc) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Macros and environments to document LaTeX packages and classes.

%description -l pl.UTF-8
Makra i środowiska do dokumentowania pakietów i klas LaTeXa.

%prep
%setup -q -n ydoc

%build
tex ydoc.dtx

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{doc/latex,tex/generic,tex/latex}/ydoc

cp -p *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/ydoc
cp -p *.tex $RPM_BUILD_ROOT%{_datadir}/texmf/tex/generic/ydoc
cp -p *.cls *.sty *.cfg $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/ydoc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
%doc %{_datadir}/texmf/doc/latex/ydoc
%{_datadir}/texmf/tex/generic/ydoc
%{_datadir}/texmf/tex/latex/ydoc
