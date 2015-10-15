#!/bin/bash


#install OpenBLAS
echo -e "Removing current libopenblas and liblapack packages"
sudo apt-get -y remove libopenblas* liblapack* 2>&1 >/dev/null

echo -e "Installing prerequisite packages for OpenBLAS : gcc & gfortran"
sudo apt-get -y install gcc gfortran git 2>&1 >/dev/null
export CC="gcc -w"
export FC="gfortran -w"

echo -e "Downloading OpenBLAS : cloning from Github"
git clone -q git://github.com/xianyi/OpenBLAS

echo -e "Building OpenBLAS (this can take several minutes)"
cd OpenBLAS
make -s 2>&1 >/dev/null

echo -e "Installing OpenBLAS at /usr/local"
sudo make install PREFIX=/usr/local 2>&1 >/dev/null

echo -e "Cleaning"
cd ..
sudo rm -rf OpenBLAS



#export and permanant export
export BLAS=/usr/local/lib/libopenblas.so
export LAPACK=/usr/local/lib/libopenblas.so
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
echo -e "" >> ~/.bashrc
echo -e "export BLAS=/usr/local/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LAPACK=/usr/local/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/lib" >> ~/.bashrc



#install python numpy and scipy
echo -e "Installing python prerequisite packages : python3 python3-dev python3-pip g++"
sudo apt-get -y install python3 python3-dev python3-pip g++ 2>&1 >/dev/null

echo -e "Removing current numpy and scipy packages"
sudo apt-get -y remove python3-numpy python3-scipy 2>&1 >/dev/null
yes | sudo pip3 uninstall -q numpy 2>&1 >/dev/null
yes | sudo pip3 uninstall -q scipy 2>&1 >/dev/null

echo -e "Downloading, compiling and installing numpy package (this can take several minutes)"
yes | sudo BLAS=$BLAS LAPACK=$LAPACK LD_LIBRARY_PATH=$LD_LIBRARY_PATH pip3 install -q numpy 2>&1 >/dev/null

echo -e "Downloading, compiling and installing scipy package (this can take several minutes)"
yes | sudo BLAS=$BLAS LAPACK=$LAPACK LD_LIBRARY_PATH=$LD_LIBRARY_PATH pip3 install -q scipy 2>&1 >/dev/null
