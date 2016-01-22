import os
import sys

import numpy
from scipy.linalg import eigvalsh

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Distance(object):
    @staticmethod
    def euclidean(covmat1, covmat2):
        return (covmat1 - covmat2).norm(ord='fro')

    @staticmethod
    def log_euclidean(covmat1, covmat2):
        return (covmat1.logm - covmat2.logm).norm(ord='fro')

    @staticmethod
    def log_determinant(covmat1, covmat2):
        return numpy.sqrt(
            numpy.log(((covmat1 + covmat2) / 2.0).determinant) - 0.5 * numpy.log(
                covmat1.determinant * covmat2.determinant))

    @staticmethod
    def riemannian(covmat1, covmat2):
        return numpy.sqrt((numpy.log(eigvalsh(covmat1.numpy_array, covmat2.numpy_array, check_finite=False)) ** 2).sum())

    @staticmethod
    def kullback(covmat1, covmat2):
        return 0.5 * ((covmat2.inverse * covmat1).trace() - covmat1.matrix_order + numpy.log(
            covmat2.determinant / covmat1.determinant))

    @staticmethod
    def kullback_right(covmat1, covmat2):
        return Distance.kullback(covmat2, covmat1)

    @staticmethod
    def kullback_sym(covmat1, covmat2):
        return Distance.kullback(covmat1, covmat2) + Distance.kullback_right(covmat1, covmat2)

    @staticmethod
    def wasserstein(covmat1, covmat2):
        return numpy.sqrt((covmat1 + covmat2 - 2 * (covmat2.sqrtm * covmat1 * covmat2.sqrtm).sqrtm).trace())
