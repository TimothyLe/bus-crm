#!/bin/bash

if ! command -v microk8s
then
	echo "ERROR: microk8s not found"
	exit
fi

# ENABLE REQUIRED SERVICES FOR KUBERNETES
microk8s enable dns dashboard

# SPECIFY DOCKER IMAGE
while [[ $# -gt 0 ]] && [[ "$1" == "--"* ]] ;
do
    opt="$1";
    # EXPOSE NEXT ARGUMENT
    shift;             
    case "$opt" in
        "--image=*" )
	   # TAKE OPTION
           IMAGE="${opt#*=}";;
        *) echo >&2 "Invalid option: $@"; exit 1;;
   esac
done
microk8s ctr image import "$IMAGE"

# FIND IMAGE NAME BEFORE *.tar
if microk8s ctr images ls | grep -q "${IMAGE##*.}"
then
	echo "Image imported sucessfully"
fi

# CREATE DEPLOYMENT
kubectl apply -f deployment.yaml

# SCALE AND LOAD BALANCE
#kubectl get pods
#kubectl get deployments
#kubectl get all

# EXPOSE DEPLOYMENT
EXTERNAL_IP="192.168.26.133"
SERVICE_NAME="whipcrm-deployment-service"
#kubectl expose deployment ${IMAGE##*.} --type LoadBalancer --name "$SERVICE_NAME" --external-ip="$EXTERNAL_IP"

# LOADBALANCER IP
#kubectl get all | grep LoadBalancer | cut -f 3-4
# curl http://$EXTERNAL_IP:$PORT
