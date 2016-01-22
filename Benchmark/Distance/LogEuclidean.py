import os
import sys
import timeit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat

size = [10, 25, 50, 75, 100, 250, 500, 750, 1000]

# WARMUP
print("Warm up...")
for i in range(0, 10):
    warm_up_covmat = CovMat.random(1000)
    warm_up_covmat.expm

for i in range(0, len(size)):
    covmat1 = CovMat.random(size[i])
    covmat2 = CovMat.random(size[i])

    t = timeit.Timer("distance_logeuclid(covmat1.numpy_array, covmat2.numpy_array)",
                     setup="from __main__ import covmat1; from __main__ import covmat2; from oldPyRiemann.distance import distance_logeuclid; import Utils.OpenBLAS")
    old_time = t.timeit(number=size[len(size) - i - 1]) / size[len(size) - i - 1]

    covmat1 = CovMat.random(size[i])
    covmat2 = CovMat.random(size[i])
    t = timeit.Timer("covmat1.reset_fields(); covmat2.reset_fields(); Distance.log_euclidean(covmat1, covmat2)",
                     setup="from Utils.Distance import Distance; from __main__ import covmat1; from __main__ import covmat2")
    new_time = t.timeit(number=size[len(size) - i - 1]) / size[len(size) - i - 1]

    print("matrix size : " + str(size[i]) + "x" + str(size[i]) + "\t\told time : " + str(
        old_time) + " sec\t\t" + "new time : " + str(new_time) + " sec\t\t" + "speed up : " + str(
        old_time / new_time))
