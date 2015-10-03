#!/bin/bash


#install and remove package
sudo apt-get remove libopenblas* liblapack*
sudo apt-get install python3 python3-dev python3-numpy python3-scipy cython3 gcc gfortran


#install OpenBLAS
git clone git://github.com/xianyi/OpenBLAS
cd OpenBLAS
make
sudo make install
cd ..
sudo rm -rf OpenBLAS
export BLAS=/opt/OpenBLAS/lib/libopenblas.so
export LAPACK=/opt/OpenBLAS/lib/libopenblas.so
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/OpenBLAS/lib


#permanant export
echo -e "export BLAS=/opt/OpenBLAS/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LAPACK=/opt/OpenBLAS/lib/libopenblas.so" >> ~/.bashrc
echo -e "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/opt/OpenBLAS/lib" >> ~/.bashrc