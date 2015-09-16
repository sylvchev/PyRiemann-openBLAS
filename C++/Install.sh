#!/bin/bash

#Install libopenblas et liblapack
sudo apt-get install libopenblas-base
sudo apt-get install libopenblas-dev
sudo apt-get install liblapack-dev

#Build and install Armadillo
cd Armadillo
rm -f CMakeCache.txt
cmake .
make
sudo make install
cd ..

#Compile everything
./Compile.sh
