#!/bin/bash

# INSTALL BOILERPLATE
sudo yum update
sudo yum upgrade

sudo yum install nodejs
sudo yum install npm

if ! command -v npm
then
	echo "ERROR: npm not found"
	exit
fi

# DEFAULT REACT APP
npm install -g create-react-app
create-react-app --version

# INSTALL DOCKER
if command -v docker
then
	echo "docker is installed. No action needed."
else
	sudo dnf install docker
	sudo systemctl start docker
	sudo docker run hello-world
	while true; do
		read -p "Do you wish to enable docker daemon? Y/n" yn
		case $yn in
			[Yy]* ) sudo systemctl enable docker; break;;
			[Nn]* ) break;;
			* ) echo "Please answer Y/n";;
		esac
	done
	while true; do
		read -p "Do you wish to add user to docker group? Y/n" yn
		case $yn in
			[Yy]* ) sudo groupadd docker && sudo gpasswd -a ${USER} docker && sudo systemctl restart docker; break;;
			[Nn]* ) break;;
			* ) echo "Please answer Y/n";;
		esac
	done
fi

# INSTALL SNAP STORE (PREREQUISITE TO KUBE)
sudo dnf install snapd
sudo ln -s /var/lib/snapd/snap /snap

# INSTALL MICROK8S
sudo snap install microk8s --classic
snap alias microk8s.kubectl kubectl
microk8s status
