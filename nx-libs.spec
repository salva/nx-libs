%global _hardened_build 1

Name:           nx-libs
Version:        3.5.99.0
Release:        0.0build1%{?dist}
Summary:        NX X11 protocol compression libraries

Group:          System Environment/Libraries
%if 0%{?suse_version}
License:        GPL-2.0+
%else
License:        GPLv2+
%endif
URL:            http://github.com/ArcticaProject/nx-libs/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf >= 2.13
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig

# suse_version 1315 is SLE-12
%if 0%{?suse_version} != 1315 && 0%{?suse_version} >= 1230
BuildRequires:  gpg-offline
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
%if 0%{?suse_version} >= 1130
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pixman-1) >= 0.13.2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xfont)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xinerama)
%else
BuildRequires:  libexpat-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  pixman-devel >= 0.13.2
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXext-devel
BuildRequires:  xorg-x11-libXpm-devel
BuildRequires:  xorg-x11-libXfont-devel
BuildRequires:  xorg-x11-libXdmcp-devel
BuildRequires:  xorg-x11-libXdamage-devel
BuildRequires:  xorg-x11-libXcomposite-devel
BuildRequires:  xorg-x11-libXrandr-devel
BuildRequires:  xorg-x11-libXfixes-devel
BuildRequires:  xorg-x11-libXtst-devel
BuildRequires:  xorg-x11-libXinerama-devel
%endif
BuildRequires:  xorg-x11-util-devel
%endif

%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  expat-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  pixman-devel >= 0.13.2
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXfont-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXinerama-devel
%endif

# For imake
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  zlib-devel

%if 0%{?suse_version} >= 1130 || 0%{?fedora}
%define cond_noarch BuildArch: noarch
%else
%define cond_noarch %nil
%endif

Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Obsoletes:      nx%{?_isa} < 3.5.0-19
Provides:       nx%{?_isa} = %{version}-%{release}

%if 0%{?el5}
# For compatibility with EPEL5
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
%else
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif

%description
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.


%package -n libNX_X11-6
Group:          System Environment/Libraries
Summary:        Core NX protocol client library
Requires:       %{name}%{?_isa} >= 3.5.0.29
Obsoletes:      libNX_X11
%if 0%{?suse_version}
Requires:       xorg-x11-fonts-core
%endif

%description -n libNX_X11-6
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.


%package -n libNX_X11-devel
Group:          Development/Libraries
Summary:        Development files for the Core NX protocol library
Requires:       libNX_X11-6%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}

%description -n libNX_X11-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

This package contains all necessary include files and libraries
needed to develop applications that require these.


%package -n libNX_Xau-devel
Group:          Development/Libraries
Summary:        Development files for the NX authorization protocol library
Requires:       libNX_Xau6%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}

%description -n libNX_Xau-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

libNX_Xau provides mechanisms for individual access to an nx-X11 Window
System display. It uses existing core protocol and library hooks for
specifying authorization data in the connection setup block to restrict
use of the display to only those clients that show that they know a
server-specific key called a "magic cookie".

This package contains all necessary include files and libraries
needed to develop applications that require these.


%package -n libNX_Xau6
Group:          System Environment/Libraries
Summary:        NX authorization protocol library
Requires:       %{name}%{?_isa} >= 3.5.0.29
Obsoletes:      libNX_Xau

%description -n libNX_Xau6
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

libNX_Xau provides mechanisms for individual access to an X Window
System display. It uses existing core protocol and library hooks for
specifying authorization data in the connection setup block to
restrict use of the display to only those clients that show that they
know a server-specific key called a "magic cookie".


%package -n libNX_Xext-devel
Group:          Development/Libraries
Summary:        Development files for the NX Common Extensions library
Requires:       libNX_Xext6%{?_isa} = %{version}-%{release}
Requires:       libNX_Xau6-devel%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}

