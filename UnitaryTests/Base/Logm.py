import os
import sys

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat
from oldPyRiemann.base import logm


def test_logm():
    numpy_array = numpy.array([[2, 1, 0], [1, 2, 0], [0, 0, 3]])
    if (CovMat(numpy_array).logm - CovMat(logm(numpy_array))).norm() < 1e-10:
        print("logm: PASS")
        return True
    else:
        print("logm: FAIL")
        return False

