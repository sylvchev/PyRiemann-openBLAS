#!/bin/bash


#install OpenBLAS
sudo apt-get install gcc g++ gfortran
git clone git://github.com/xianyi/OpenBLAS
cd OpenBLAS
echo -e "Building OpenBLAS, please wait (this can take several minutes)"
make FC=gfortran > tmp
rm -rf tmp
sudo make install PREFIX=/usr/local
cd ..
sudo rm -rf OpenBLAS


#export and permanant export
export BLAS=/usr/local/lib/libopenblas.so
export LAPACK=/usr/local/lib/libopenblas.so
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
echo -e "export BLAS=/usr/local/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LAPACK=/usr/local/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/lib" >> ~/.bashrc


#install and remove package
sudo apt-get remove libopenblas* liblapack*
sudo apt-get install python3 python3-dev python3-pip
sudo pip3 uninstall numpy scipy
sudo pip3 install numpy scipy
