FROM ubuntu:14.04

MAINTAINER sylvchev "https://github.com/sylvchev"

# Install packages for building OpenBLAS
RUN apt-get update
RUN apt-get remove -y libopenblas* liblapack*
RUN apt-get install -y --force-yes gcc gfortran git
RUN apt-get clean
# RUN export CC="gcc -w"
# RUN export FC="gfortran -w"
# RUN git clone -q git://github.com/xianyi/OpenBLAS
RUN git clone git://github.com/xianyi/OpenBLAS
RUN ls /root
RUN cd /root/OpenBLAS; make; make install PREFIX=/usr/local
RUN rm -rf /root/OpenBLAS
# Install Python, numpy and scipy
RUN apt-get -y --force-yes install python3 python3-dev python3-pip g++
RUN apt-get -y --force-yes remove python3-numpy python3-scipy
RUN yes | sudo pip3 install -q numpy
RUN yes | sudo pip3 install -q scipy

RUN git clone https://github.com/sylvchev/PyRiemannEigen /root/pyriem