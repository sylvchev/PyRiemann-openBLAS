import numpy
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

import Utils.OpenBLAS
from oldPyRiemann.mean import mean_riemann
from oldPyRiemann.geodesic import geodesic_riemann


def compute(matrice_order, loop_number):
    tmp = numpy.random.rand(matrice_order, 2 * matrice_order)
    a = numpy.dot(tmp, tmp.T) / 1000
    tmp = numpy.random.rand(matrice_order, 2 * matrice_order)
    b = numpy.dot(tmp, tmp.T) / 1000

    l = [a, b]
    covmats = numpy.array(l)

    for i in range(0, loop_number):
        mean = mean_riemann(covmats)
        l += [geodesic_riemann(covmats[j, :, :], mean) for j in range(covmats.shape[0])]
        covmats = numpy.array(l)
