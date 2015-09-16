#!/bin/bash

sudo apt-get install libopenblas-dev
sudo apt-get install libopenblas-base
sudo apt-get install liblapack-dev

#Build and install Eigen
cd Armadillo
cmake .
make
sudo make install
cd ..

#Compile everything
./Compile.sh