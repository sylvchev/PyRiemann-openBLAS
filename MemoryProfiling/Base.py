import os
import sys
import numpy
from memory_profiler import profile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMat import CovMat
from oldPyRiemann.base import sqrtm, invsqrtm, expm, logm, powm


@profile()
def function():
    covmat = CovMat.random(100)
    sqrtm = covmat.sqrtm
    invsqrtm = covmat.invsqrtm
    expm = covmat.expm
    logm = covmat.logm
    pown = covmat.powm(2)


@profile()
def function2():
    a = numpy.random.rand(100, 200)
    covmat = numpy.dot(a, a.T) / 100 ** 2
    a = sqrtm(covmat)
    b = invsqrtm(covmat)
    c = expm(covmat)
    d = logm(covmat)
    e = powm(covmat, 2)


function()
function2()
