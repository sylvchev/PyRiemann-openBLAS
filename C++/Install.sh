#!/bin/bash

#Install librairies
sudo apt-get install cmake
sudo apt-get remove libopenblas*
sudo apt-get remove liblapack*
sudo rm -rf /usr/include/armadillo*
sudo rm -rf /usr/local/include/armadillo*
sudo rm -rf /usr/lib/libarmadillo.so*
sudo rm -rf /usr/local/lib/libarmadillo.so*

#Build and install OpenBLAS
rm -rf OpenBLAS
rm -rf tmp
git clone git://github.com/xianyi/OpenBLAS
mv OpenBLAS tmp
cd tmp
make
make install PREFIX=../OpenBLAS
cd ..
rm -rf tmp

#Build and install LAPACK
rm -rf LAPACK
rm -rf lapack-3.5.0
wget http://www.netlib.org/lapack/lapack-3.5.0.tgz
tar -xvf lapack-3.5.0.tgz
cd lapack-3.5.0
tar -xvf lapack-3.5.0.tar
cd lapack-3.5.0
cmake .
make make install PREFIX=../../LAPACK
rm -rf lapack-3.5.0

#Build and install Armadillo
wget http://sourceforge.net/projects/arma/files/armadillo-5.600.2.tar.gz
tar -xvf armadillo-5.600.2.tar.gz
rm armadillo-5.600.2.tar.gz
cd armadillo-5.600.2
cmake .
make
sudo make install
cd ..
rm -rf armadillo-5.600.2

#Compile everything
./Compile.sh
