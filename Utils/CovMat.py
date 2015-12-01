import os
import sys
from enum import Enum

import numpy
from scipy.linalg import eigvalsh

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class CovMat(object):
    # ------------------------------------------------------------------------- #
    # ------------------------------- DATA TYPE ------------------------------- #
    # ------------------------------------------------------------------------- #

    class DataType(Enum):
        int8 = numpy.int8
        int16 = numpy.int16
        int32 = numpy.int32
        int64 = numpy.int64
        # int128 = numpy.int128
        uint8 = numpy.uint8
        uint16 = numpy.uint16
        uint32 = numpy.int32
        uint64 = numpy.uint64
        # uint128 = numpy.uint128
        float16 = numpy.float16
        float32 = numpy.float32
        float64 = numpy.float64
        # float80 = numpy.float80
        # float96 = numpy.float96
        float128 = numpy.float128
        # float256 = numpy.float256
        int = numpy.int_
        float = numpy.float32
        double = numpy.float64

    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMAT CONSTRUCTORS ------------------------------- #
    # ----------------------------------------------------------------------------------- #

    @staticmethod
    def __matrix_from_array(numpy_array, copy=True, data_type=DataType.double):
        return numpy.matrix(numpy_array, data_type.value, copy)

    def __init__(self, arg, copy=True, data_type=DataType.double):
        if isinstance(arg, int):  # arg is an it
            # alloc memory only. matrix isn't sym def pos (use randomise() function fot it)
            self.__matrix_order = arg
            self.__matrix = self.__matrix_from_array(numpy.empty((arg, arg)), False, data_type)
        elif isinstance(arg, numpy.ndarray):  # arg is an ndarray
            # map an ndarray into a matrix array
            self.__matrix = self.__matrix_from_array(arg, copy, data_type)
            self.__matrix_order = arg.shape[0]
        elif isinstance(arg, numpy.matrix):  # arg is a matrix
            self.__matrix = self.__matrix_from_array(arg, copy, data_type)
            self.__matrix_order = arg.shape[0]

        self.__eigen_values = None
        self.__eigen_vectors = None
        self.__eigen_vectors_transpose = None
        self.__norm = None
        self.__determinant = None
        self.__inverse = None
        self.__sqrtm = None
        self.__invsqrtm = None
        self.__expm = None
        self.__logm = None
        self.__powm = None
        self.__power = 1

    @staticmethod
    def zero(matrix_order, data_type=DataType.double):
        return CovMat(numpy.zeros((matrix_order, matrix_order)), False, data_type)

    @staticmethod
    def identity(matrix_order, data_type=DataType.double):
        return CovMat(numpy.eye(matrix_order), False, data_type)

    @staticmethod
    def random(matrix_order, data_type=DataType.double):
        covmat = CovMat(matrix_order, False, data_type)
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
        self.__invsqrtm = None
        self.__expm = None
        self.__logm = None
        self.__powm = None
        self.__power = 1

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def shape(self):
        return self.__matrix.shape

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

        self.__inverse = CovMat(self.__matrix.getI(), False)
        return self.__inverse

    @property
    def sqrtm(self):
        if self.__sqrtm is not None:
            return self.__sqrtm

        self.__compute_eigen()
        self.__sqrtm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(numpy.sqrt(self.__eigen_values)), False) * self.__eigen_vectors_transpose, False)
        return self.__sqrtm

    @property
    def invsqrtm(self):
        if self.__invsqrtm is not None:
            return self.__invsqrtm

        self.__compute_eigen()
        self.__invsqrtm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(1.0 / numpy.sqrt(self.__eigen_values)), False) * self.__eigen_vectors_transpose, False)
        return self.__invsqrtm

    @property
    def expm(self):
        if self.__expm is not None:
            return self.__expm

        self.__compute_eigen()
        self.__expm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(numpy.exp(self.__eigen_values)), False) * self.__eigen_vectors_transpose, False)
        return self.__expm

    @property
    def logm(self):
        if self.__logm is not None:
            return self.__logm

        self.__compute_eigen()
        self.__logm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(numpy.log(self.__eigen_values)), False) * self.__eigen_vectors_transpose, False)
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
        tmp = numpy.random.rand(self.__matrix_order, 2 * self.__matrix_order)
        self.__matrix = self.__matrix_from_array(numpy.dot(tmp, numpy.transpose(tmp)) / 1000, False)
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
            self.__eigen_vectors = self.__matrix_from_array(self.__eigen_vectors, False)
            self.__eigen_vectors_transpose = self.__eigen_vectors.getT()

    def powm(self, power):
        if power == 1:
            return self

        if self.__power == power:
            return self.__powm

        self.__compute_eigen()
        self.__powm = CovMat(self.__eigen_vectors * self.__matrix_from_array(
            numpy.diag(self.__eigen_values ** power), False) * self.__eigen_vectors_transpose, False)
        self.__power = power
        return self.__powm

    @staticmethod
    def elements_wise_product(covmat1, covmat2):
        return CovMat(numpy.multiply(covmat1.matrix, covmat2.matrix), False)

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
            return CovMat(self.__matrix + arg.matrix, False)
        else:
            return CovMat(self.__matrix + arg, False)

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
            return CovMat(self.__matrix - arg.matrix, False)
        else:
            return CovMat(self.__matrix - arg, False)

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
            return CovMat(self.__matrix * arg.matrix, False)
        else:
            return CovMat(self.__matrix * arg, False)

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
        return CovMat(self.__matrix / arg, False)

    def __rtruediv__(self, arg):
        return CovMat(arg / self.__matrix, False)

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
