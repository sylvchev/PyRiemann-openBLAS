#!/bin/bash

#Install librairies
sudo apt-get remove libopenblas*
sudo apt-get remove liblapack*
sudo rm -rf /usr/include/armadillo*
sudo rm -rf /usr/local/include/armadillo*
sudo rm -rf /usr/lib/libarmadillo.so*
sudo rm -rf /usr/local/lib/libarmadillo.so*

#Build ans install OpenBLAS
rm -rf OpenBLAS
git clone git://github.com/xianyi/OpenBLAS
mv OpenBLAS tmp
cd tmp
make
make install PREFIX=../OpenBLAS
cd ..
rm -rf tmp

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
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:`pwd`/OpenBLAS/lib
./Compile.sh
