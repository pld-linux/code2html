%include	/usr/lib/rpm/macros.perl
Summary:	Code2html is a tool which allows you to convert your source code files to syntax highlighted HTML
Summary(pl):	Code2html jest narzêdziem konwertuj±cym twój kod ¼ród³owy do HTML-u z wyró¿nieniem sk³adni
Name:		code2html
Version:	0.9.1
Release:	1
License:	Freeware
Group:		Applications/Publishing
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Code2html is a perl script which converts a program source code to
syntax highlighted HTML, or any other format for which rules are
defined. To use code2html, you also need to install Perl.

%description -l pl
Code2html jest skryptem Perla konwertuj±cym ¼ród³o programu do HTML-u
z wyró¿nieniem sk³adni, albo do innego formatu, dla którego zostan±
zdefiniowane odpowiednie regu³y. Aby u¿ywaæ code2html, musisz jeszcze
zainstalowaæ pakiet perl.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install code2html $RPM_BUILD_ROOT%{_bindir}
install code2html.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
