import os
import sys
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMat import CovMat


class CovMats(object):
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg):
        self.__covmats = arg
        self.__numpy_array = numpy.array([covmat.numpy_array for covmat in self.__covmats], copy=False)

    @staticmethod
    def random(matrices_order, size, data_type=CovMat.DataType.double):
        list = []
        for i in range(0, size):
            list.append(CovMat.random(matrices_order, data_type))
        return CovMats(list)

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def shape(self):
        return self.__numpy_array.shape

    @property
    def numpy_array(self):
        return self.__numpy_array

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def to_list(self):
        return self.__covmats

    def randomize(self):
        for covmat in self.__covmats:
            covmat.randomize()
        self.__numpy_array = numpy.array([covmat.numpy_array for covmat in self.__covmats], copy=False)

    def reset_fields(self):
        for covmat in self.__covmats:
            covmat.reset_fields()

    def append(self, arg):
        if isinstance(arg, list):
            self.__covmats += list
        else:
            self.__covmats.append(arg)
        self.__numpy_array = numpy.array([covmat.numpy_array for covmat in self.__covmats], copy=False)

    def remove(self, arg):
        self.__covmats.remove(arg)
        self.__numpy_array = numpy.array([covmat.numpy_array for covmat in self.__covmats], copy=False)

    def pop(self, arg):
        self.__covmats.pop(arg)
        self.__numpy_array = numpy.array([covmat.numpy_array for covmat in self.__covmats], copy=False)

    def mean(self, axis=None):
        if axis == 0:
            return CovMat(numpy.mean(self.__numpy_array, axis=axis))
        else:
            return numpy.mean(self.__numpy_array, axis=axis)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __getitem__(self, slice):
        if isinstance(slice, int):
            return self.__covmats[slice]
        else:
            return self.numpy_array[slice]

    def __str__(self):
        return str(self.__numpy_array)

    def __iter__(self):
        return iter(self.__covmats)
