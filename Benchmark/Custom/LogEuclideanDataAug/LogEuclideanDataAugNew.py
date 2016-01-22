import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from Utils.CovMats import CovMats
from Utils.Mean import Mean
from Utils.Geodesic import Geodesic


def compute(matrice_order, loop_number):
    covmats = CovMats.random(1, matrice_order)

    for i in range(0, loop_number):
        mean = Mean.log_euclidean(covmats)
        covmats.add_all([Geodesic.log_euclidean(covmat, mean) for covmat in covmats])
