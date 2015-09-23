#!/bin/bash

#Install librairies
sudo apt-get install g++-4.9
sudo apt-get install cmake
sudo apt-get install libopenblas-dev
sudo apt-get install liblapack-dev
sudo rm -rf /usr/include/armadillo*
sudo rm -rf /usr/local/include/armadillo*
sudo rm -rf /usr/lib/libarmadillo.so*
sudo rm -rf /usr/local/lib/libarmadillo.so*

#Build and install Armadillo
wget http://sourceforge.net/projects/arma/files/armadillo-5.600.2.tar.gz
tar -xvf armadillo-5.600.2.tar.gz
rm armadillo-5.600.2.tar.gz
cd armadillo-5.600.2
./configure
make
sudo make install
cd ..
rm -rf armadillo-5.600.2

#Compile everything
./Compile.sh
