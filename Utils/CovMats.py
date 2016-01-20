import os
import sys
import numpy
from numpy.linalg import inv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.AbsCovMat import AbsCovMat
from Utils.CovMat import CovMat
from Utils.DataType import DataType


class CovMats(AbsCovMat):
    # ---------------------------------------------------------------------- #
    # ------------------------------- FIELDS ------------------------------- #
    # ---------------------------------------------------------------------- #

    __covmats = None

    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg, copy=True, data_type=DataType.double):
        if isinstance(arg, list):
            self.__covmats_from_list(arg, data_type)
        elif isinstance(arg, numpy.ndarray):
            self.__covmats_from_numpy_array(arg, copy, data_type)

    def __covmats_from_list(self, arg, data_type=DataType.double):
        if len(arg) == 0:
            raise ValueError("The list is empty.")
        self.reset_fields()
        self._numpy_array = numpy.array([covmat.numpy_array for covmat in arg], dtype=data_type)
        self.__covmats = arg
        for i, covmat in enumerate(self.__covmats):
            covmat.set_numpy_array_for_covmats(self._numpy_array[i, :, :])

    def __covmats_from_numpy_array(self, arg, copy, data_type=DataType.double):
        self.reset_fields()
        self._numpy_array = numpy.array(arg, dtype=data_type, copy=copy)
        self.__covmats = []
        for i in range(self.length):
            self.__covmats.append(CovMat(self._numpy_array[i, :, :], False))

    @staticmethod
    def random(length, matrices_order, data_type=DataType.double):
        return CovMats([CovMat.random(matrices_order, data_type) for i in range(length)])

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def length(self):
        return self._numpy_array.shape[0]

    @property
    def matrices_order(self):
        return self._numpy_array.shape[1]

    def get_covmat(self, index):
        return self.__covmats[index]

    @property
    def inverse(self):
        if self._inverse is not None:
            return self._inverse

        self._inverse = CovMats(inv(self._numpy_array), False)
        return self._inverse

    @property
    def sqrtm(self):
        if self._sqrtm is not None:
            return self._sqrtm

        self._compute_eigen()
        self._sqrtm = CovMats(numpy.dot(numpy.dot(self._eigen_vectors, numpy.diag(numpy.sqrt(self._eigen_values))),
                                        self._eigen_vectors_transpose), False)
        return self._sqrtm

    @property
    def invsqrtm(self):
        if self._invsqrtm is not None:
            return self._invsqrtm

        self._compute_eigen()
        self._invsqrtm = CovMats(
            numpy.dot(numpy.dot(self._eigen_vectors, numpy.diag(1.0 / numpy.sqrt(self._eigen_values))),
                      self._eigen_vectors_transpose), False)
        return self._invsqrtm

    @property
    def expm(self):
        if self._expm is not None:
            return self._expm

        self._compute_eigen()
        self._expm = CovMats(numpy.dot(numpy.dot(self._eigen_vectors, numpy.diag(numpy.exp(self._eigen_values))),
                                       self._eigen_vectors_transpose), False)
        return self._expm

    @property
    def logm(self):
        if self._logm is not None:
            return self._logm

        self._compute_eigen()
        self._logm = CovMats(numpy.dot(numpy.dot(self._eigen_vectors, numpy.diag(numpy.log(self._eigen_values))),
                                       self._eigen_vectors_transpose), False)
        return self._logm

    def powm(self, power):
        if power == 1:
            return self

        if self._power == power:
            return self._powm

        self._compute_eigen()
        self._powm = CovMats(numpy.dot(numpy.dot(self._eigen_vectors, numpy.diag(self._eigen_values ** power)),
                                       self._eigen_vectors_transpose), False)
        self._power = power
        return self._powm

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def get_list(self):
        return self.__covmats

    def randomize(self, data_type=DataType.double):
        self.__covmats_from_list([CovMat.random(self.matrices_order, data_type) for i in range(self.length)])

    def reset_covmats_fields(self):
        for covmat in self.__covmats:
            covmat.reset_fields()
        self.reset_fields()

    def add(self, arg):
        self.__covmats.append(arg)
        self.__covmats_from_list(self.__covmats, self._data_type)

    def add_all(self, arg):
        self.__covmats += arg
        self.__covmats_from_list(self.__covmats, self._data_type)

    def remove(self, arg):
        self.__covmats.remove(arg)
        self.__covmats_from_list(self.__covmats, self._data_type)

    def remove_all(self, arg):
        self.__covmats = [covmat for covmat in self.__covmats if covmat not in arg]
        self.__covmats_from_list(self.__covmats, self._data_type)

    def pop(self, arg):
        self.__covmats.pop(arg)
        self.__covmats_from_list(self.__covmats, self._data_type)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __iter__(self):
        return iter(self.__covmats)
