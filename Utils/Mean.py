#!/usr/bin/python

import Utils.Environment as Environment
import numpy
from Utils.CovMat import CovMat


class Mean(object):
    @staticmethod
    def get_sample_weight(sample_weight, covmats):
        if sample_weight is None:
            sample_weight = numpy.ones(len(covmats))

        if len(covmats) != len(sample_weight):
            raise ValueError("len of sample_weight must be equal to len of data.")

        sample_weight /= numpy.sum(sample_weight)

        return sample_weight

    @staticmethod
    def identity(covmats):
        matrix_order = covmats[0].matrix_order
        return CovMat.identity(matrix_order)

    @staticmethod
    def euclidean(covmats, sample_weight=None):
        nb_covmats = len(covmats)
        matrix_order = covmats[0].matrix_order
        sample_weight = Mean.get_sample_weight(sample_weight, covmats)

        output = CovMat.zero(matrix_order)

        for i in range(nb_covmats):
            output += sample_weight[i] * covmats[i]

        return output

    @staticmethod
    def log_euclidean(covmats, sample_weight=None):
        nb_covmats = len(covmats)
        matrix_order = covmats[0].matrix_order
        sample_weight = Mean.get_sample_weight(sample_weight, covmats)

        output = CovMat.zero(matrix_order)

        for i in range(nb_covmats):
            output += sample_weight[i] * covmats[i].logm

        return output.expm

    @staticmethod
    def log_determinant(covmats, tol=10e-5, max_iter=50, init=None, sample_weight=None):
        nb_covmats = len(covmats)
        matrix_order = covmats[0].matrix_order
        sample_weight = Mean.get_sample_weight(sample_weight, covmats)

        if init is None:
            output = Mean.euclidean(covmats)
        else:
            output = init

        k = 0
        crit = numpy.finfo(Environment.data_type).max
        tmp = CovMat(matrix_order)

        while crit > tol and k < max_iter:
            k += 1
            tmp.fill(0)

            for i in range(nb_covmats):
                tmp += sample_weight[i] * (0.5 * (covmats[i] + output)).inverse 

            new_output = tmp.inverse
            crit = (new_output - output).norm
            output = new_output

        if k == max_iter:
            print("Max iter reach")

        return output

    @staticmethod
    def riemannian(covmats, tol=10e-9, max_iter=50, init=None, sample_weight=None):
        sample_weight = Mean.get_sample_weight(sample_weight, covmats)
        nb_covmats = len(covmats)
        matrix_order = covmats[0].matrix_order

        if init is None:
            output = Mean.euclidean(covmats)
        else:
            output = init

        k = 0
        nu = 1.0
        tau = numpy.finfo(Environment.data_type).max
        crit = numpy.finfo(Environment.data_type).max
        tmp = CovMat(matrix_order)

        while crit > tol and k < max_iter and nu > tol:
            k += 1
            tmp.fill(0)

            for i in range(nb_covmats):
                tmp += sample_weight[i] * (output.invsqrtm * covmats[i] * output.invsqrtm).logm

            crit = tmp.norm
            h = nu * crit

            output = output.sqrtm * (nu * tmp).expm * output.sqrtm

            if h < tau:
                nu *= 0.95
                tau = h
            else:
                nu *= 0.5

        if k == max_iter:
            print("Max iter reach")

        return output
