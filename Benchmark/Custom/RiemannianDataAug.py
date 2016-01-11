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

t = timeit.Timer("compute(100, 10)",
                 setup="from Benchmark.Custom.RiemannianDataAug.RiemannianDataAugOld import compute")
old_time = t.timeit(number=2) / 2

t = timeit.Timer("compute(100, 10)",
                 setup="from Benchmark.Custom.RiemannianDataAug.RiemannianDataAugNew import compute")
new_time = t.timeit(number=2) / 2

print("matrix size : " + str(100) + "x" + str(100) + "\t\told time : " + str(
    old_time) + " sec\t\t" + "new time : " + str(new_time) + " sec\t\t" + "speed up : " + str(
    old_time / new_time))
