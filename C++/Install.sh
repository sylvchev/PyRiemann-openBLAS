#!/bin/bash

#Uninstall any previous libopenblas
sudo apt-get remove libopenblas-base

#Install liblapack
sudo apt-get install liblapack-dev

#Build and install OpenBlas
rm -rf OpenBLAS
git clone git://github.com/xianyi/OpenBLAS
cd OpenBLAS
make
sudo make install
cd..
rm -rf OpenBLAS

#Build and install Armadillo
cd Armadillo
rm -f CMakeCache.txt
cmake .
make
sudo make install
cd ..

#Compile everything
./Compile.sh