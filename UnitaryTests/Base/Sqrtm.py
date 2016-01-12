import os
import sys

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat
from oldPyRiemann.base import sqrtm


def test_sqrtm():
    numpy_array = numpy.array([[2, 1, 0], [1, 2, 0], [0, 0, 3]])
    if (CovMat(numpy_array).sqrtm - CovMat(sqrtm(numpy_array))).norm() < 1e-10:
        print("sqrtm: PASS")
        return True
    else:
        print("sqrtm: FAIL")
        return False
