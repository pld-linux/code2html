%include	/usr/lib/rpm/macros.perl
Summary:	Code2html is a tool which allows you to convert your source code files to syntax highlighted HTML
Summary(pl):	Code2html jest narzêdziem konwertuj±cym twój kod ¼ród³owy do HTML-u z wyró¿nieniem sk³adni
Name:		code2html
Version:	0.9.1
Release:	1
License:	Freeware
Group:		Applications/Publishing
Group(cs):	Aplikace/Publikování
Group(da):	Programmer/Udgivelse
Group(de):	Applikationen/Publizieren
Group(es):	Aplicaciones/Edición
Group(fr):	Applications/Edition
Group(is):	Forrit/Umbrot
Group(it):	Applicazioni/Publishing
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥Ñ¥Ö¥ê¥Ã¥·¥ó¥°
Group(no):	Applikasjoner/Publisering
Group(pl):	Aplikacje/Publikowanie
Group(pt):	Aplicações/Publicação
Group(pt_BR):	Aplicações/Editoração
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/ôÉÐÏÇÒÁÆÉÑ
Group(sl):	Programi/Zalo¾ni¹tvo
Group(sv):	Tillämpningar/Publicering
Group(uk):	ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ/ôÉÐÏÇÒÁÆ¦Ñ
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Code2html is a perl script which converts a program source code to
syntax highlighted HTML, or any other format for which rules are
defined. To use code2html, you also need to install Perl.

%description -l pl
Code2html jest skryptem Perla konwertuj±cym ¼ród³o programu do HTML-u
z wyró¼nieniem sk³adni, albo do innego formatu, dla którego zostan±
zdefiniowane odpowiednie regu³y. Aby u¿ywaæ code2html, musisz jeszcze
zainstalowaæ pakiet perl.

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
