Name: 		srm
Version: 	1.2.13
Release: 	2
License: 	MIT
URL: 		https://srm.sourceforge.net
Group: 		System/Base
Source: 	%{name}-%{version}.tar.gz

Summary:        Secure rm - destroys file contents before unlinking

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
%makeinstall

%clean
make clean

%files
%attr(-, root, root) %{_bindir}/srm
%attr(0644,root,root) %{_mandir}/man1/*
