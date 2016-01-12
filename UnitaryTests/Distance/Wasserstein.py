import os
import sys
import numpy

from Utils.Distance import Distance
from Utils.CovMat import CovMat
from oldPyRiemann.distance import distance_wasserstein

m1 = CovMat.random(10)
m2 = CovMat.random(10)


def test_distance_wasserstein():
    old_dist = distance_wasserstein(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.wasserstein(m1, m2)

    return _get_state(old_dist, new_dist, "wasserstein")


def _get_state(old, new, func_name):
    if abs( old - new ) < 1e-10:
        print("%s : PASS" % func_name)
        return True
    else:
        print("%s : FAIL" % func_name)
        return False