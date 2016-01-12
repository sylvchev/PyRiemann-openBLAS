import os
import sys
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMats import CovMats
from Utils.Mean import Mean
from oldPyRiemann.mean import mean_logdet, mean_logeuclid


def test_mean_log_determinant():
    covmats = CovMats.random(10, 10)
    old_dist = mean_logdet(covmats.numpy_array)
    covmats.reset_fields()
    new_dist = Mean.log_determinant(covmats)

    return _get_state(old_dist, new_dist, "mean log determinant")


def test_mean_log_euclidean():
    covmats = CovMats.random(10, 10)
    old_dist = mean_logeuclid(covmats.numpy_array)
    covmats.reset_fields()
    new_dist = Mean.log_euclidean(covmats)

    return _get_state(old_dist, new_dist, "mean log euclidian")



def _get_state(old, new, func_name):
    if abs(old.sum() - new.sum()) < 1e-10:
        print("%s : PASS" % func_name)
        return True
    else:
        print("%s : FAIL" % func_name)
        return False
