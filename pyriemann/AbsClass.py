from abc import ABCMeta, abstractproperty, abstractmethod
import numpy as np
import numpy.linalg as la

# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# import Utils.OpenBLAS

class Abstract_Covariance_Matrix(object):
    __metaclass__ = ABCMeta
    _array = None
    _dtype = None

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def array(self):
        return self._array

    @property
    def dtype(self):
        return self._dtype

    @property
    def shape(self):
        return self._array.shape

    @abstractproperty
    def transpose(self):
        raise NotImplementedError

    # ----------------------------------------------------------------------- #
    # ------------------------------- METHODS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @abstractmethod
    def reset_fields(self):
        raise NotImplementedError

    def as_type(self, dtype):
        self._dtype = dtype
        self._array.astype(dtype, copy=False)

    def norm(self, ord=None, axis=None):
        return la.norm(self._array, ord, axis)

    def trace(self, offset=0):
        return self._array.trace(offset)

    def diagonal(self, offset=0):
        return self._array.diagonal(offset)

    def maximum(self, axis=None):
        return self._array.max(axis)

    def minimum(self, axis=None):
        return self._array.min(axis)

    def mean(self, axis=None):
        return self._array.mean(axis)

    def average(self, axis=None, weights=None):
        return np.average(self._array, axis, weights)

    def variance(self, axis=None):
        return self._array.var(axis)

    def sum(self, axis=None):
        return self._array.sum(axis)

    def product(self, axis=None):
        return self._array.prod(axis)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __str__(self):
        return str(self._array)

    def __getitem__(self, slice):
        return self._array[slice]
