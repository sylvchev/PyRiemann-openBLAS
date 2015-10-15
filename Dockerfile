FROM ubuntu:14.04

MAINTAINER sylvchev "https://github.com/sylvchev"

# Install packages for building OpenBLAS
RUN apt-get update &> /dev/null
RUN apt-get remove -y libopenblas* liblapack* 
RUN apt-get install -y --force-yes gcc gfortran git build-essential
# &> /dev/null
RUN apt-get clean 
RUN git clone git://github.com/xianyi/OpenBLAS /root/OpenBLAS
RUN cd /root/OpenBLAS; make -s &> /dev/null; make install PREFIX=/usr
RUN rm -rf /root/OpenBLAS
# RUN ln -s /usr/lib/libopenblas.so /usr/local/lib/libopenblas.so
# Install Python, numpy and scipy
RUN apt-get -y --force-yes install python3 python3-dev python3-pip g++
RUN apt-get -y --force-yes remove python3-numpy python3-scipy
RUN yes | sudo pip3 install -q numpy
RUN yes | sudo pip3 install -q scipy

RUN git clone https://github.com/sylvchev/PyRiemannEigen /root/pyriem