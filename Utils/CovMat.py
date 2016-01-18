import os
import sys
import numpy
from scipy.linalg import eigvalsh, eigh
from numpy.linalg import inv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Utils.OpenBLAS


class CovMat(object):
    # ------------------------------------------------------------------------- #
    # ------------------------------- DATA TYPE ------------------------------- #
    # ------------------------------------------------------------------------- #

    class DataType(object):
        float32 = numpy.float32
        float64 = numpy.float64
        float = numpy.float32
        double = numpy.float64

    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMAT CONSTRUCTORS ------------------------------- #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg, copy=True, data_type=DataType.double):
        if isinstance(arg, int):  # arg is an it
            # alloc memory only. matrix isn't sym def pos (use randomise() function fot it)
            self.__matrix_order = arg
            self.__numpy_array = numpy.empty((arg, arg), dtype=data_type)
        elif isinstance(arg, numpy.ndarray):  # arg is an ndarray
            self.__numpy_array = numpy.array(arg, dtype=data_type, copy=copy)
            self.__matrix_order = arg.shape[0]

        self.__eigen_values = None
        self.__eigen_vectors = None
        self.__eigen_vectors_transpose = None
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
    def eye(matrix_order, diagonal_id=0, data_type=DataType.double):
        return CovMat(numpy.eye(matrix_order, k=diagonal_id), False, data_type)

    @staticmethod
    def identity(matrix_order, data_type=DataType.double):
        return CovMat(numpy.eye(matrix_order), False, data_type)

    @staticmethod
    def random(matrix_order, data_type=DataType.double):
        covmat = CovMat(matrix_order, False, data_type)
        covmat.randomize(data_type)
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

    def set_numpy_array_for_covmats(self, numpy_array):
        self.__numpy_array = numpy_array

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def shape(self):
        return self.__numpy_array.shape

    @property
    def numpy_array(self):
        return self.__numpy_array

    @property
    def matrix_order(self):
        return self.__matrix_order

    @property
    def inverse(self):
        if self.__inverse is not None:
            return self.__inverse

        self.__inverse = CovMat(inv(self.__numpy_array), False)
        return self.__inverse

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
    def determinant(self):
        if self.__determinant is not None:
            return self.__determinant

        self.__determinant = numpy.linalg.det(self.__numpy_array)
        return self.__determinant

    @property
    def transpose(self):
        return self

    @property
    def sqrtm(self):
        if self.__sqrtm is not None:
            return self.__sqrtm

        self.__compute_eigen()
        self.__sqrtm = CovMat(numpy.dot(numpy.dot(self.__eigen_vectors, numpy.diag(numpy.sqrt(self.__eigen_values))),
                                        self.__eigen_vectors_transpose), False)
        return self.__sqrtm

    @property
    def invsqrtm(self):
        if self.__invsqrtm is not None:
            return self.__invsqrtm

        self.__compute_eigen()
        self.__invsqrtm = CovMat(
            numpy.dot(numpy.dot(self.__eigen_vectors, numpy.diag(1.0 / numpy.sqrt(self.__eigen_values))),
                      self.__eigen_vectors_transpose), False)
        return self.__invsqrtm

    @property
    def expm(self):
        if self.__expm is not None:
            return self.__expm

        self.__compute_eigen()
        self.__expm = CovMat(numpy.dot(numpy.dot(self.__eigen_vectors, numpy.diag(numpy.exp(self.__eigen_values))),
                                       self.__eigen_vectors_transpose), False)
        return self.__expm

    @property
    def logm(self):
        if self.__logm is not None:
            return self.__logm

        self.__compute_eigen()
        self.__logm = CovMat(numpy.dot(numpy.multiply(self.__eigen_vectors, numpy.log(self.__eigen_values)),
                                       self.__eigen_vectors_transpose), False)
        return self.__logm

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def to_type(self, data_type):
        self.__numpy_array.astype(data_type, copy=False)

    def reset_fields(self):
        self.__fields_initialization()

    def fill(self, value):
        self.__numpy_array.fill(value)
        self.__fields_initialization()

    def randomize(self, data_type=DataType.double):
        tmp = numpy.random.rand(self.__matrix_order, 2 * self.__matrix_order)
        self.__numpy_array = (numpy.dot(tmp, numpy.transpose(tmp)) / 1000).astype(data_type, copy=False)
        self.__fields_initialization()

    def norm(self, ord=None, axis=None):
        return numpy.linalg.norm(self.__numpy_array, ord, axis)

    def trace(self, offset=0):
        return self.__numpy_array.trace(offset)

    def diagonal(self, offset=0):
        return self.__numpy_array.diagonal(offset)

    def column(self, i):
        return self.__numpy_array[:, i]

    def row(self, i):
        return self.__numpy_array[i, :]

    def maximum(self, axis=None):
        return self.__numpy_array.max(axis)

    def minimum(self, axis=None):
        return self.__numpy_array.min(axis)

    def mean(self, axis=None):
        return self.__numpy_array.mean(axis)

    def average(self, axis=None, weights=None):
        return numpy.average(self.__numpy_array, axis, weights)

    def variance(self, axis=None):
        return self.__numpy_array.var(axis)

    def sum(self, axis=None):
        return self.__numpy_array.sum(axis)

    def product(self, axis=None):
        return self.__numpy_array.prod(axis)

    def __compute_eigen(self, eigen_values_only=False):
        if self.__eigen_values is not None and self.__eigen_vectors is not None:
            return

        if eigen_values_only:
            if self.__eigen_values is not None:
                return

            self.__eigen_values = eigvalsh(self.__numpy_array)
        else:
            self.__eigen_values, self.__eigen_vectors = eigh(self.__numpy_array)
            self.__eigen_vectors_transpose = self.__eigen_vectors.T

    def powm(self, power):
        if power == 1:
            return self

        if self.__power == power:
            return self.__powm

        self.__compute_eigen()
        self.__powm = CovMat(numpy.dot(numpy.dot(self.__eigen_vectors, numpy.diag(self.__eigen_values ** power)),
                                       self.__eigen_vectors_transpose), False)
        self.__power = power
        return self.__powm

    @staticmethod
    def multiply(covmat1, covmat2):
        return CovMat(covmat1.numpy_array * covmat2.numpy_array, False)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __str__(self):
        return str(self.__numpy_array)

    def __getitem__(self, slice):
        return self.__numpy_array[slice]

    def __add__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self.__numpy_array + arg.numpy_array, False)
        else:
            return CovMat(self.__numpy_array + arg, False)

    def __radd__(self, arg):
        return self.__add__(arg)

    def __iadd__(self, arg):
        if isinstance(arg, CovMat):
            self.__numpy_array += arg.numpy_array
        else:
            self.__numpy_array += arg

        self.__fields_initialization()
        return self

    def __sub__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self.__numpy_array - arg.numpy_array, False)
        else:
            return CovMat(self.__numpy_array - arg, False)

    def __rsub__(self, arg):
        return CovMat(-1 * self.__numpy_array + arg, False)

    def __isub__(self, arg):
        if isinstance(arg, CovMat):
            self.__numpy_array -= arg.numpy_array
        else:
            self.__numpy_array -= arg

        self.__fields_initialization()
        return self

    def __mul__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(numpy.dot(self.__numpy_array, arg.numpy_array), False)
        else:
            return CovMat(self.__numpy_array * arg, False)

    def __rmul__(self, arg):
        return self.__mul__(arg)

    def __imul__(self, arg):
        if isinstance(arg, CovMat):
            self.__numpy_array = numpy.dot(self.__numpy_array, arg.numpy_array)
        else:
            self.__numpy_array *= arg

        self.__fields_initialization()
        return self

    def __truediv__(self, arg):
        return CovMat(self.__numpy_array / arg, False)

    def __rtruediv__(self, arg):
        return CovMat(arg / self.__numpy_array, False)

    def __itruediv__(self, arg):
        self.__numpy_array /= arg
        self.__fields_initialization()
        return self

    def __pow__(self, arg):
        return self.powm(arg)

    def __ipow__(self, arg):
        self.__numpy_array = self.powm(arg).numpy_array
        self.__fields_initialization()
        return self
