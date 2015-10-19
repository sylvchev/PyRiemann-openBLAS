#!/usr/bin/python

import sys
import os
import numpy
from scipy.linalg import eigvalsh

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Utils.Environment as Environment


class CovMat(object):
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMAT CONSTRUCTORS ------------------------------- #
    # ----------------------------------------------------------------------------------- #

    @staticmethod
    def __matrix_from_array(numpy_array, memory_safe_state=False):
        return numpy.matrix(numpy_array, Environment.data_type, memory_safe_state)

    def __init__(self, arg, memory_safe_state=Environment.memory_safe_state):
        if isinstance(arg, int):  # arg is an it
            self.__matrix_order = arg  # alloc memory only. matrix isn't sym def pos (use randomise() function fot it)
            self.__matrix = self.__matrix_from_array(numpy.empty((arg, arg)))
        elif isinstance(arg, numpy.ndarray):  # arg is an ndarray
            self.__matrix = self.__matrix_from_array(arg, memory_safe_state)  # map an ndarray into a matrix array
            self.__matrix_order = arg.shape[0]
        elif isinstance(arg, numpy.matrix):  # arg is a matrix
            self.__matrix = self.__matrix_from_array(arg, memory_safe_state)
            self.__matrix_order = arg.shape[0]
            
        self.__eigen_values = None
        self.__eigen_vectors = None
        self.__eigen_vectors_transpose = None
        self.__norm = None
        self.__determinant = None
        self.__inverse = None
        self.__sqrtm = None
        self.__sqrtm = None
        self.__expm = None
        self.__logm = None
        self.__powm = None
        self.__power = 1

    @staticmethod
    def zero(matrix_order):
        return CovMat(numpy.zeros((matrix_order, matrix_order)), False)

    @staticmethod
    def identity(matrix_order):
        return CovMat(numpy.eye(matrix_order), False)

    @staticmethod
    def random(matrix_order):
        covmat = CovMat(matrix_order)
        covmat.randomize()

        return covmat

    def __fields_initialization(self):
        self.__eigen_values = None
        self.__eigen_vectors = None
        self.__eigen_vectors_transpose = None
        self.__norm = None
        self.__determinant = None
        self.__inverse = None
        self.__sqrtm = None
        self.__sqrtm = None
        self.__expm = None
        self.__logm = None
        self.__powm = None
        self.__power = 1

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def matrix(self):
        return self.__matrix

    @property
    def matrix_order(self):
        return self.__matrix_order

    @property
    def eigen_values(self):
        if self.__eigen_values is not None:
            return self.__eigen_values
            
        self.__compute_eigen(True)
        return self.__eigen_values

    @property
    def eigen_vectors(self):
        if self.__eigen_vectors is not None:
            return self.__eigen_vectors

        self.__compute_eigen()
        return self.__eigen_vectors

    @property
    def eigen_vectors_transpose(self):
        if self.__eigen_vectors_transpose is not None:
            return self.__eigen_vectors_transpose

        self.__compute_eigen()
        return self.__eigen_vectors_transpose

    @property
    def norm(self):
        if self.__norm is not None:
            return self.__norm

        self.__norm = numpy.linalg.norm(self.__matrix)
        return self.__norm

    @property
    def determinant(self):
        if self.__determinant is not None:
            return self.__determinant

        self.__determinant = numpy.linalg.det(self.__matrix)
        return self.__determinant

    @property
    def transpose(self):
        return self

    @property
    def inverse(self):
        if self.__inverse is not None:
            return self.__inverse

        self.__inverse = CovMat(self.__matrix.getI())
        return self.__inverse

    @property
    def sqrtm(self):
        if self.__sqrtm is not None:
            return self.__sqrtm

        self.__compute_eigen()
        self.__sqrtm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(numpy.sqrt(self.__eigen_values))) * self.__eigen_vectors_transpose)
        return self.__sqrtm

    @property
    def invsqrtm(self):
        if self.__sqrtm is not None:
            return self.__sqrtm

        self.__compute_eigen()
        self.__sqrtm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(1.0 / numpy.sqrt(self.__eigen_values))) * self.__eigen_vectors_transpose)
        return self.__sqrtm

    @property
    def expm(self):
        if self.__expm is not None:
            return self.__expm

        self.__compute_eigen()
        self.__expm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(numpy.exp(self.__eigen_values))) * self.__eigen_vectors_transpose)
        return self.__expm

    @property
    def logm(self):
        if self.__logm is not None:
            return self.__logm

        self.__compute_eigen()
        self.__logm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(numpy.log(self.__eigen_values))) * self.__eigen_vectors_transpose)
        return self.__logm

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def reset_fields(self):
        self.__fields_initialization()

    def fill(self, value):
        self.__matrix.fill(value)
        self.__fields_initialization()

    def randomize(self):
        tmp = numpy.random.rand(self.__matrix_order, 2*self.__matrix_order)
        self.__matrix = self.__matrix_from_array(numpy.dot(tmp, numpy.transpose(tmp)) / 1000)
        self.__fields_initialization()

    def trace(self, offset=0):
        return self.__matrix.trace(offset)

    def diagonal(self, offset=0):
        return self.__matrix.diagonal(offset)

    def column(self, i):
        return self.__matrix[:, i]

    def row(self, i):
        return self.__matrix[i, :]

    def maximum(self, axis=None):
        return self.__matrix.max(axis)

    def minimum(self, axis=None):
        return self.__matrix.min(axis)

    def mean(self, axis=None):
        return self.__matrix.mean(axis)

    def variance(self, axis=None):
        return self.__matrix.var(axis)

    def sum(self, axis=None):
        return self.__matrix.sum(axis)

    def product(self, axis=None):
        return self.__matrix.prod(axis)

    def __compute_eigen(self, eigen_values_only=False):
        if self.__eigen_values is not None and self.__eigen_vectors is not None:
            return

        if eigen_values_only:
            if self.__eigen_values is not None:
                return

            self.__eigen_values = numpy.linalg.eigvalsh(self.__matrix)
        else:
            self.__eigen_values, self.__eigen_vectors = numpy.linalg.eigh(self.__matrix)
            self.__eigen_vectors = self.__matrix_from_array(self.__eigen_vectors)
            self.__eigen_vectors_transpose = self.__eigen_vectors.getT()

    def powm(self, power):
        if power == 1:
            return self

        if self.__power == power:
            return self.__powm

        self.__compute_eigen()
        self.__powm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(self.__eigen_values ** power)) * self.__eigen_vectors_transpose)
        self.__power = power
        return self.__powm

    @staticmethod
    def elements_wise_product(covmat1, covmat2):
        return CovMat(CovMat.__matrix_from_array(numpy.multiply(covmat1.matrix, covmat2.matrix)))

    @staticmethod
    def solve_problem(covmat1, covmat2):
        return eigvalsh(covmat1.matrix, covmat2.matrix)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __str__(self):
        return str(self.__matrix)

    def __getitem__(self, slice):
        return self.__matrix[slice]

    def __add__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self.__matrix + arg.matrix)
        else:
            return CovMat(self.__matrix + arg)

    def __radd__(self, arg):
        return self.__add__(arg)

    def __iadd__(self, arg):
        if isinstance(arg, CovMat):
            self.__matrix += arg.matrix
        else:
            self.__matrix += arg

        self.__fields_initialization()
        return self

    def __sub__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self.__matrix - arg.matrix)
        else:
            return CovMat(self.__matrix - arg)

    def __rsub__(self, arg):
        return CovMat(-1 * self.__matrix + arg)

    def __isub__(self, arg):
        if isinstance(arg, CovMat):
            self.__matrix -= arg.matrix
        else:
            self.__matrix -= arg

        self.__fields_initialization()
        return self

    def __mul__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self.__matrix * arg.matrix)
        else:
            return CovMat(self.__matrix * arg)

    def __rmul__(self, arg):
        return self.__mul__(arg)

    def __imul__(self, arg):
        if isinstance(arg, CovMat):
            self.__matrix *= arg.matrix
        else:
            self.__matrix *= arg

        self.__fields_initialization()
        return self

    def __truediv__(self, arg):
        return CovMat(self.__matrix / arg)

    def __rtruediv__(self, arg):
        return CovMat(arg / self.__matrix)

    def __itruediv__(self, arg):
        self.__matrix /= arg
        self.__fields_initialization()
        return self

    def __pow__(self, arg):
        return self.powm(arg)

    def __ipow__(self, arg):
        self.__matrix = self.powm(arg).matrix
        self.__fields_initialization()
        return self
