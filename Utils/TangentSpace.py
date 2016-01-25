import os
import sys

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMats import CovMats
import Utils.OpenBLAS


class TangentSpace(object):
    @staticmethod
    def tangent(covmats, covmat_ref):
        idx = numpy.triu_indices_from(covmat_ref.numpy_array)
        output = numpy.empty((covmats.length, covmats.matrices_order * (covmats.matrices_order + 1) / 2))
        coeffs = (
            numpy.sqrt(2) * numpy.triu(numpy.ones((covmats.matrices_order, covmats.matrices_order)), 1) + numpy.eye(
                covmats.matrices_order))[idx]

        for i in range(covmats.length):
            tmp = (covmat_ref.invsqrtm * covmats.get_covmat(i) * covmat_ref.invsqrtm).logm
            output[i, :] = numpy.multiply(coeffs, tmp[idx])

        return output

    @staticmethod
    def untangent(tangent, covmat_ref):
        nt, nd = tangent.shape
        ne = int((numpy.sqrt(1 + 8 * nd) - 1) / 2)

        idx = numpy.triu_indices_from(covmat_ref.numpy_array)
        covmats = CovMats(numpy.empty((nt, ne, ne)))
        covmats[:, idx[0], idx[1]] = tangent

        for i, covmat in enumerate(covmats):
            covmats[i] = numpy.diag(numpy.diag(covmats[i])) + numpy.triu(
                covmats[i], 1) / numpy.sqrt(2) + numpy.triu(covmats[i], 1).T / numpy.sqrt(2)
            covmats[i] = (covmat_ref.sqrtm * covmat.expm * covmat_ref.sqrtm).numpy_array

        return covmats
