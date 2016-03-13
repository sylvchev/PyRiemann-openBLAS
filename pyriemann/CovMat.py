import numpy as np
from numpy import array, dot, empty, exp, eye, log, multiply, sqrt, zeros
from numpy.random import rand
from scipy.linalg import eigvalsh, eigh
from numpy.linalg import det, inv

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# import os
# import sys
# from Utils.DataType import DataType
# import Utils.OpenBLAS

from .AbsClass import Abstract_Covariance_Matrix


class Covariance_Matrix(Abstract_Covariance_Matrix):
    # ---------------------------------------------------------------------- #
    # ------------------------------- FIELDS ------------------------------- #
    # ---------------------------------------------------------------------- #

    __e_val = None
    __e_vec = None
    __e_vec_t = None
    __det = None
    __inv = None
    __sqrtm = None
    __invsqrtm = None
    __expm = None
    __logm = None
    __powm = None
    __power = None

    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMAT CONSTRUCTORS ------------------------------- #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg=None, copy=True, dtype=np.double):
        self._dtype = dtype
        if isinstance(arg, int):
            self._array = empty((arg, arg), dtype=dtype)
        elif isinstance(arg, np.ndarray):
            self._array = array(arg, dtype=dtype, copy=copy)

    @staticmethod
    def zero(dim, dtype=np.double):
        return Covariance_Matrix(zeros((dim, dim)), False, dtype)

    @staticmethod
    def eye(dim, k=0, dtype=np.double):
        return Covariance_Matrix(eye(dim, k=k), False, dtype)

    @staticmethod
    def identity(dim, dtype=np.double):
        return Covariance_Matrix(eye(dim), False, dtype)

    @staticmethod
    def random(dim, dtype=np.double):
        covmat = Covariance_Matrix(dim, False, dtype)
        covmat.randomize(dtype)
        return covmat

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def dim(self):
        return self._array.shape[0]

    @property
    def determinant(self):
        if self.__det is not None:
            return self.__det
        self.__det = det(self._array)
        return self.__det

    @property
    def transpose(self):
        return self

    @property
    def inverse(self):
        if self.__inv is not None:
            return self.__inv
        self.__inv = Covariance_Matrix(inv(self._array), False)
        return self.__inv

    @property
    def eigenval(self):
        if self.__e_val is not None:
            return self.__e_val
        self._compute_eigen(True)
        return self.__e_val

    @property
    def eigenvec(self):
        if self.__e_vec is not None:
            return self.__e_vec
        self._compute_eigen()
        return self.__e_vec

    @property
    def eigenvec_transpose(self):
        if self.__e_vec_t is not None:
            return self.__e_vec_t
        self._compute_eigen()
        return self.__e_vec_t

    @property
    def sqrtm(self):
        if self.__sqrtm is not None:
            return self.__sqrtm
        self._compute_eigen()
        self.__sqrtm = Covariance_Matrix(dot(multiply(self.__e_vec, sqrt(self.__e_val)),
                                             self.__e_vec_t), False)
        return self.__sqrtm

    @property
    def invsqrtm(self):
        if self.__invsqrtm is not None:
            return self.__invsqrtm

        self._compute_eigen()
        self.__invsqrtm = Covariance_Matrix(dot(multiply(self.__e_vec,
                                                         1./sqrt(self.__e_val)),
                                                self.__e_vec_t), False)
        return self.__invsqrtm

    @property
    def expm(self):
        if self.__expm is not None:
            return self.__expm
        self._compute_eigen()
        self.__expm = Covariance_Matrix(dot(multiply(self.__e_vec,
                                                     exp(self.__e_val)),
                                            self.__e_vec_t), False)
        return self.__expm

    @property
    def logm(self):
        if self.__logm is not None:
            return self.__logm
        self._compute_eigen()
        self.__logm = Covariance_Matrix(dot(multiply(self.__e_vec,
                                                     log(self.__e_val)),
                                            self.__e_vec_t), False)
        return self.__logm

    def powm(self, power):
        if power == 1:
            return self
        if self.__power == power:
            return self.__powm
        self._compute_eigen()
        self.__powm = Covariance_Matrix(dot(multiply(self.__e_vec,
                                                     self.__e_val ** power),
                                            self.__e_vec_t), False)
        self.__power = power
        return self.__powm

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def reset_fields(self):
        self.__e_val = None
        self.__e_vec = None
        self.__e_vec_t = None
        self._determinant = None
        self._inverse = None
        self.__sqrtm = None
        self.__invsqrtm = None
        self.__expm = None
        self.__logm = None
        self.__powm = None
        self.__power = 1

    # TODO: Use Wishart
    def randomize(self, dtype=None):
        if dtype is None:
            dtype = self._dtype
        tmp = rand(self.dim, 2 * self.dim)
        self._array = (tmp.dot(tmp.T)/self.dim**2).astype(dtype, copy=False)
        self.reset_fields()

    def _compute_eigen(self, eigenvalues_only=False):
        if self.__e_val is not None and self.__e_vec is not None:
            return
        if eigenvalues_only:
            if self.__e_val is not None: return
            else: self.__e_val = eigvalsh(self._array)
        else:
            self.__e_val, self.__e_vec = eigh(self._array)
            self.__e_vec_t = self.__e_vec.T

    @staticmethod
    def multiply(covmat1, covmat2):
        return Covariance_Matrix(covmat1._array * covmat2._array, False)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __setitem__(self, key, value):
        self._array[key] = value
        self.reset_fields()

    def __add__(self, other):
        if isinstance(other, Covariance_Matrix):
            return Covariance_Matrix(self._array + other._array, False)
        else:
            return Covariance_Matrix(self._array + other, False)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Covariance_Matrix):
            self._array += other._array
        else:
            self._array += other
        self.reset_fields()
        return self

    def __sub__(self, other):
        if isinstance(other, Covariance_Matrix):
            return Covariance_Matrix(self._array - other._array, False)
        else:
            return Covariance_Matrix(self._array - other, False)

    def __rsub__(self, other):
        return Covariance_Matrix(other - self._array, False)

    def __isub__(self, other):
        if isinstance(other, Covariance_Matrix):
            self._array -= other._array
        else:
            self._array -= other
        self.reset_fields()
        return self

    def __mul__(self, other):
        if isinstance(other, Covariance_Matrix):
            return Covariance_Matrix(self._array.dot(other._array), False)
        else:
            return Covariance_Matrix(self._array * other, False)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, Covariance_Matrix):
            self._array = self._array.dot(other._array)
        else:
            self._array *= other
        self.reset_fields()
        return self

    def __truediv__(self, other):
        return Covariance_Matrix(self._array / other, False)

    def __rtruediv__(self, other):
        return Covariance_Matrix(other / self._array, False)

    def __itruediv__(self, other):
        self._array /= other
        self.reset_fields()
        return self

    # -------------------------------------------------------
    # Python 2.7 division

    def __div__(self, other):
        return Covariance_Matrix(self._array / other, False)

    def __rdiv__(self, other):
        return Covariance_Matrix(other / self._array, False)

    def __idiv__(self, other):
        self._array /= other
        self.reset_fields()
        return self

    # -------------------------------------------------------

    def __pow__(self, other):
        return self.powm(other)

    def __ipow__(self, other):
        self._array = self.powm(other)._array
        self.reset_fields()
        return self

    def __eq__(self, other):
        return self._array == other._array