%description -n libNX_Xext-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The NX_Xext library contains a handful of X11 extensions:
- Display Power Management Signaling (DPMS) extension
- X11 Nonrectangular Window Shape extension (Xshape)
- The MIT Shared Memory extension (MIT-SHM/Xshm)

This package contains all necessary include files and libraries
needed to develop applications that require these.


%package -n libNX_Xext6
Group:          System Environment/Libraries
Summary:        Common extensions to the NX protocol
Requires:       %{name}%{?_isa} >= 3.5.0.29
Obsoletes:      libNX_Xext

%description -n libNX_Xext6
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The NX_Xext library contains a handful of X11 extensions:
- Double Buffer extension (DBE/Xdbe)
- Display Power Management Signaling (DPMS) extension
- X11 Nonrectangular Window Shape extension (Xshape)
- The MIT Shared Memory extension (MIT-SHM/Xshm)
- TOG-CUP (colormap) protocol extension (Xcup)
- X Extended Visual Information extension (XEvi)
- X11 Double-Buffering, Multi-Buffering, and Stereo extension (Xmbuf)

NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.


%package -n libXcomp-devel
Group:          Development/Libraries
Summary:        Development files for the NX differential compression library
Requires:       libXcomp3%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel = %{version}-%{release}

%description -n libXcomp-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The NX differential compression library's development files.


%package -n libXcomp3
Group:          System Environment/Libraries
Summary:        NX differential compression library
Requires:       %{name}%{?_isa} >= 3.5.0.29
Obsoletes:      libXcomp

%description -n libXcomp3
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package contains the NX differential compression library for X11.


%package -n libXcompext-devel
Group:          Development/Libraries
Summary:        Development files for the NX compression extensions library
Requires:       libXcompext3%{?_isa} = %{version}-%{release}
Requires:       libNX_X11-devel%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}

%description -n libXcompext-devel
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

The NX compression extensions library's development files.


%package -n libXcompext3
Group:          System Environment/Libraries
Summary:        NX protocol compression extensions library
Requires:       %{name}%{?_isa} >= 3.5.0.29
Obsoletes:      libXcompext

%description -n libXcompext3
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package provides the library to support additional features to
the core NX library.


%package -n libXcompshad-devel
Group:          Development/Libraries
Summary:        Development files for the NX session shadowing library
Requires:       libXcompshad3%{?_isa} = %{version}-%{release}
Requires:       libNX_X11-devel%{?_isa} = %{version}-%{release}
Requires:       libNX_Xext-devel%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n libXcompshad-devel
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

The NX session shadowing library's development files.


%package -n libXcompshad3
Group:          System Environment/Libraries
Summary:        NX session shadowing Library
Requires:       %{name}%{?_isa} >= 3.5.0.29
Obsoletes:      libXcompshad

%description -n libXcompshad3
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package provides the session shadowing library.


%package devel
Group:          Development/Libraries
Summary:        Include files and libraries for NX development
Requires:       libNX_X11-devel%{?_isa} = %{version}-%{release}
Requires:       libNX_Xau-devel%{?_isa} = %{version}-%{release}
Requires:       libNX_Xext-devel%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package contains all necessary include files and libraries
needed to develop nx-X11 applications that require these.


%package -n nx-proto-devel
Group:          Development/Libraries
Summary:        Include files for NX development

%description -n nx-proto-devel
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package contains all necessary include files and libraries
for the nx_X11 wire protocol.


%package -n nxagent
Group:          Applications/System
Summary:        NX Agent
Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Obsoletes:      nx%{?_isa} < 3.5.0-19
Provides:       nx%{?_isa} = %{version}-%{release}
%if 0%{?suse_version}
Requires:       xorg-x11-fonts-core
%endif

%description -n nxagent
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

nxagent is an agent providing NX transport of X sessions. The
application is based on the well-known Xnest server. nxagent, like
Xnest, is an X server for its own clients, and at the same time, an X
client for a system's local X server.

The main scope of nxagent is to eliminate X round-trips or transform
them into asynchronous replies. nxagent works together with nxproxy.
nxproxy itself does not make any effort to minimize round-trips by
itself, this is demanded of nxagent.

