#!/usr/bin/python

import numpy

class TangentSpace(object):
    @staticmethod
    def Tangent(covMats, cRef) :
        nbCovMats = len(covMats)
        matrixOrder = covMats[0].MatrixOrder

        idx = numpy.triu_indices_from(cRef.Matrix)
        T = numpy.empty((nbCovMats, matrixOrder * (matrixOrder + 1) / 2))
        coeffs = (numpy.sqrt(2) * numpy.triu(numpy.ones((matrixOrder, matrixOrder)), 1) + numpy.eye(matrixOrder))[idx]