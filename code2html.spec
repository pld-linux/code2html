Summary:	Code2html is a tool which allows you to convert your source code files to syntax highlighted HTML
Summary(pl.UTF-8):	Code2html jest narzędziem konwertującym twój kod źródłowy do HTML-a z wyróżnieniem składni
Name:		code2html
Version:	0.9.1
Release:	2
License:	Freeware
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	368377696547026c79c51a274571dc39
URL:		http://www.palfrader.org/code2html/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Code2html is a perl script which converts a program source code to
syntax highlighted HTML, or any other format for which rules are
defined. To use code2html, you also need to install Perl.

%description -l pl.UTF-8
Code2html jest skryptem Perla konwertującym źródło programu do HTML-a
z wyróżnieniem składni, albo do innego formatu, dla którego zostaną
zdefiniowane odpowiednie reguły. Aby używać code2html, musisz jeszcze
zainstalować pakiet perl.

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
