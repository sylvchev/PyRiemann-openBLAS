import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from Utils.CovMat import CovMat
from Utils.CovMats import CovMats
from Utils.Mean import Mean
from Utils.Geodesic import Geodesic


def compute(matrice_order, loop_number):
    a = CovMat.random(matrice_order)
    b = CovMat.random(matrice_order)
    covmats = CovMats([a, b])

    for i in range(0, loop_number):
        mean = Mean.riemannian(covmats)

        l = []
        for j in range(0, covmats.length):
            l.append(Geodesic.riemannian(covmats[j], mean))

        covmats.append(l)
