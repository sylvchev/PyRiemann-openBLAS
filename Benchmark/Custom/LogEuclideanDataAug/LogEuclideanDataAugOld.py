import numpy
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

import Utils.OpenBLAS
from oldPyRiemann.mean import mean_logeuclid
from oldPyRiemann.geodesic import geodesic_logeuclid


def compute(matrice_order, loop_number):
    tmp = numpy.random.rand(matrice_order, 2 * matrice_order)
    a = numpy.dot(tmp, tmp.T) / 1000

    l = [a]
    covmats = numpy.array(l)

    for i in range(0, loop_number):
        mean = mean_logeuclid(covmats)
        l += [geodesic_logeuclid(covmats[j, :, :], mean) for j in range(covmats.shape[0])]
        covmats = numpy.array(l)
