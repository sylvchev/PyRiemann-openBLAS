from abc import ABCMeta, abstractproperty, abstractmethod
import os
import sys
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Utils.OpenBLAS


class AbsClass(object):
    __metaclass__ = ABCMeta

    # ---------------------------------------------------------------------- #
    # ------------------------------- FIELDS ------------------------------- #
    # ---------------------------------------------------------------------- #

    _numpy_array = None
    _data_type = None
    _determinant = None
    _inverse = None

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
    def determinant(self):
        if self._determinant is not None:
            return self._determinant

        self._determinant = numpy.linalg.det(self._numpy_array)
        return self._determinant

    @abstractproperty
    def transpose(self):
        raise NotImplementedError

    @abstractproperty
    def inverse(self):
        raise NotImplementedError

    # ----------------------------------------------------------------------- #
    # ------------------------------- METHODS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @abstractmethod
    def reset_fields(self):
        raise NotImplementedError

    def as_type(self, data_type):
        self._data_type = data_type
        self._numpy_array.astype(data_type, copy=False)

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
