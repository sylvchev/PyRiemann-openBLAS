import os
import sys
import numpy
from scipy.linalg import eigvalsh, eigh
from numpy.linalg import inv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.AbsClass import AbsClass
from Utils.DataType import DataType


class CovMat(AbsClass):
    # ---------------------------------------------------------------------- #
    # ------------------------------- FIELDS ------------------------------- #
    # ---------------------------------------------------------------------- #

    __eigen_values = None
    __eigen_vectors = None
    __eigen_vectors_transpose = None
    __sqrtm = None
    __invsqrtm = None
    __expm = None
    __logm = None
    __powm = None
    __power = None

    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMAT CONSTRUCTORS ------------------------------- #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg, copy=True, data_type=DataType.double):
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
    def eigen_values(self):
        if self.__eigen_values is not None:
            return self.__eigen_values

        self._compute_eigen(True)
        return self.__eigen_values

    @property
    def eigen_vectors(self):
        if self.__eigen_vectors is not None:
            return self.__eigen_vectors

        self._compute_eigen()
        return self.__eigen_vectors

    @property
    def eigen_vectors_transpose(self):
        if self.__eigen_vectors_transpose is not None:
            return self.__eigen_vectors_transpose

        self._compute_eigen()
        return self.__eigen_vectors_transpose

    @property
    def sqrtm(self):
        if self.__sqrtm is not None:
            return self.__sqrtm

        self._compute_eigen()
        self.__sqrtm = CovMat(numpy.dot(numpy.multiply(self.__eigen_vectors, numpy.sqrt(self.__eigen_values)),
                                        self.__eigen_vectors_transpose), False)
        return self.__sqrtm

    @property
    def invsqrtm(self):
        if self.__invsqrtm is not None:
            return self.__invsqrtm

        self._compute_eigen()
        self.__invsqrtm = CovMat(
            numpy.dot(numpy.multiply(self.__eigen_vectors, 1.0 / numpy.sqrt(self.__eigen_values)),
                      self.__eigen_vectors_transpose), False)
        return self.__invsqrtm

    @property
    def expm(self):
        if self.__expm is not None:
            return self.__expm

        self._compute_eigen()
        self.__expm = CovMat(numpy.dot(numpy.multiply(self.__eigen_vectors, numpy.exp(self.__eigen_values)),
                                       self.__eigen_vectors_transpose), False)
        return self.__expm

    @property
    def logm(self):
        if self.__logm is not None:
            return self.__logm

        self._compute_eigen()
        self.__logm = CovMat(numpy.dot(numpy.multiply(self.__eigen_vectors, numpy.log(self.__eigen_values)),
                                       self.__eigen_vectors_transpose), False)
        return self.__logm

    def powm(self, power):
        if power == 1:
            return self

        if self.__power == power:
            return self.__powm

        self._compute_eigen()
        self.__powm = CovMat(numpy.dot(numpy.multiply(self.__eigen_vectors, self.__eigen_values ** power),
                                       self.__eigen_vectors_transpose), False)
        self.__power = power
        return self.__powm

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def reset_fields(self):
        self.__eigen_values = None
        self.__eigen_vectors = None
        self.__eigen_vectors_transpose = None
        self._determinant = None
        self._inverse = None
        self.__sqrtm = None
        self.__invsqrtm = None
        self.__expm = None
        self.__logm = None
        self.__powm = None
        self.__power = 1

    def randomize(self, data_type=None):
        if data_type is None:
            data_type = self._data_type
        tmp = numpy.random.rand(self.matrix_order, 2 * self.matrix_order)
        self._numpy_array = (numpy.dot(tmp, numpy.transpose(tmp)) / 1000).astype(data_type, copy=False)
        self.reset_fields()

    def _compute_eigen(self, eigen_values_only=False):
        if self.__eigen_values is not None and self.__eigen_vectors is not None:
            return

        if eigen_values_only:
            if self.__eigen_values is not None:
                return

            self.__eigen_values = eigvalsh(self._numpy_array)
        else:
            self.__eigen_values, self.__eigen_vectors = eigh(self._numpy_array)
            self.__eigen_vectors_transpose = self.__eigen_vectors.T

    @staticmethod
    def multiply(covmat1, covmat2):
        return CovMat(covmat1.numpy_array * covmat2.numpy_array, False)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __add__(self, other):
        if isinstance(other, CovMat):
            return CovMat(self._numpy_array + other.numpy_array, False)
        else:
            return CovMat(self._numpy_array + other, False)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, CovMat):
            self._numpy_array += other.numpy_array
        else:
            self._numpy_array += other

        self.reset_fields()
        return self

    def __sub__(self, other):
        if isinstance(other, CovMat):
            return CovMat(self._numpy_array - other.numpy_array, False)
        else:
            return CovMat(self._numpy_array - other, False)

    def __rsub__(self, other):
        return CovMat(other - self._numpy_array, False)

    def __isub__(self, other):
        if isinstance(other, CovMat):
            self._numpy_array -= other.numpy_array
        else:
            self._numpy_array -= other

        self.reset_fields()
        return self

    def __mul__(self, other):
        if isinstance(other, CovMat):
            return CovMat(numpy.dot(self._numpy_array, other.numpy_array), False)
        else:
            return CovMat(self._numpy_array * other, False)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, CovMat):
            self._numpy_array = numpy.dot(self._numpy_array, other.numpy_array)
        else:
            self._numpy_array *= other

        self.reset_fields()
        return self

    def __truediv__(self, other):
        return CovMat(self._numpy_array / other, False)

    def __rtruediv__(self, other):
        return CovMat(other / self._numpy_array, False)

    def __itruediv__(self, other):
        self._numpy_array /= other
        self.reset_fields()
        return self

    def __pow__(self, other):
        return self.powm(other)

    def __ipow__(self, other):
        self._numpy_array = self.powm(other).numpy_array
        self.reset_fields()
        return self

    def __eq__(self, other):
        return self._numpy_array == other.numpy_array
