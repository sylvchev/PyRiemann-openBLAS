#!/bin/bash

#Build and install Eigen
mkdir EigenBuild
cd EigenBuild
cmake ../Eigen
sudo make install
cd ..
rm -rf EigenBuild

#Compile everything
./Compile.sh