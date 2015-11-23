import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat
from Utils.CovMats import CovMats
from Utils.Mean import Mean


def print_progress(i):
    text = "Progress : " + str(i) + "%"
    sys.stdout.write(" " * 20)
    sys.stdout.write("\b" * 20)
    sys.stdout.write(text)
    sys.stdout.write("\b" * len(text))
    sys.stdout.flush()


nb_repet = 5
size = [10, 25, 50, 75, 100, 250, 500, 750, 1000]
nb_covmats = 10
tps = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# WARMUP
print("Warm up...")
for i in range(0, 10):
    warm_up_covmat = CovMat.random(1000)
    warm_up_covmat.sqrtm

for i in range(0, len(size)):
    covmats = CovMats.random(size[i], nb_covmats)
    for j in range(0, nb_repet):
        print_progress(round((i * nb_repet + j) * 100 / (nb_repet * len(size)), 2))
        covmats.reset_matrices_fields()
        start = time.time()
        Mean.log_determinant(covmats)
        tps[i] += time.time() - start

print_progress(100)

for i in range(0, len(size)):
    tps[i] /= nb_repet
    print("CovMats size : " + str(nb_covmats) + "x" + str(size[i]) + "x" + str(size[i]) + "	time : " + str(tps[i]) + " sec")
