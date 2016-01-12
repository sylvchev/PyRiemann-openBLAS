import os
import sys
import numpy
from Utils.Distance import Distance
from Utils.CovMat import CovMat
from oldPyRiemann.distance import distance_logdet, distance_logeuclid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

A = numpy.random.rand(100)
B = numpy.random.rand(100)
m1 = CovMat.random(10)
m2 = CovMat.random(10)


def test_distance_logdet():
    old_dist = distance_logdet(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.log_determinant(m1, m2) # TypeError: unsupported operand type(s) for /: 'CovMat' and 'float'
    #new_dist = Distance.log_determinant(m1.numpy_array, m2.numpy_array) # AttributeError: 'numpy.ndarray' object has no attribute 'determinant

    return _get_state(old_dist, new_dist, "log determinant")


def test_log_euclidean():
    old_dist = distance_logeuclid(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.log_euclidean(m1, m2)

    return _get_state(old_dist, new_dist, "log euclidean")


def _get_state(old, new, func_name):
    if abs( old - new ) < 1e-10:
        print("%s : PASS")
        return True
    else:
        print("%s : FAIL")
        return False