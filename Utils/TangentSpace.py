#!/usr/bin/python

import numpy


class TangentSpace(object):
    @staticmethod
    def tangent(covmats, covmat):
        nb_covmats = len(covmats)
        matrix_order = covmats[0].matrix_order

        idx = numpy.triu_indices_from(covmat.matrix)
        output = numpy.empty((nb_covmats, matrix_order * (matrix_order + 1) / 2))
        coeffs = (numpy.sqrt(2) * numpy.triu(numpy.ones((matrix_order, matrix_order)), 1) + numpy.eye(matrix_order))[
            idx]

        for i in range(nb_covmats):
            tmp = (covmat.invsqrtm * covmats[i] * covmat.invsqrtm).logm
            output[i, :] = numpy.multiply(coeffs, tmp.matrix[idx])

        return output

    @staticmethod 
    def untangent(t, covmat):
        nt, nd = t.shape
        ne = int((numpy.sqrt(1 + 8 * nd) - 1) / 2)

        idx = numpy.triu_indices_from(covmat)
        covmats = numpy.empty((nt, ne, ne))
        covmats[:, idx[0], idx[1]] = t
        for i in range(nt):
            covmats[i] = numpy.diag(numpy.diag(covmats[i].matrix)) + numpy.triu(
                covmats[i].matrix, 1) / numpy.sqrt(2) + numpy.triu(covmats[i].matrix, 1).T / numpy.sqrt(2)
            covmats[i] = covmats[i].expm
            covmats[i] = covmat.sqrtm * covmat[i] * covmat.sqrtm

        return covmats