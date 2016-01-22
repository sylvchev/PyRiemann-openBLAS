import os
import sys

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat
from oldPyRiemann.base import powm


def test_powm():
    numpy_array = numpy.array([[2, 1, 0], [1, 2, 0], [0, 0, 3]])
    if (CovMat(numpy_array).powm(5) - CovMat(powm(numpy_array, 5))).norm() < 1e-10:
        print("powm: PASS")
        return True
    else:
        print("powm: FAIL")
        return False
