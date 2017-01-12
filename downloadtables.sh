#!/bin/bash

DIR='html/'
SRC='http://www.spanishdict.com/conjugate/'
TIMEOUT=2  # Delay in seconds to prevent clobbering server

for v in `cat $1`; {
	OUTFILENAME=${DIR}${v}
	URL=${SRC}${v}

	if [ ! -f $OUTFILENAME ]
	then
		wget -O $OUTFILENAME $URL
		sleep $TIMEOUT
	fi
}
