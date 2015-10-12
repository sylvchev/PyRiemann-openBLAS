#!/usr/bin/python

import numpy
from Utils.CovMat import CovMat


class TangentSpace(object):
    @staticmethod
    def tangent(covmats, covmat):
        idx = numpy.triu_indices_from(covmat.matrix)
        output = numpy.empty((covmats.size, covmats.matrices_order * (covmats.matrices_order + 1) / 2))
        coeffs = (
            numpy.sqrt(2) * numpy.triu(numpy.ones((covmats.matrices_order, covmats.matrices_order)), 1) + numpy.eye(
                covmats.matrices_order))[idx]

        for i in range(covmats.size):
            tmp = (covmat.invsqrtm * covmats[i] * covmat.invsqrtm).logm
            output[i, :] = numpy.multiply(coeffs, tmp.matrix[idx])

        return output

    @staticmethod
    def untangent(tangent, covmat):
        nt, nd = tangent.shape
        ne = int((numpy.sqrt(1 + 8 * nd) - 1) / 2)

        idx = numpy.triu_indices_from(covmat.matrix)
        covmats = numpy.empty((nt, ne, ne))
        covmats[:, idx[0], idx[1]] = tangent
        for i in range(nt):
            numpy_matrix = covmats[i].matrix
            tmp = numpy.diag(numpy.diag(numpy_matrix)) + numpy.triu(
                numpy_matrix, 1) / numpy.sqrt(2) + numpy.triu(numpy_matrix, 1).T / numpy.sqrt(2)
            tmp2 = CovMat(tmp, False)
            covmats[i] = covmat.sqrtm * tmp2.expm * covmat.sqrtm

        return covmats
