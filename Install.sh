#!/bin/bash


#install OpenBLAS
sudo apt-get install gcc g++ gfortran
git clone git://github.com/xianyi/OpenBLAS
cd OpenBLAS
make
sudo make install
cd ..
sudo rm -rf OpenBLAS


#install and remove package
sudo apt-get remove libopenblas* liblapack*
sudo apt-get install python3 python3-numpy python3-scipy 


#export and permanant export
export BLAS=/opt/OpenBLAS/lib/libopenblas.so
export LAPACK=/opt/OpenBLAS/lib/libopenblas.so
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/OpenBLAS/lib
echo -e "export BLAS=/opt/OpenBLAS/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LAPACK=/opt/OpenBLAS/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/opt/OpenBLAS/lib" >> ~/.bashrc