import os
import sys
import numpy
from memory_profiler import profile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMat import CovMat
from Utils.Distance import Distance
from oldPyRiemann.distance import *


@profile()
def function():
    covmat1 = CovMat.random(100)
    covmat2 = CovMat.random(100)
    a = Distance.euclidean(covmat1, covmat2)
    b = Distance.log_euclidean(covmat1, covmat2)
    c = Distance.log_determinant(covmat1, covmat2)
    d = Distance.riemannian(covmat1, covmat2)
    e = Distance.wasserstein(covmat1, covmat2)
    f = Distance.kullback(covmat1, covmat2)
    g = Distance.kullback_right(covmat1, covmat2)
    h = Distance.kullback_sym(covmat1, covmat2)


@profile()
def function2():
    a = numpy.random.rand(100, 200)
    b = numpy.random.rand(100, 200)
    covmat1 = numpy.dot(a, a.T) / 100 ** 2
    covmat2 = numpy.dot(b, b.T) / 100 ** 2
    a = distance_euclid(covmat1, covmat2)
    b = distance_logeuclid(covmat1, covmat2)
    c = distance_logdet(covmat1, covmat2)
    d = distance_riemann(covmat1, covmat2)
    e = distance_wasserstein(covmat1, covmat2)
    f = distance_kullback(covmat1, covmat2)
    g = distance_kullback_right(covmat1, covmat2)
    h = distance_kullback_sym(covmat1, covmat2)


function()
function2()
