#!/bin/bash

#Install librairies
sudo apt-get install cmake
sudo apt-get install libopenblas-dev
sudo apt-get install liblapack-dev
sudo apt-get install libarpack-dev
sudo apt-get update
#sudo apt-get upgrade

#Build and install Armadillo
cd Armadillo
rm -f CMakeCache.txt
cmake .
make
sudo make install
cd ..

#Compile everything
./Compile.sh
