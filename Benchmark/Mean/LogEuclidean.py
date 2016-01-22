import os
import sys
import timeit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat
from Utils.CovMats import CovMats

size = [10, 25, 50, 75, 100, 250, 500, 750, 1000]

# WARMUP
print("Warm up...")
for i in range(0, 10):
    warm_up_covmat = CovMat.random(1000)
    warm_up_covmat.expm

for i in range(0, len(size)):
    covmats = CovMats.random(10, size[i])

    t = timeit.Timer("mean_logeuclid(covmats.numpy_array)",
                     setup="from __main__ import covmats; from oldPyRiemann.mean import mean_logeuclid; import Utils.OpenBLAS")
    old_time = t.timeit(number=size[len(size) - i - 1]) / size[len(size) - i - 1]

    t = timeit.Timer("covmats.reset_fields(); Mean.log_euclidean(covmats)",
                     setup="from Utils.Mean import Mean; from __main__ import covmats")
    new_time = t.timeit(number=size[len(size) - i - 1]) / size[len(size) - i - 1]

    print("matrix size : " + "10x" + str(size[i]) + "x" + str(size[i]) + "\t\told time : " + str(
        old_time) + " sec\t\t" + "new time : " + str(new_time) + " sec\t\t" + "speed up : " + str(
        old_time / new_time))
