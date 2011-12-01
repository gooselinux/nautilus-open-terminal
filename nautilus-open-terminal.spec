Name:           nautilus-open-terminal
Version:        0.17
Release:	3%{?dist}
Summary:        Nautilus extension for an open terminal shortcut

Group:          User Interface/Desktops
License:       	GPLv2+
URL:            http://download.gnome.org/sources/%{name}/
Source0:        http://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gnome-desktop-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:	libtool automake autoconf gettext intltool
# need extensions
BuildRequires:	nautilus-devel

# https://bugzilla.gnome.org/show_bug.cgi?id=597376
Patch0: leak.patch

%description
The nautilus-open-terminal extension provides a right-click "Open
Terminal" option for nautilus users who prefer that option.

%prep
%setup -q
%patch0 -p1 -b .leak
libtoolize --force --copy
autoreconf

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/nautilus/extensions-2.0/*.{l,}a

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 \
	    --makefile-install-rule \
	    %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :



%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS TODO
%config(noreplace) %{_sysconfdir}/gconf/schemas/*
%{_libdir}/nautilus/extensions-2.0/*.so*

%changelog
* Mon Oct  5 2009 Matthias Clasen <mclasen@redhat.com> - 0.17-2
- Plug a small leak

* Tue Aug 11 2009 Matthias Clasen <mclasen@redhat.com> - 0.17-1
- Update to 0.17

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Paul W. Frields <stickster@gmail.com> - 0.13-1
- Update to upstream 0.13

* Thu May 21 2009 Paul W. Frields <stickster@gmail.com> - 0.12-1
- Update to upstream 0.12

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 0.9-11
- Rebuild against new gnome-desktop

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> - 0.9-10
- Rebuild against latest gnome-desktop

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 0.9-4
- Rebuild against latest gnome-desktop
- Remove the support for Fedora < 6, since "10" < "6"

* Fri May  9 2008 Paul W. Frields <stickster@gmail.com> - 0.9-3
- Use latest automake in spec

* Fri Apr  4 2008 Paul W. Frields <stickster@gmail.com> - 0.9-2
- Handle GConf schema installation

* Fri Feb 29 2008 Matthias Clasen <mclasen@redhat.com> - 0.9-1
- Update to 0.9

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8-4
- Autorebuild for GCC 4.3

* Mon Jan 24 2008 Josh Boyer <jwboyer@gmail.com> - 0.8-2
- Grab SVN snapshot to fix extension directory and building against newer
  nautilus

* Sat Sep 22 2007 Paul W. Frields <stickster@gmail.com> - 0.8-2
- Fix download and source URIs

* Fri Aug 17 2007 Paul W. Frields <stickster@gmail.com> - 0.8-1
- Update License tag
- Update to version 0.8
- Include patch to silence truth value warning

* Sat Aug 28 2006 Paul W. Frields <stickster@gmail.com> - 0.7-3
- Include BR: intltool for mass FC6 rebuild

* Wed Aug 16 2006 Paul W. Frields <stickster@gmail.com> - 0.7-2
- Handle splitting of nautilus and nautilus-extensions

* Tue Aug  1 2006 Paul W. Frields <stickster@gmail.com> - 0.7-1
- Update to version 0.7

* Fri Jun 16 2006 Paul W. Frields <stickster@gmail.com> - 0.6-4
- Fix BuildRequires, adding gettext

* Fri Feb 17 2006 Paul W. Frields <stickster@gmail.com> - 0.6-3
- FESCo mandated rebuild

* Thu Feb  2 2006 Paul W. Frields <stickster@gmail.com> - 0.6-2
- Remove superfluous docs (#179289, thanks Brian Pepple)

* Sat Oct  8 2005 Paul W. Frields <stickster@gmail.com> - 0.6-1
- Update to version 0.6

* Sat Aug 20 2005 Paul W. Frields <stickster@gmail.com> - 0.4-7
- Push release for new build

* Wed Aug 17 2005 Paul W. Frields <stickster@gmail.com> - 0.4-6
- Rebuild against new cairo
- Include <gtk/gtk.h> and remove unused variable (#166346)

* Sun Jul 17 2005 Paul W. Frields <stickster@gmail.com> - 0.4-5
- Add libtoolize to fix multilib problem (#163463)

* Fri Jul 15 2005 Paul W. Frields <stickster@gmail.com> - 0.4-4
- Use find_lang and scriptlets per official guidelines

* Thu Jul 14 2005 Paul W. Frields <stickster@gmail.com> - 0.4-3
- Remove .a and .la devel files from build

* Thu Jul 14 2005 Paul W. Frields <stickster@gmail.com> - 0.4-2
- Use dist tag and update BuildRequires

* Wed Jul 13 2005 Paul W. Frields <stickster@gmail.com> - 0.4-1
- Initial version

