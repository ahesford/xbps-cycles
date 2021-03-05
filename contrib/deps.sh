#!/bin/sh

# usage: 
# cd $XBPS_DISTDIR
# ./deps.sh [n]
# ./loops.py builddeps $XBPS_DISTDIR/srcpkgs

nproc=${1:-4}

mkdir -p builddeps
find srcpkgs -mindepth 1 -maxdepth 1 | cut -d/ -f2 | xargs -n 1 -P ${nproc} -I {} sh -c 'echo " {}"; ./xbps-src show-build-deps {} > builddeps/{}'
