#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: ab27b0e
#
Name     : R-fastcluster
Version  : 1.2.6
Release  : 63
URL      : https://cran.r-project.org/src/contrib/fastcluster_1.2.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fastcluster_1.2.6.tar.gz
Summary  : Fast Hierarchical Clustering Routines for R and 'Python'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-fastcluster-lib = %{version}-%{release}
BuildRequires : R-flashClust
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
both R and 'Python'. It implements fast hierarchical, agglomerative
        clustering routines. Part of the functionality is designed as drop-in

%package lib
Summary: lib components for the R-fastcluster package.
Group: Libraries

%description lib
lib components for the R-fastcluster package.


%prep
%setup -q -n fastcluster
pushd ..
cp -a fastcluster buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1705167385

%install
export SOURCE_DATE_EPOCH=1705167385
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fastcluster/CITATION
/usr/lib64/R/library/fastcluster/DESCRIPTION
/usr/lib64/R/library/fastcluster/INDEX
/usr/lib64/R/library/fastcluster/LICENSE
/usr/lib64/R/library/fastcluster/Meta/Rd.rds
/usr/lib64/R/library/fastcluster/Meta/features.rds
/usr/lib64/R/library/fastcluster/Meta/hsearch.rds
/usr/lib64/R/library/fastcluster/Meta/links.rds
/usr/lib64/R/library/fastcluster/Meta/nsInfo.rds
/usr/lib64/R/library/fastcluster/Meta/package.rds
/usr/lib64/R/library/fastcluster/Meta/vignette.rds
/usr/lib64/R/library/fastcluster/NAMESPACE
/usr/lib64/R/library/fastcluster/NEWS.md
/usr/lib64/R/library/fastcluster/R/fastcluster
/usr/lib64/R/library/fastcluster/R/fastcluster.rdb
/usr/lib64/R/library/fastcluster/R/fastcluster.rdx
/usr/lib64/R/library/fastcluster/doc/fastcluster.Rtex
/usr/lib64/R/library/fastcluster/doc/fastcluster.pdf
/usr/lib64/R/library/fastcluster/doc/index.html
/usr/lib64/R/library/fastcluster/help/AnIndex
/usr/lib64/R/library/fastcluster/help/aliases.rds
/usr/lib64/R/library/fastcluster/help/fastcluster.rdb
/usr/lib64/R/library/fastcluster/help/fastcluster.rdx
/usr/lib64/R/library/fastcluster/help/paths.rds
/usr/lib64/R/library/fastcluster/html/00Index.html
/usr/lib64/R/library/fastcluster/html/R.css
/usr/lib64/R/library/fastcluster/tests/test_fastcluster.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fastcluster/libs/fastcluster.so
/usr/lib64/R/library/fastcluster/libs/fastcluster.so.avx2
/usr/lib64/R/library/fastcluster/libs/fastcluster.so.avx512
