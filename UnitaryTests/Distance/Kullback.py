import os
import sys
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.Distance import Distance
from Utils.CovMat import CovMat
from oldPyRiemann.distance import distance_kullback, distance_kullback_right, distance_kullback_sym


A = numpy.random.rand(100)
B = numpy.random.rand(100)
m1 = CovMat.random(10)
m2 = CovMat.random(10)

def test_distance_kullback():
    old_dist = distance_kullback(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.kullback(m1, m2)

    return _get_state(old_dist, new_dist, "kullback")


def test_distance_kullback_right():
    old_dist = distance_kullback_right(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.kullback_right(m1, m2)

    return _get_state(old_dist, new_dist, "kullback right")


def test_distance_kullback_sym():
    old_dist = distance_kullback_sym(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.kullback_sym(m1, m2)

    return _get_state(old_dist, new_dist, "kullback sym")


def _get_state(old, new, func_name):
    if abs( old - new ) < 1e-10:
        print("%s : PASS")
        return True
    else:
        print("%s : FAIL")
        return False