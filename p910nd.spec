Summary:	Tiny non-spooling printer daemon
Name:		p910nd
Version:	0.93
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://etherboot.sourceforge.net/p910nd
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

gcc %{optflags} -DUSE_LIBWRAP -o p910nd p910nd.c -lwrap

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
