Summary:	Code2html is a tool which allows you to convert your source code files to syntax highlighted HTML
Summary(pl):	Code2html jest narz�dziem konwertuj�cym tw�j kod �r�d�owy do HTML-u z wyr�nieniem sk�adni
Name:		code2html
Version:	0.9.1
Release:	1
License:	Freeware
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikov�n�
Group(da):	Programmer/Udgivelse
Group(de):	Applikationen/Publizieren
Group(es):	Aplicaciones/Edici�n
Group(fr):	Applications/Edition
Group(is):	Forrit/Umbrot
Group(it):	Applicazioni/Publishing
Group(ja):	���ץꥱ�������/�ѥ֥�å���
Group(no):	Applikasjoner/Publisering
Group(pl):	Aplikacje/Publikowanie
Group(pt):	Aplica��es/Publica��o
Group(pt_BR):	Aplica��es/Editora��o
Group(ru):	����������/����������
Group(sl):	Programi/Zalo�ni�tvo
Group(sv):	Till�mpningar/Publicering
Group(uk):	�������Φ ��������/�������Ʀ�
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Code2html is a perl script which converts a program source code to
syntax highlighted HTML, or any other format for which rules are
defined. To use code2html, you also need to install Perl.

%description -l pl
Code2html jest skryptem Perla konwertuj�cym �r�d�o programu do HTML-u
z wyr�nieniem sk�adni, albo do innego formatu, dla kt�rego zostan�
zdefiniowane odpowiednie regu�y. Aby u�ywa� code2html, musisz jeszcze
zainstalowa� pakiet perl.

%prep
%setup -q 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install code2html $RPM_BUILD_ROOT%{_bindir}
install code2html.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf ChangeLog CREDITS LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
