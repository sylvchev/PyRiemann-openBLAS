#!/bin/bash


#install OpenBLAS
echo -e "Removing current libopenblas and liblapack packages"
sudo apt-get -y remove libopenblas* liblapack* 2>&1 >/dev/null

echo -e "Installing prerequisite packages for OpenBLAS : gcc & gfortran"
sudo apt-get -y install gcc gfortran 2>&1 >/dev/null
export CC="gcc -w"
export FC="gfortran -w"

echo -e "Downloading OpenBLAS : cloning from Github"
git clone -q git://github.com/xianyi/OpenBLAS

echo -e "Building OpenBLAS, please wait (this can take several minutes)"
cd OpenBLAS
make -s 2>&1 >/dev/null

echo -e "Installing OpenBLAS at /usr/local"
sudo make install PREFIX=/usr/local 2>&1 >/dev/null

echo -e "Cleaning"
cd ..
sudo rm -rf OpenBLAS


#install python numpy and scipy
echo -e "Installing python prerequisite packages : python3 python3-dev python3-pip g++"
sudo apt-get -y install python3 python3-dev python3-pip g++ 2>&1 >/dev/null

echo -e "Removing current numpy and scipy packages"
sudo apt-get -y remove python3-numpy python3-scipy 2>&1 >/dev/null
yes | sudo pip3 uninstall -q numpy scipy 2>&1 >/dev/null

echo -e "Downloading, compiling and installing numpy package (this can take several minutes)"
yes | sudo pip3 install -q numpy 2>&1 >/dev/null

echo -e "Downloading, compiling and installing scipy package (this can take several minutes)"
yes | sudo pip3 install -q scipy 2>&1 >/dev/null
