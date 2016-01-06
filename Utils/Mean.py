import os
import sys

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMat import CovMat


class Mean(object):
    @staticmethod
    def get_sample_weight(sample_weight, covmats):
        if sample_weight is None:
            sample_weight = numpy.ones(covmats.shape[0])
        elif covmats.shape[0] != len(sample_weight):
            raise ValueError("len of sample_weight must be equal to len of data.")

        return sample_weight / numpy.sum(sample_weight)

    @staticmethod
    def identity(covmats):
        return CovMat.identity(covmats.shape[1])

    @staticmethod
    def euclidean(covmats, sample_weight=None):
        return CovMat(numpy.average(covmats.numpy_array, axis=0, weights=sample_weight))

    @staticmethod
    def log_euclidean(covmats, sample_weight=None):
        sample_weight = Mean.get_sample_weight(sample_weight, covmats)

        output = CovMat.zero(covmats.shape[1])

        for i in range(covmats.shape[0]):
            output += sample_weight[i] * covmats[i].logm

        return output.expm

    @staticmethod
    def log_determinant(covmats, tol=10e-5, max_iter=50, init=None, sample_weight=None):
        sample_weight = Mean.get_sample_weight(sample_weight, covmats)

        if init is None:
            output = covmats.mean(0)
        else:
            output = init

        k = 0
        crit = numpy.finfo(numpy.double).max
        tmp = CovMat(covmats.shape[1])

        while crit > tol and k < max_iter:
            k += 1
            tmp.fill(0)

            for i in range(covmats.shape[0]):
                tmp += sample_weight[i] * (0.5 * (covmats[i] + output)).inverse

            new_output = tmp.inverse
            crit = (new_output - output).norm(ord='fro')
            output = new_output

        if k == max_iter:
            print("Max iter reach")

        return output

    @staticmethod
    def riemannian(covmats, tol=10e-9, max_iter=50, init=None, sample_weight=None):
        sample_weight = Mean.get_sample_weight(sample_weight, covmats)

        if init is None:
            output = covmats.mean(0)
        else:
            output = init

        k = 0
        nu = 1.0
        tau = numpy.finfo(numpy.double).max
        crit = numpy.finfo(numpy.double).max
        tmp = CovMat(covmats.shape[1])

        while crit > tol and k < max_iter and nu > tol:
            k += 1
            tmp.fill(0)

            for i in range(covmats.shape[0]):
                tmp += sample_weight[i] * (output.invsqrtm * covmats[i] * output.invsqrtm).logm

            crit = tmp.norm(ord='fro')
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

    @staticmethod
    def wasserstein(covmats, tol=10e-4, max_iter=50, init=None, sample_weight=None):
        sample_weight = Mean.get_sample_weight(sample_weight, covmats)

        if init is None:
            output = covmats.mean(0)
        else:
            output = init

        k = 0
        crit = numpy.finfo(numpy.double).max
        tmp = CovMat(covmats.shape[1])

        while (crit > tol) and (k < max_iter):
            k += 1
            tmp.fill(0)

            for i in range(covmats.shape[0]):
                tmp += sample_weight[i] * (output.sqrtm * covmats[i] * output.sqrtm).sqrtm

            new_output = tmp.sqrtm
            crit = (new_output - output).norm(ord='fro')
            output = new_output

        if k == max_iter:
            print("Max iter reach")

        return output * output
