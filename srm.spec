Name: 		srm
Version: 	1.2.11
Release: 	%mkrel 2
License: 	MIT
URL: 		http://srm.sourceforge.net
Group: 		System/Base
Source: 	%{name}-%{version}.tar.bz2

Summary: srm (secure rm) is a command-line compatible rm(1) which destroys file contents before unlinking

%description
This is srm, a secure replacement for rm(1). Unlike the standard rm,
it overwrites the data in the target files before unlinking them. This
prevents command-line recovery of the data by examining the raw block
device. It may also help frustrate physical examination of the disk,
although it's unlikely that completely protects against this type of
recovery.
%prep
%setup
%configure
%make

%build

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}
make clean

%files
%attr(-, root, root) %{_bindir}/srm
%attr(0644,root,root) %{_mandir}/man1/*



%changelog
* Mon Mar 21 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.2.11-2mdv2011.0
+ Revision: 647202
- tipo

* Sun Mar 20 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.2.11-1
+ Revision: 647191
- 1.2.11

* Mon Nov 08 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.2.10-2mdv2011.0
+ Revision: 595117
- rebuild
- Summary fix
- Vendor fix
- import srm

