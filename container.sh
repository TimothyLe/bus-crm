#!/bin/bash

if ! command -v docker
then
	echo "ERROR: docker not found"
	exit
fi

# BUILD DOCKER IMAGE
docker build -t whipcrm-app .

# VERIFY IMAGE
#docker run -it whipcrm-app bash

# EXPORT IMAGE
docker save whipcrm-app > whipcrm-app.tar
