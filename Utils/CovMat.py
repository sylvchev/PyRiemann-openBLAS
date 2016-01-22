import os
import sys
import numpy
from numpy.linalg import inv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.AbsClass import AbsClass
from Utils.DataType import DataType


class CovMat(AbsClass):
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMAT CONSTRUCTORS ------------------------------- #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg, copy=True, data_type=DataType.double):
        self.reset_fields()
        self._data_type = data_type
        if isinstance(arg, int):
            self._numpy_array = numpy.empty((arg, arg), dtype=data_type)
        elif isinstance(arg, numpy.ndarray):
            self._numpy_array = numpy.array(arg, dtype=data_type, copy=copy)

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

    # ----------------------------------------------------------------------- #
    # ------------------------------- SETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    def set_numpy_array_for_covmats(self, numpy_array):
        self._numpy_array = numpy_array

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def matrix_order(self):
        return self._numpy_array.shape[0]

    @property
    def transpose(self):
        return self

    @property
    def inverse(self):
        if self._inverse is not None:
            return self._inverse

        self._inverse = CovMat(inv(self._numpy_array), False)
        return self._inverse

    @property
    def sqrtm(self):
        if self._sqrtm is not None:
            return self._sqrtm

        self._compute_eigen()
        self._sqrtm = CovMat(numpy.dot(numpy.multiply(self._eigen_vectors, numpy.sqrt(self._eigen_values)),
                                       self._eigen_vectors_transpose), False)
        return self._sqrtm

    @property
    def invsqrtm(self):
        if self._invsqrtm is not None:
            return self._invsqrtm

        self._compute_eigen()
        self._invsqrtm = CovMat(
            numpy.dot(numpy.multiply(self._eigen_vectors, 1.0 / numpy.sqrt(self._eigen_values)),
                      self._eigen_vectors_transpose), False)
        return self._invsqrtm

    @property
    def expm(self):
        if self._expm is not None:
            return self._expm

        self._compute_eigen()
        self._expm = CovMat(numpy.dot(numpy.multiply(self._eigen_vectors, numpy.exp(self._eigen_values)),
                                      self._eigen_vectors_transpose), False)
        return self._expm

    @property
    def logm(self):
        if self._logm is not None:
            return self._logm

        self._compute_eigen()
        self._logm = CovMat(numpy.dot(numpy.multiply(self._eigen_vectors, numpy.log(self._eigen_values)),
                                      self._eigen_vectors_transpose), False)
        return self._logm

    def powm(self, power):
        if power == 1:
            return self

        if self._power == power:
            return self._powm

        self._compute_eigen()
        self._powm = CovMat(numpy.dot(numpy.multiply(self._eigen_vectors, self._eigen_values ** power),
                                      self._eigen_vectors_transpose), False)
        self._power = power
        return self._powm

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def randomize(self, data_type=None):
        if data_type is None:
            data_type = self._data_type
        tmp = numpy.random.rand(self.matrix_order, 2 * self.matrix_order)
        self._numpy_array = (numpy.dot(tmp, numpy.transpose(tmp)) / 1000).astype(data_type, copy=False)
        self.reset_fields()

    @staticmethod
    def multiply(covmat1, covmat2):
        return CovMat(covmat1.numpy_array * covmat2.numpy_array, False)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __add__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self._numpy_array + arg.numpy_array, False)
        else:
            return CovMat(self._numpy_array + arg, False)

    def __radd__(self, arg):
        return self.__add__(arg)

    def __iadd__(self, arg):
        if isinstance(arg, CovMat):
            self._numpy_array += arg.numpy_array
        else:
            self._numpy_array += arg

        self.reset_fields()
        return self

    def __sub__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(self._numpy_array - arg.numpy_array, False)
        else:
            return CovMat(self._numpy_array - arg, False)

    def __rsub__(self, arg):
        return CovMat(-1 * self._numpy_array + arg, False)

    def __isub__(self, arg):
        if isinstance(arg, CovMat):
            self._numpy_array -= arg.numpy_array
        else:
            self._numpy_array -= arg

        self.reset_fields()
        return self

    def __mul__(self, arg):
        if isinstance(arg, CovMat):
            return CovMat(numpy.dot(self._numpy_array, arg.numpy_array), False)
        else:
            return CovMat(self._numpy_array * arg, False)

    def __rmul__(self, arg):
        return self.__mul__(arg)

    def __imul__(self, arg):
        if isinstance(arg, CovMat):
            self._numpy_array = numpy.dot(self._numpy_array, arg.numpy_array)
        else:
            self._numpy_array *= arg

        self.reset_fields()
        return self

    def __truediv__(self, arg):
        return CovMat(self._numpy_array / arg, False)

    def __rtruediv__(self, arg):
        return CovMat(arg / self._numpy_array, False)

    def __itruediv__(self, arg):
        self._numpy_array /= arg
        self.reset_fields()
        return self

    def __pow__(self, arg):
        return self.powm(arg)

    def __ipow__(self, arg):
        self._numpy_array = self.powm(arg).numpy_array
        self.reset_fields()
        return self