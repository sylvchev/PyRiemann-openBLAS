FROM ubuntu:14.04

MAINTAINER sylvchev "https://github.com/sylvchev"

# Install packages for building OpenBLAS
RUN apt-get update 2>&1 >/dev/null
RUN apt-get remove -y libopenblas* liblapack* 2>&1 >/dev/null
RUN apt-get install -y --force-yes gcc gfortran git build-essential 2>&1 >/dev/null
RUN apt-get clean 2>&1 >/dev/null
RUN git clone git://github.com/xianyi/OpenBLAS /root/OpenBLAS
RUN cd /root/OpenBLAS; make -s 2>&1 >/dev/null; make install PREFIX=/usr 
RUN rm -rf /root/OpenBLAS
# Install Python, numpy and scipy
RUN apt-get -y --force-yes install python3 python3-dev python3-pip g++ 2>&1 >/dev/null
RUN apt-get -y --force-yes remove python3-numpy python3-scipy 2>&1 >/dev/null
RUN yes | sudo pip3 install -q numpy
RUN yes | sudo pip3 install -q scipy

RUN git clone https://github.com/sylvchev/PyRiemannEigen /root/pyriem