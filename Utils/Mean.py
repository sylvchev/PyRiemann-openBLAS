import os
import sys

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMat import CovMat
from Utils.CovMats import CovMats


class Mean(object):
    @staticmethod
    def get_sample_weight(sample_weight, covmats):
        if sample_weight is None:
            sample_weight = numpy.ones(covmats.length)
        elif covmats.length != len(sample_weight):
            raise ValueError("len of sample_weight must be equal to len of data.")

        return sample_weight / numpy.sum(sample_weight)

    @staticmethod
    def identity(covmats):
        return CovMat.identity(covmats.matrices_order)

    @staticmethod
    def euclidean(covmats, sample_weight=None):
        return CovMat(covmats.average(0, sample_weight), False)

    @staticmethod
    def log_euclidean(covmats, sample_weight=None):
        logm_covmats = CovMats([covmat.logm for covmat in covmats], False)
        return CovMat(logm_covmats.average(0, sample_weight), False).expm

    @staticmethod
    def log_determinant(covmats, tol=10e-5, max_iter=50, init=None, sample_weight=None):
        if init is None:
            output = CovMat(covmats.mean(0), False)
        else:
            output = init

        k = 0
        crit = numpy.finfo(numpy.double).max

        while crit > tol and k < max_iter:
            k += 1
            tmp = CovMats([(0.5 * (covmat + output)).inverse for covmat in covmats], False)
            new_output = CovMat(tmp.average(0, sample_weight), False).inverse
            crit = (new_output - output).norm(ord='fro')
            output = new_output

        # if k == max_iter:
        #    print("Max iter reach")

        return output

    @staticmethod
    def riemannian(covmats, tol=10e-9, max_iter=50, init=None, sample_weight=None):
        if init is None:
            output = CovMat(covmats.mean(0), False)
        else:
            output = init

        k = 0
        nu = 1.0
        tau = numpy.finfo(numpy.double).max
        crit = numpy.finfo(numpy.double).max

        while crit > tol and k < max_iter and nu > tol:
            k += 1
            tmp = CovMats([(output.invsqrtm * covmat * output.invsqrtm).logm for covmat in covmats], False)
            average = CovMat(tmp.average(0, sample_weight), False)
            crit = average.norm(ord='fro')
            h = nu * crit
            output = output.sqrtm * (nu * average).expm * output.sqrtm

            if h < tau:
                nu *= 0.95
                tau = h
            else:
                nu *= 0.5

        # if k == max_iter:
        #    print("Max iter reach")

        return output

    @staticmethod
    def wasserstein(covmats, tol=10e-4, max_iter=1, init=None, sample_weight=None):
        if init is None:
            output = CovMat(covmats.mean(0))
        else:
            output = init

        k = 0
        crit = numpy.finfo(numpy.double).max

        while (crit > tol) and (k < max_iter):
            k += 1
            tmp = CovMats([(output.sqrtm * covmat * output.sqrtm).sqrtm for covmat in covmats], False)
            average = CovMat(tmp.average(0, sample_weight), False)

            new_output = average.sqrtm
            crit = (new_output - output.sqrtm).norm(ord='fro')
            output = new_output

        # if k == max_iter:
        #    print("Max iter reach")

        return output * output
