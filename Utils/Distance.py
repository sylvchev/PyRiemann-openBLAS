#!/usr/bin/python

import numpy
from Utils.CovMat import CovMat


class Distance(object):
    @staticmethod
    def euclidean(covmat1, covmat2):
        return (covmat1 - covmat2).norm

    @staticmethod
    def log_euclidean(covmat1, covmat2):
        return (covmat1.logm - covmat2.logm).norm

    @staticmethod
    def log_determinant(covmat1, covmat2):
        return numpy.sqrt(
            numpy.log(((covmat1 + covmat2) / 2).determinant) - 0.5 * numpy.log((covmat1 * covmat2).determinant))

    @staticmethod
    def riemannian(covmat1, covmat2):
        return numpy.sqrt((numpy.log(CovMat.solve_problem(covmat1, covmat2)) ** 2).sum())

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