Being an X server, nxagent is able to resolve all the property/atoms
related requests locally, ensuring that the most common source of
round-trips are nearly reduced to zero.


%package -n nxauth
Group:          Applications/System
Summary:        NX Auth

%description -n nxauth
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

This package provides the NX xauth binary.


%package -n nxproxy
Group:          Applications/System
Summary:        NX Proxy
Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Obsoletes:      nx%{?_isa} < 3.5.0-19
Provides:       nx%{?_isa} = %{version}-%{release}

%description -n nxproxy
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

This package provides the NX proxy (client) binary.


%prep
%setup -q
# remove build cruft that is in Git (also taken from roll-tarball.sh)
rm -Rf nx*/configure nx*/autom4te.cache*
# Install into /usr
sed -i -e 's,/usr/local,/usr,' nx-X11/config/cf/site.def
# Use rpm optflags
sed -i -e 's#-O3#%{optflags}#' nx-X11/config/cf/host.def
# Use multilib dirs
# We're installing binaries into %%{_libdir}/nx/bin rather than %%{_libexedir}/nx
# because upstream expects libraries and binaries in the same directory
sed -i -e 's,/lib/nx,/%{_lib}/nx,' Makefile nx-X11/config/cf/X11.tmpl
sed -i -e 's,/usr/lib/,/usr/%{_lib}/,' bin/*
# Fix FSF address
find -name LICENSE | xargs sed -i \
  -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/'
# Fix source permissions
find -type f -name '*.[hc]' | xargs chmod -x

# Bundled nx-X11/extras
# Mesa - Used by the X server

# Xcursor - Other code still references files in it


%build
cat >"my_configure" <<'EOF'
%configure
EOF
chmod a+x my_configure;
# The RPM macro for the linker flags does not exist on EPEL
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
export SHLIBGLOBALSFLAGS="%{__global_ldflags}"
export LOCAL_LDFLAGS="%{__global_ldflags}"
make %{?_smp_mflags} CONFIGURE="$PWD/my_configure" PREFIX=%{_prefix} USRLIBDIR=%{_libdir} SHLIBDIR=%{_libdir}

%install
make install \
        DESTDIR=%{buildroot} \
        PREFIX=%{_prefix} \
        USRLIBDIR=%{_libdir} SHLIBDIR=%{_libdir} \
        INSTALL_DIR="install -dm0755" \
        INSTALL_FILE="install -pm0644" \
        INSTALL_PROGRAM="install -pm0755"

# Remove static libs (they don't exist on SLES, so using -f here)
rm -f %{buildroot}%{_libdir}/*.a

# Fix permissions on shared libraries
chmod 755  %{buildroot}%{_libdir}/lib*.so*

#Remove extras, GL, and other unneeded headers
rm -r %{buildroot}%{_includedir}/GL
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XInput.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XK*.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/*Xv*.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/dpms.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/security.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/sync.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/xtestext1.h
rm -r %{buildroot}%{_includedir}/nx-X11/Xtrans

%if 0%{?fdupes:1}
%fdupes %buildroot/%_prefix
%endif

%post -p /sbin/ldconfig
%post -n libNX_X11-6 -p /sbin/ldconfig
%post -n libNX_Xau6 -p /sbin/ldconfig
%post -n libNX_Xext6 -p /sbin/ldconfig
%post -n libXcomp3 -p /sbin/ldconfig
%post -n libXcompext3 -p /sbin/ldconfig
%post -n libXcompshad3 -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%postun -n libNX_X11-6 -p /sbin/ldconfig
%postun -n libNX_Xau6 -p /sbin/ldconfig
%postun -n libNX_Xext6 -p /sbin/ldconfig
%postun -n libXcomp3 -p /sbin/ldconfig
%postun -n libXcompext3 -p /sbin/ldconfig
%postun -n libXcompshad3 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING
%doc nx-X11/README
%dir %{_libdir}/nx
%dir %{_datadir}/nx
%{_datadir}/nx/SecurityPolicy

%files -n libNX_X11-6
%defattr(-,root,root)
%{_libdir}/libNX_X11.so.6*

%files -n libNX_X11-devel
%defattr(-,root,root)
%{_libdir}/libNX_X11.so
%dir %{_includedir}/nx
%dir %{_includedir}/nx-X11
%{_includedir}/nx-X11/ImUtil.h
%{_includedir}/nx-X11/XKBlib.h
%{_includedir}/nx-X11/Xcms.h
%{_includedir}/nx-X11/Xlib.h
%{_includedir}/nx-X11/XlibConf.h
%{_includedir}/nx-X11/Xlibint.h
%{_includedir}/nx-X11/Xlocale.h
%{_includedir}/nx-X11/Xregion.h
%{_includedir}/nx-X11/Xresource.h
%{_includedir}/nx-X11/Xutil.h
%{_includedir}/nx-X11/cursorfont.h

%files -n libNX_Xau-devel
%defattr(-,root,root)
%{_libdir}/libNX_Xau.so
%{_includedir}/nx-X11/Xauth.h

%files -n libNX_Xau6
%defattr(-,root,root)
%{_libdir}/libNX_Xau.so.6*

%files -n libNX_Xext-devel
%defattr(-,root,root)
%{_libdir}/libNX_Xext.so
%dir %{_includedir}/nx-X11/extensions
%{_includedir}/nx-X11/extensions/XShm.h
%{_includedir}/nx-X11/extensions/Xext.h
%{_includedir}/nx-X11/extensions/extutil.h
%{_includedir}/nx-X11/extensions/shape.h

%files -n libNX_Xext6
%defattr(-,root,root)
%{_libdir}/libNX_Xext.so.6*

%files -n libXcomp-devel
%defattr(-,root,root)
%_libdir/libXcomp.so
%{_includedir}/nx/MD5.h
%{_includedir}/nx/NX.h
%{_includedir}/nx/NXalert.h
%{_includedir}/nx/NXpack.h
%{_includedir}/nx/NXproto.h
%{_includedir}/nx/NXvars.h
%{_libdir}/pkgconfig/nxcomp.pc

%files -n libXcomp3
%defattr(-,root,root)
%doc COPYING
%doc nxcomp/README
%_libdir/libXcomp.so.3*

%files -n libXcompext-devel
%defattr(-,root,root)
%_libdir/libXcompext.so
%{_includedir}/nx/NXlib.h
%{_includedir}/nx/NXlibint.h
%{_libdir}/pkgconfig/nxcompext.pc

%files -n libXcompext3
%defattr(-,root,root)
%doc COPYING
%doc nxcompext/README
%_libdir/libXcompext.so.3*

%files -n libXcompshad-devel
%defattr(-,root,root)
%_libdir/libXcompshad.so
%{_includedir}/nx/Shadow.h
%{_libdir}/pkgconfig/nxcompshad.pc

%files -n libXcompshad3
%defattr(-,root,root)
%doc COPYING
%_libdir/libXcompshad.so.3*

%files devel
%defattr(-,root,root)
%{_includedir}/nx-X11/X10.h
%dir %{_includedir}/nx-X11/extensions
%{_includedir}/nx-X11/extensions/panoramiXext.h
%{_includedir}/nx-X11/extensions/record.h
%{_includedir}/nx-X11/misc.h
%{_includedir}/nx-X11/os.h

%files -n nx-proto-devel
%defattr(-,root,root)
%dir %{_includedir}/nx-X11
%{_includedir}/nx-X11/DECkeysym.h
%{_includedir}/nx-X11/HPkeysym.h
%{_includedir}/nx-X11/Sunkeysym.h
%{_includedir}/nx-X11/X.h
%{_includedir}/nx-X11/XF86keysym.h
%{_includedir}/nx-X11/XWDFile.h
%{_includedir}/nx-X11/Xalloca.h
%{_includedir}/nx-X11/Xarch.h
%{_includedir}/nx-X11/Xatom.h
%{_includedir}/nx-X11/Xdefs.h
%{_includedir}/nx-X11/Xfuncproto.h
%{_includedir}/nx-X11/Xfuncs.h
%{_includedir}/nx-X11/Xmd.h
%{_includedir}/nx-X11/Xos.h
%{_includedir}/nx-X11/Xos_r.h
%{_includedir}/nx-X11/Xosdefs.h
%{_includedir}/nx-X11/Xpoll.h
%{_includedir}/nx-X11/Xproto.h
%{_includedir}/nx-X11/Xprotostr.h
%{_includedir}/nx-X11/Xthreads.h
%{_includedir}/nx-X11/ap_keysym.h
%{_includedir}/nx-X11/keysym.h
%{_includedir}/nx-X11/keysymdef.h
%{_includedir}/nx-X11/extensions/Xdbeproto.h
%{_includedir}/nx-X11/extensions/XI.h
%{_includedir}/nx-X11/extensions/XIproto.h
%{_includedir}/nx-X11/extensions/XResproto.h
%{_includedir}/nx-X11/extensions/bigreqstr.h
%{_includedir}/nx-X11/extensions/composite.h
%{_includedir}/nx-X11/extensions/compositeproto.h
%{_includedir}/nx-X11/extensions/damagewire.h
%{_includedir}/nx-X11/extensions/damageproto.h
%{_includedir}/nx-X11/extensions/dpmsstr.h
%{_includedir}/nx-X11/extensions/panoramiXproto.h
%{_includedir}/nx-X11/extensions/randr.h
%{_includedir}/nx-X11/extensions/randrproto.h
%{_includedir}/nx-X11/extensions/recordstr.h
%{_includedir}/nx-X11/extensions/render.h
%{_includedir}/nx-X11/extensions/renderproto.h
%{_includedir}/nx-X11/extensions/securstr.h
%{_includedir}/nx-X11/extensions/shapestr.h
%{_includedir}/nx-X11/extensions/shmstr.h
%{_includedir}/nx-X11/extensions/syncstr.h
%{_includedir}/nx-X11/extensions/xcmiscstr.h
%{_includedir}/nx-X11/extensions/xf86bigfont.h
%{_includedir}/nx-X11/extensions/xf86bigfstr.h
%{_includedir}/nx-X11/extensions/xfixesproto.h
%{_includedir}/nx-X11/extensions/xfixeswire.h
%{_includedir}/nx-X11/extensions/xtestconst.h
%{_includedir}/nx-X11/extensions/xteststr.h

%files -n nxagent
%defattr(-,root,root)
%dir %{_sysconfdir}/nxagent
%config(noreplace) %{_sysconfdir}/nxagent/keystrokes.cfg
%config(noreplace) %{_sysconfdir}/nxagent/nxagent.keyboard
%config(noreplace) %{_sysconfdir}/nxagent/rgb
%{_bindir}/nxagent
%dir %{_libdir}/nx/bin
%{_libdir}/nx/bin/nxagent
%{_datadir}/pixmaps/nxagent.xpm
%{_datadir}/nx/rgb
%{_datadir}/man/man1/nxagent.1*

%files -n nxauth
%defattr(-,root,root)
%{_bindir}/nxauth
%dir %{_libdir}/nx/bin
%{_libdir}/nx/bin/nxauth
%{_datadir}/man/man1/nxauth.1*

%files -n nxproxy
%defattr(-,root,root)
%{_bindir}/nxproxy
%{_mandir}/man1/nxproxy.1*
%{_datadir}/man/man1/nxproxy.1*
%dir %{_libdir}/nx/bin
%{_libdir}/nx/bin/nxproxy


%changelog
* Thu Jan 29 2015 Mike Gabriel <mike.gabriel@das-netzwerkteam.de> 3.5.99.0
- See upstream ChangeLog and debian/changelog for details.
