#!/bin/bash

#Install librairies
sudo apt-get install cmake
sudo apt-get remove libopenblas-base
sudo apt-get remove libopenblas-dev
sudo apt-get remove liblapack-dev

#Build ans install OpenBLAS
git clone git://github.com/xianyi/OpenBLAS
cd OpenBLAS
make FC=gfortran
sudo make install

#Build and install Armadillo
cd Armadillo
rm -f CMakeCache.txt
cmake .
make
sudo make install
cd ..

#Compile everything
./Compile.sh
