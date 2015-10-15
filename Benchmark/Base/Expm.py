#!/usr/bin/python

import time
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "PyRiemann")))

from Utils.CovMat import CovMat


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
warm_up_covmat = CovMat.random(2500)
warm_up_covmat.expm

print_progress(0)

for i in range(0, len(size)):
    for j in range(0, nb_repet):
        covmat = CovMat.random(size[i])
        start = time.time()
        covmat.expm
        tps[i] += time.time() - start
        print_progress(round((i * nb_repet + j) * 100 / (nb_repet * len(size)), 2))

print_progress(100)

for i in range(0, len(size)):
    tps[i] /= nb_repet
    print("CovMat size : " + str(size[i]) + "x" + str(size[i]) + "	time : " + str(tps[i]) + " sec")
