#!/usr/bin/python

import sys
import os
import time
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from oldPyRiemann.base import expm

def print_progress(i):
    text = "Progress : " + str(i) + "%"
    sys.stdout.write(" " * 20)
    sys.stdout.write("\b" * 20)
    sys.stdout.write(text)
    sys.stdout.write("\b" * len(text))
    sys.stdout.flush()


nb_repet = 5
size = [10, 25, 50, 75, 100, 250, 500, 750, 1000]
tps = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# WARMUP
print("Warm up...")
for i in range(0, 10) :
    A = numpy.random.rand(1000, 2000)
    warm_up_covmat = numpy.dot(A, numpy.transpose(A))/1000
    expm(warm_up_covmat)

for i in range(0, len(size)):
    A = numpy.random.rand(size[i], 2*size[i])/1000
    covmat = numpy.dot(A, numpy.transpose(A))
    for j in range(0, nb_repet):
        print_progress(round((i * nb_repet + j) * 100 / (nb_repet * len(size)), 2))
        start = time.time()
        expm(covmat)
        tps[i] += time.time() - start

print_progress(100)

for i in range(0, len(size)):
    tps[i] /= nb_repet
    print("CovMat size : " + str(size[i]) + "x" + str(size[i]) + "	time : " + str(tps[i]) + " sec")
