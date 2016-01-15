import os
import sys
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMat import CovMat


class CovMats(object):
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg, copy=True, data_type=CovMat.DataType.double):
        self.__data_type = data_type
        self.__covmats = []
        if isinstance(arg, list):
            self.__covmats_from_list(arg, data_type)
        elif isinstance(arg, numpy.ndarray):
            self.__covmats_from_numpy_array(arg, copy, data_type)

    @staticmethod
    def random(length, matrices_order, data_type=CovMat.DataType.double):
        list = []
        for i in range(length):
            list.append(CovMat.random(matrices_order, data_type))
        return CovMats(list)

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def length(self):
        return self.shape[0]

    @property
    def matrices_order(self):
        return self.shape[1]

    @property
    def shape(self):
        return self.__numpy_array.shape

    @property
    def numpy_array(self):
        return self.__numpy_array

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def __covmats_from_list(self, arg, data_type=CovMat.DataType.double):
        if len(arg) == 0:
            raise ValueError("There is currently no covmat in the list")
        self.__numpy_array = numpy.array([covmat.numpy_array for covmat in arg], dtype=data_type)
        self.__covmats = arg
        for i in range(self.__numpy_array.shape[0]):
            self.__covmats[i].set_numpy_array_for_covmats(self.__numpy_array[i, :, :])

    def __covmats_from_numpy_array(self, arg, copy, data_type=CovMat.DataType.double):
        self.__numpy_array = numpy.array(arg, dtype=data_type, copy=copy)
        for i in range(self.__numpy_array.shape[0]):
            self.__covmats.append(CovMat(self.__numpy_array[i, :, :], False))

    def to_list(self):
        return self.__covmats

    def randomize(self, ):
        l = []
        for i in range(self.length):
            l.append(CovMat.random(self.matrices_order, self.__data_type))

    def reset_fields(self):
        for covmat in self.__covmats:
            covmat.reset_fields()

    def add(self, arg):
        self.__covmats.append(arg)
        self.__covmats_from_list(self.__covmats, self.__data_type)

    def add_all(self, arg):
        self.__covmats += arg
        self.__covmats_from_list(self.__covmats, self.__data_type)

    def remove(self, arg):
        self.__covmats.remove(arg)
        self.__covmats_from_list(self.__covmats, self.__data_type)

    def remove_all(self, arg):
        self.__covmats = [covmat for covmat in self.__covmats if covmat not in arg]
        self.__covmats_from_list(self.__covmats, self.__data_type)

    def pop(self, arg):
        self.__covmats.pop(arg)
        self.__covmats_from_list(self.__covmats, self.__data_type)

    def mean(self, axis=None):
        return numpy.mean(self.numpy_array, axis)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __getitem__(self, slice):
        if isinstance(slice, int):
            return self.__covmats[slice]
        else:
            return self.__numpy_array[slice]

    def __str__(self):
        return str(self.__numpy_array)

    def __iter__(self):
        return iter(self.__covmats)
