#!/usr/bin/python

import Utils.Environment as Environment
import numpy
import scipy.linalg


class CovMat(object):
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMAT CONSTRUCTORS ------------------------------- #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg, memory_safe_state=Environment.memory_safe_state):
        if isinstance(arg, int):  # arg is an it
            self._matrix_order = arg  # alloc memory only. matrix isn't sym def pos (use randomise() function fot it)
            self._matrix = matrix_from_array(numpy.empty((arg, arg)))
        elif isinstance(arg, numpy.ndarray):  # arg is an ndarray
            self._matrix = matrix_from_array(arg, memory_safe_state)  # map an ndarray into a matrix array
            self._matrix_order = arg.shape[0]
        elif isinstance(arg, numpy.matrix):  # arg is a matrix
            self._matrix = matrix_from_array(arg, memory_safe_state)
            self._matrix_order = arg.shape[0]
            
        self._eigen_values = None
        self._eigen_vectors = None
        self._eigen_vectors_transpose = None
        self._norm = None
        self._determinant = None
        self._inverse = None
        self._sqrtm = None
        self._invsqrtm = None
        self._expm = None
        self._logm = None
        self._powm = None
        self._power = 1

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

    def fields_initialization(self):
        self._eigen_values = None
        self._eigen_vectors = None
        self._eigen_vectors_transpose = None
        self._norm = None
        self._determinant = None
        self._inverse = None
        self._sqrtm = None
        self._invsqrtm = None
        self._expm = None
        self._logm = None
        self._powm = None
        self._power = 1

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value

    @property
    def matrix_order(self):
        return self._matrix_order

    @matrix_order.setter
    def matrix_order(self, value):
        self._matrix_order = value

    @property
    def eigen_values(self):
        if self._eigen_values is not None:
            return self._eigen_values
        self.compute_eigen(True)
        return self._eigen_values

    @eigen_values.setter
    def eigen_values(self, value):
        self._eigen_values = value

    @property
    def eigen_vectors(self):
        if self._eigen_vectors is not None:
            return self._eigen_vectors

        self.compute_eigen()
        return self._eigen_vectors
    
    @eigen_vectors.setter
    def eigen_vectors(self, value):
        self._eigen_values = value

    @property
    def eigen_vectors_transpose(self):
        if self._eigen_vectors_transpose is not None:
            return self._eigen_vectors_transpose

        self.compute_eigen()
        return self._eigen_vectors_transpose

    @eigen_vectors_transpose.setter
    def eigen_vectors_transpose(self, value):
        self._eigen_vectors_transpose = value

    @property
    def norm(self):
        if self._norm is not None:
            return self._norm

        self._norm = numpy.linalg.norm(self._matrix)
        return self._norm

    @norm.setter
    def norm(self, value):
        self._norm = value

    @property
    def determinant(self):
        if self._determinant is not None:
            return self._determinant

        self._determinant = numpy.linalg.det(self._matrix)
        return self._determinant

    @determinant.setter
    def determinant(self, value):
        self._determinant = value

    @property
    def transpose(self):
        return self

    @property
    def inverse(self):
        if self._inverse is not None:
            return self._inverse

        self._inverse = CovMat(self._matrix.getI())
        return self._inverse

    @inverse.setter
    def inverse(self, value):
        self._inverse = value

    @property
    def sqrtm(self):
        if self._sqrtm is not None:
            return self._sqrtm

        self.compute_eigen()
        self._sqrtm = CovMat(self._eigen_vectors * matrix_from_array(
            numpy.diag(numpy.sqrt(self._eigen_values))) * self._eigen_vectors_transpose)
        return self._sqrtm

    @sqrtm.setter
    def sqrtm(self, value):
        self._sqrtm = value

    @property
    def invsqrtm(self):
        if self._invsqrtm is not None:
            return self._invsqrtm

        self.compute_eigen()
        self._invsqrtm = CovMat(self._eigen_vectors * matrix_from_array(
            numpy.diag(1.0 / numpy.sqrt(self._eigen_values))) * self._eigen_vectors_transpose)
        return self._invsqrtm

    @invsqrtm.setter
    def invsqrtm(self, value):
        self._invsqrtm = value

    @property
    def expm(self):
        if self._expm is not None:
            return self._expm

        self.compute_eigen()
        self._expm = CovMat(self._eigen_vectors * matrix_from_array(
            numpy.diag(numpy.exp(self._eigen_values))) * self._eigen_vectors_transpose)
        return self._expm

    @expm.setter
    def expm(self, value):
        self._expm = value

    @property
    def logm(self):
        if self._logm is not None:
            return self._logm

        self.compute_eigen()
        self._logm = CovMat(self._eigen_vectors * matrix_from_array(
            numpy.diag(numpy.log(self._eigen_values))) * self._eigen_vectors_transpose)
        return self._logm

    @logm.setter
    def logm(self, value):
        self._logm = value

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def fill(self, value):
        self._matrix.fill(value)
        self.fields_initialization()

    def randomize(self):
        tmp = numpy.random.rand(self._matrix_order, self._matrix_order)
        self._matrix = matrix_from_array(numpy.dot(tmp, numpy.transpose(tmp)) / 100)
        self.fields_initialization()

    def trace(self, offset=0):
        return self._matrix.trace(offset)

    def diagonal(self, offset=0):
        return self._matrix.diagonal(offset)

    def column(self, i):
        return self._matrix[:, i]

    def row(self, i):
        return self._matrix[i, :]

    def maximum(self, axis=None):
        return self._matrix.max(axis)

    def minimum(self, axis=None):
        return self._matrix.min(axis)

    def mean(self, axis=None):
        return self._matrix.mean(axis)

    def variance(self, axis=None):
        return self._matrix.var(axis)

    def sum(self, axis=None):
        return self._matrix.sum(axis)

    def product(self, axis=None):
        return self._matrix.prod(axis)

    def compute_eigen(self, eigen_values_only=False):
        if self._eigen_values is not None and self._eigen_vectors is not None:
            return

        if eigen_values_only:
            if self._eigen_values is not None:
                return

            self._eigen_values = numpy.linalg.eigvalsh(self._matrix)
        else:
            self._eigen_values, self._eigen_vectors = numpy.linalg.eigh(self._matrix)
            self._eigen_vectors = matrix_from_array(self._eigen_vectors)
            self._eigen_vectors_transpose = self._eigen_vectors.getT()

    def powm(self, power):
        if power == 1:
            return self

        if self._power == power:
            return self._powm

        self.compute_eigen()
        self._powm = CovMat(self._eigen_vectors * matrix_from_array(
            numpy.diag(self._eigen_values ** power)) * self._eigen_vectors_transpose)
        self._power = power
        return self._powm

    @staticmethod
    def elements_wise_prodcut(self, covmat1, covmat2):
        return self._MatrixFromArray(numpy.multiply(covmat1, covmat2))

    @staticmethod
    def solve_problem(covmat1, covmat2):
        return scipy.linalg.eigvalsh(covmat1.matrix, covmat2.matrix)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __str__(self):
        return str(self._matrix)

    def __call__(self, x, y):
        return self._matrix[x, y]

    def __add__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self._matrix + arg.matrix)
        else:
            return CovMat(self._matrix + arg)

    def __radd__(self, arg):
        return self.__add__(arg)

    def __iadd__(self, arg):
        if isinstance(arg, CovMat):
            self._matrix += arg.matrix
        else:
            self._matrix += arg

        self.fields_initialization()
        return self

    def __sub__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self._matrix - arg.matrix)
        else:
            return CovMat(self._matrix - arg)

    def __rsub__(self, arg):
        return CovMat(-1 * self._matrix + arg.matrix)

    def __isub__(self, arg):
        if isinstance(arg, CovMat):
            self._matrix -= arg.matrix
        else:
            self._matrix -= arg

        self.fields_initialization()
        return self

    def __mul__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self._matrix * arg.matrix)
        else:
            return CovMat(self._matrix * arg)

    def __rmul__(self, arg):
        return self.__mul__(arg)

    def __imul__(self, arg):
        if isinstance(arg, CovMat):
            self._matrix = self._matrix * arg.matrix
        else:
            self._matrix = self._matrix * arg

        self.fields_initialization()
        return self

    def __truediv__(self, arg):
        return CovMat(self._matrix / arg)

    def __rtruediv__(self, arg):
        return CovMat(arg / self._matrix)

    def __itruediv__(self, arg):
        self._matrix /= arg
        self.fields_initialization()
        return self

#    def __pow__(self, arg):
#        return self._powm(arg)

#    def __ipow__(self, arg):
#        self = self._powm(arg).matrix
#        return self


def matrix_from_array(numpy_array, memory_safe_state=False):
    return numpy.matrix(numpy_array, Environment.data_type, memory_safe_state)
