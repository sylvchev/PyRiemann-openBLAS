import os
import sys

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMat import CovMat
from Utils.CovMats import CovMats


class TangentSpace(object):
    @staticmethod
    def tangent(covmats, covmat):
        idx = numpy.triu_indices_from(covmat.numpy_array)
        output = numpy.empty((covmats.length, covmats.matrices_order * (covmats.matrices_order + 1) / 2))
        coeffs = (
            numpy.sqrt(2) * numpy.triu(numpy.ones((covmats.matrices_order, covmats.matrices_order)), 1) + numpy.eye(
                covmats.matrices_order))[idx]

        for i in range(covmats.length):
            tmp = (covmat.invsqrtm * covmats[i] * covmat.invsqrtm).logm
            output[i, :] = numpy.multiply(coeffs, tmp[idx])

        return output

    @staticmethod
    def untangent(tangent, covmat):
        nt, nd = tangent.shape
        ne = int((numpy.sqrt(1 + 8 * nd) - 1) / 2)

        idx = numpy.triu_indices_from(covmat.matrix)
        numpy_array = numpy.empty((nt, ne, ne))
        covmats = CovMats()
        
        numpy_array[:, idx[0], idx[1]] = tangent
        for i in range(nt):
            tmp = numpy.diag(numpy.diag(numpy_array[i])) + numpy.triu(
                numpy_array[i], 1) / numpy.sqrt(2) + numpy.triu(numpy_array[i], 1).T / numpy.sqrt(2)
            covmats.append(covmat.sqrtm * CovMat(tmp, False).expm * covmat.sqrtm)

        return CovMats(numpy_array)
