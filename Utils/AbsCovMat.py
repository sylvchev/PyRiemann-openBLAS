from abc import ABCMeta, abstractproperty, abstractmethod
import os
import sys
import numpy
from numpy.linalg import eigvalsh, eigh

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Utils.OpenBLAS


class AbsCovMat(object):
    __metaclass__ = ABCMeta

    # ---------------------------------------------------------------------- #
    # ------------------------------- FIELDS ------------------------------- #
    # ---------------------------------------------------------------------- #

    _numpy_array = None
    _data_type = None
    _eigen_values = None
    _eigen_vectors = None
    _eigen_vectors_transpose = None
    __determinant = None
    _inverse = None
    _sqrtm = None
    _invsqrtm = None
    _expm = None
    _logm = None
    _powm = None
    _power = None

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def numpy_array(self):
        return self._numpy_array

    @property
    def data_type(self):
        return self._data_type

    @property
    def shape(self):
        return self._numpy_array.shape

    @property
    def eigen_values(self):
        if self._eigen_values is not None:
            return self._eigen_values

        self._compute_eigen(True)
        return self._eigen_values

    @property
    def eigen_vectors(self):
        if self._eigen_vectors is not None:
            return self._eigen_vectors

        self._compute_eigen()
        return self._eigen_vectors

    @property
    def eigen_vectors_transpose(self):
        if self._eigen_vectors_transpose is not None:
            return self._eigen_vectors_transpose

        self._compute_eigen()
        return self._eigen_vectors_transpose

    @property
    def determinant(self):
        if self.__determinant is not None:
            return self.__determinant

        self.__determinant = numpy.linalg.det(self._numpy_array)
        return self.__determinant

    @property
    def transpose(self):
        return self

    @property
    def inverse(self):
        raise NotImplementedError

    @abstractproperty
    def sqrtm(self):
        raise NotImplementedError

    @abstractproperty
    def invsqrtm(self):
        raise NotImplementedError

    @abstractproperty
    def expm(self):
        raise NotImplementedError

    @abstractproperty
    def logm(self):
        raise NotImplementedError

    @abstractmethod
    def powm(self, power):
        raise NotImplementedError

    # ----------------------------------------------------------------------- #
    # ------------------------------- METHODS ------------------------------- #
    # ----------------------------------------------------------------------- #

    def reset_fields(self):
        self._eigen_values = None
        self._eigen_vectors = None
        self._eigen_vectors_transpose = None
        self.__determinant = None
        self._inverse = None
        self._sqrtm = None
        self._invsqrtm = None
        self._expm = None
        self._logm = None
        self._powm = None
        self._power = 1

    def as_type(self, data_type):
        self._numpy_array.astype(data_type, copy=False)

    def _compute_eigen(self, eigen_values_only=False):
        if self._eigen_values is not None and self._eigen_vectors is not None:
            return

        if eigen_values_only:
            if self._eigen_values is not None:
                return

            self._eigen_values = eigvalsh(self._numpy_array)
        else:
            self._eigen_values, self._eigen_vectors = eigh(self._numpy_array)
            self._eigen_vectors_transpose = self._eigen_vectors.T

    def fill(self, value):
        self._numpy_array.fill(value)
        self.reset_fields()

    def norm(self, ord=None, axis=None):
        return numpy.linalg.norm(self._numpy_array, ord, axis)

    def trace(self, offset=0):
        return self._numpy_array.trace(offset)

    def diagonal(self, offset=0):
        return self._numpy_array.diagonal(offset)

    def maximum(self, axis=None):
        return self._numpy_array.max(axis)

    def minimum(self, axis=None):
        return self._numpy_array.min(axis)

    def mean(self, axis=None):
        return self._numpy_array.mean(axis)

    def average(self, axis=None, weights=None):
        return numpy.average(self._numpy_array, axis, weights)

    def variance(self, axis=None):
        return self._numpy_array.var(axis)

    def sum(self, axis=None):
        return self._numpy_array.sum(axis)

    def product(self, axis=None):
        return self._numpy_array.prod(axis)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __str__(self):
        return str(self._numpy_array)

    def __getitem__(self, slice):
        return self._numpy_array[slice]
