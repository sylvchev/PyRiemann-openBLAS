import numpy
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Utils.OpenBLAS


class DataType(object):
    float32 = numpy.float32
    float64 = numpy.float64
    float = numpy.float32
    double = numpy.float64
