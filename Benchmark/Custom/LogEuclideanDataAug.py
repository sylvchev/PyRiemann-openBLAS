import os
import sys
import timeit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat

# WARMUP
print("Warm up...")
for i in range(0, 10):
    warm_up_covmat = CovMat.random(1000)
    warm_up_covmat.expm

size = [10, 25, 50, 75, 100, 250, 500]
matrix_order = 0

for i in range(0, len(size)):
    matrix_order = size[i]
    t = timeit.Timer("compute(matrix_order, 5)",
                     setup="from Benchmark.Custom.LogEuclideanDataAug.LogEuclideanDataAugNew import compute; from __main__ import matrix_order")
    old_time = t.timeit(number=5) / 5

    t = timeit.Timer("compute(matrix_order, 5)",
                     setup="from Benchmark.Custom.LogEuclideanDataAug.LogEuclideanDataAugNew import compute; from __main__ import matrix_order")
    new_time = t.timeit(number=5) / 5

    print("matrix size : " + str(size[i]) + "x" + str(size[i]) + "\t\told time : " + str(
        old_time) + " sec\t\t" + "new time : " + str(new_time) + " sec\t\t" + "speed up : " + str(
        old_time / new_time))
