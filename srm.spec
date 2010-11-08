Name: 		srm
Version: 	1.2.10
Release: 	%mkrel 2
License: 	MIT
URL: 		http://srm.sourceforge.net
Group: 		System/Base
Source: 	%{name}-%{version}.tar.bz2

Summary: srm (secure rm) is a command-line compatible rm(1) which destroys file contents before unlinking

%description
This is srm, a secure replacement for rm(1). Unlike the standard rm,
it overwrites the data in the target files before unlinkg them. This
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

