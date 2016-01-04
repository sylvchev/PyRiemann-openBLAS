import os
import sys

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Utils.CovMat import CovMat
from oldPyRiemann.base import invsqrtm


def test_invsqrtm():
    numpy_array = numpy.array([[2, 1, 0], [1, 2, 0], [0, 0, 3]])
    if (CovMat(numpy_array).invsqrtm - CovMat(invsqrtm(numpy_array))).norm < 1e-10:
        print("invsqrtm: PASS")
        return True
    else:
        print("invsqrtm: FAIL")
        return False


