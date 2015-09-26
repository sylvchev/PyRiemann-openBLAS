#!/bin/bash

#Install librairies
sudo apt-get install libopenblas-dev liblapack-dev python3 python3-numpy python3-scipy

#Build and install Armadillo
echo -e "" >> ~/.bashrc
echo -e "alias python=\"python3.4\"" >> ~/.bashrc
