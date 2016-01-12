import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat
from Utils.Distance import Distance
from oldPyRiemann.distance import distance_euclid

def test_euclidean():
    m1 = CovMat.random(10)
    m2 = CovMat.random(10)
    old_dist = distance_euclid(m1.numpy_array, m2.numpy_array)
    m1.reset_fields()
    m2.reset_fields()
    new_dist = Distance.euclidean(m1, m2)

    if abs( old_dist - new_dist ) < 1e-10:
        print("euclid: PASS")
        return True
    else:
        print("euclid: FAIL")
        return False