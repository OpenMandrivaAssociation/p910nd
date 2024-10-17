Summary:	Tiny non-spooling printer daemon
Name:		p910nd
Version:	0.93
Release:	2
License:	GPL
Group:		System/Servers
URL:		https://etherboot.sourceforge.net/p910nd
Source0:	http://etherboot.sourceforge.net/p910nd/%{name}-%{version}.tar.bz2
Source1:	%{name}.init
Requires(pre,post):		rpm-helper
Requires:	tcp_wrappers
BuildRequires:	tcp_wrappers-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Tiny non-spooling printer daemon for Linux hosts. Accepts data
over a TCP network connection from a spooling host. Useful on
diskless X terminals with local printer.

%prep
%setup -q

cp %{SOURCE1} %{name}.init

%build

gcc %{optflags} %{ldflags} -DUSE_LIBWRAP -o p910nd p910nd.c -lwrap

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_mandir}/man8

install -m755 %{name}.init %{buildroot}%{_initrddir}/%{name}
install -m755 %{name} %{buildroot}%{_sbindir}/
install -m755 *.pl %{buildroot}%{_datadir}/%{name}/
install -m644 %{name}.8 %{buildroot}%{_mandir}/man8/

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%config(noreplace) %attr(0755,root,root) %{_initrddir}/%{name}
%attr(0644,root,root) %{_mandir}/man8/%{name}.8*
%attr(0755,root,root) %{_datadir}/%{name}/*.pl
%attr(0755,root,root) %{_sbindir}/%{name}


%changelog
* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 0.93-1mdv2011.0
+ Revision: 602259
- use ldflas
- new version 0.93

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild early 2009.0 package (before pixel changes)

* Fri Apr 25 2008 Funda Wang <fwang@mandriva.org> 0.92-1mdv2009.0
+ Revision: 197413
- New version 0.92

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 Funda Wang <fwang@mandriva.org> 0.91-1mdv2008.1
+ Revision: 103787
- fix prerequires
- New version 0.91

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Fri Jul 06 2007 Funda Wang <fwang@mandriva.org> 0.9-1mdv2008.0
+ Revision: 49019
- New version


* Fri Nov 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7-3mdv2007.0
+ Revision: 85296
- Import p910nd

* Fri Nov 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7-3mdv2007.1
- rebuild

* Sat Sep 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7-2mdk
- rebuild

* Sat Aug 21 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.7-1mdk
- 0.7
- built against dietlibc per default

