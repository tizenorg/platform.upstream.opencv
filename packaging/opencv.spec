Name: opencv
VCS:  #e3ca2f3bdcac02e9780c2de7001310a2a61a483e-dirty
Summary: OpenCV library
Version: 2.4.9
Release: 9
Group: Development/Libraries
License: BSD-2.0 and LGPL-2.1+
Source0: %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
#BuildRequires:  gettext-tools
#BuildRequires:  edje-tools
#BuildRequires:  eet-tools
#BuildRequires:  eina-devel
#BuildRequires:  eet-devel
#BuildRequires:  evas-devel
#BuildRequires:  ecore-devel
#BuildRequires:  edje-devel
#BuildRequires:  edbus-devel
#BuildRequires:  efreet-devel
#BuildRequires:  ethumb-devel
#BuildRequires:  emotion-devel
#BuildRequires:  app-svc-devel
#BuildRequires:  libx11-devel
BuildRequires:  elementary-devel
BuildRequires:  gstreamer
BuildRequires:  gst-plugins-base
BuildRequires:  gst-plugins-good
BuildRequires:  libavutil-devel
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libswscale-devel
#BuildRequires:  gst-ffmpeg
Requires(post):  /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
The Open Computer Vision Library includes various algorithms for computer vision problems.

%package devel
Summary:    OpenCV Library (Dev)
Group:      Development/Libraries
Requires:    %{name} = %{version}-%{release}

%description devel
The Open Computer Vision Library (Dev) includes various algorithms for computer vision problems.

%prep
%setup -q

%build
%ifarch aarch64 x86_64
ARCH=aarch64
%else
ARCH=arm
%endif

cmake . -DCMAKE_INSTALL_PREFIX=/usr \
    -DARCH=${ARCH} \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CONFIGURATION_TYPES=Release \
	-DBUILD_DOCS=OFF \
	-DBUILD_PACKAGE=OFF \
	-DBUILD_ANDROID_SERVICE=OFF \
	-DBUILD_ANDRIOD_PACKAGE=OFF \
	-DBUILD_SHARED_LIBS=ON \
	-DBUILD_JASPER=OFF \
	-DBUILD_JPEG=OFF \
	-DBUILD_PERF_TESTS=OFF \
	-DBUILD_PNG=OFF \
	-DBUILD_TESTS=OFF \
	-DBUILD_TIFF=OFF \
	-DBUILD_WITH_DEBUG_INFO=ON \
	-DBUILD_ZLIB=OFF \
	-DBUILD_OPENEXR=OFF \
	-DBUILD_TBB=OFF \
	-DBUILD_EXAMPLES=OFF \
	-DBUILD_opencv_apps=OFF \
	-DBUILD_opencv_calib3d=ON \
	-DBUILD_opencv_contrib=ON \
	-DBUILD_opencv_core=ON \
	-DBUILD_opencv_imgproc=ON \
	-DBUILD_opencv_flann=ON \
	-DBUILD_opencv_features2d=ON \
	-DBUILD_opencv_objdetect=ON \
	-DBUILD_opencv_ml=ON \
	-DBUILD_opencv_gpu=OFF \
	-DBUILD_opencv_highgui=ON \
	-DBUILD_opencv_legacy=ON \
	-DBUILD_opencv_nonfree=OFF \
	-DBUILD_opencv_ocl=OFF \
	-DBUILD_opencv_photo=ON \
	-DBUILD_opencv_stitching=OFF \
	-DBUILD_opencv_superres=OFF \
	-DBUILD_opencv_ts=OFF \
	-DBUILD_opencv_video=ON \
	-DBUILD_opencv_videostab=OFF \
	-DBUILD_opencv_world=OFF \
	-DWITH_1394=OFF \
	-DWITH_CSTRIPES=OFF \
	-DWITH_CUBLAS=OFF \
	-DWITH_CUDA=OFF \
	-DWITH_CUFFT=OFF \
	-DWITH_DSHOW=OFF \
	-DWITH_EIGEN=OFF \
	-DWITH_FFMPEG=ON \
	-DWITH_GIGEAPI=OFF \
	-DWITH_INTELPERC=OFF \
	-DWITH_IPP=OFF \
	-DWITH_JASPER=OFF \
	-DWITH_MSMF=OFF \
	-DWITH_NVCUVID=OFF \
	-DWITH_OPENCL=OFF \
	-DWITH_OPENCLAMDBLAS=OFF \
	-DWITH_OPENCLAMDFFT=OFF \
	-DWITH_OPENEXR=OFF \
	-DWITH_OPENGL=ON \
	-DWITH_OPENMP=OFF \
	-DWITH_OPENNI=OFF \
	-DWITH_PNG=ON \
	-DWITH_PVAPI=OFF \
	-DWITH_QT=OFF \
	-DWITH_TBB=OFF \
	-DWITH_TIFF=ON \
	-DWITH_VFW=OFF \
	-DWITH_VTK=OFF \
	-DWITH_WIN32UI=OFF \
	-DWITH_XIMEA=OFF \
	-DWITH_GSTREAMER=ON \
	-DWITH_V4L=ON \
	-DWITH_GTK=ON \
	-DINSTALL_C_EXAMPLES=OFF \
	-DINSTALL_PYTHON_EXAMPLES=OFF \
	-DINSTALL_TESTS=OFF \
	-DINTALL_ANDROID_EXAMPLES=OFF \
	-DENABLE_PRECOMPILED_HEADERS=OFF \
	-DENABLE_DYNAMIC_CUDA=OFF \
	-DENABLE_SOLUTION_FOLDERS=OFF \
	-DENABLE_PROFILLING=OFF \
	-DENABLE_COVERAGE=OFF

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{_datadir}/license
cp LICENSE %{buildroot}%{_datadir}/license/%{name}
cp LICENSE.LGPL-2.1+ %{buildroot}%{_datadir}/license/%{name}-ffmpeg


%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest opencv.manifest
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%{_datadir}/license/*
/usr/share/*

%files devel
/usr/include/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%doc
