#!/bin/bash


#install OpenBLAS
echo -e "Installing prerequisites for OpenBLAS : gcc & gfortran"
sudo apt-get -y install gcc gfortran 2>&1 >/dev/null

echo -e "Downloading OpenBLAS : cloning from Github"
git clone -q git://github.com/xianyi/OpenBLAS

echo -e "Building OpenBLAS, please wait (this can take several minutes)"
cd OpenBLAS
make -s FC=gfortran 2>&1 >/dev/null

echo -e "Installing OpenBLAS at /usr/local"
sudo make install PREFIX=/usr/local 2>&1 >/dev/null

echo -e "Cleaning"
cd ..
sudo rm -rf OpenBLAS


#export and permanant export
export BLAS=/usr/local/lib/libopenblas.so
export LAPACK=/usr/local/lib/libopenblas.so
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
echo -e "export BLAS=/usr/local/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LAPACK=/usr/local/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/lib" >> ~/.bashrc


#install and remove package
sudo apt-get remove libopenblas* liblapack*
sudo apt-get install python3 python3-dev python3-pip
yes | sudo pip3 uninstall -q numpy scipy
yes | sudo pip3 install -q numpy scipy
