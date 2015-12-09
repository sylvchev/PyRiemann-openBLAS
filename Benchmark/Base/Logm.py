import os
import sys
import timeit
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat

size = [10, 25, 50, 75, 100, 250, 500, 750, 1000]

# WARMUP
print("Warm up...")
for i in range(0, 10):
    warm_up_covmat = CovMat.random(1000)
    warm_up_covmat.logm

for i in range(0, len(size)):
    A = numpy.random.rand(size[i], 2 * size[i])
    covmat = numpy.dot(A, A.T) / 1000
    t = timeit.Timer("logm(covmat)",
                     setup="from __main__ import covmat; from oldPyRiemann.base import logm; import Utils.OpenBLAS")
    old_time = t.timeit(number=size[len(size) - i - 1]) / size[len(size) - i - 1]

    covmat = CovMat.random(size[i])
    t = timeit.Timer("covmat.reset_fields(); covmat.logm", setup="from __main__ import covmat")
    new_time = t.timeit(number=size[len(size) - i - 1]) / size[len(size) - i - 1]

    print("matrix size : " + str(size[i]) + "x" + str(size[i]) + "\t\told time : " + str(
        old_time) + " sec\t\t" + "new time : " + str(new_time) + " sec\t\t" + "speed up : " + str(
        old_time / new_time))
