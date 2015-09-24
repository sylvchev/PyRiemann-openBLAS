#!/bin/bash

#Install librairies
sudo apt-get install libopenblas-dev
sudo apt-get install liblapack-dev
sudo apt-get install python3
sudo apt-get install python3-numpy
sudo apt-get install python3-scipy

#Build and install Armadillo
echo -e "" >> ~/.bashrc
echo -e "alias python=\"python3.4\"" >> ~/.bashrc
