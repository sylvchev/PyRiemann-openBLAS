import os
import sys
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Utils.CovMat import CovMat


class CovMats(object):
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg=None):
        if arg is None:
            self.__covmats = []
        else:
            self.__covmats = arg
        self.__numpy_array = None

    @staticmethod
    def random(length, matrices_order, data_type=CovMat.DataType.double):
        list = []
        for i in range(0, length):
            list.append(CovMat.random(matrices_order, data_type))
        return CovMats(list)

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def length(self):
        if len(self.__covmats) == 0:
            raise ValueError("There is currently no covmat in the list")
        return len(self.__covmats)

    @property
    def matrices_order(self):
        if len(self.__covmats) == 0:
            raise ValueError("There is currently no covmat in the list")
        return self.__covmats[0].matrix_order

    @property
    def shape(self):
        return [self.length, self.matrices_order, self.matrices_order]

    @property
    def numpy_array(self):
        if len(self.__covmats) == 0:
            raise ValueError("There is currently no covmat in the list")
        else:
            if self.__numpy_array is None:
                self.__numpy_array = numpy.array([covmat.numpy_array for covmat in self.__covmats], copy=False)

            return self.__numpy_array

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def to_list(self):
        return self.__covmats

    def randomize(self):
        self.__numpy_array = None
        for covmat in self.__covmats:
            covmat.randomize()

    def reset_fields(self):
        self.__numpy_array = None
        for covmat in self.__covmats:
            covmat.reset_fields()

    def append(self, arg):
        if isinstance(arg, list):
            self.__covmats += arg
        else:
            self.__covmats.append(arg)
        self.__numpy_array = None

    def remove(self, arg):
        self.__covmats.remove(arg)
        self.__numpy_array = None

    def pop(self, arg):
        self.__covmats.pop(arg)
        self.__numpy_array = None

    def mean(self, axis=None):
        if axis is None:
            mean = 0
            for numpy_array in [covmat.numpy_array for covmat in self.__covmats]:
                mean += numpy.mean(numpy_array)
            return mean / self.length
        elif axis == 0:
            mean = numpy.zeros((self.matrices_order, self.matrices_order))
            for covmat in self.__covmats:
                mean += covmat.numpy_array
            return CovMat(mean / self.length)
        else:
            return numpy.mean(self.numpy_array, axis)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __getitem__(self, slice):
        if isinstance(slice, int):
            return self.__covmats[slice]
        else:
            return self.numpy_array[slice]

    def __str__(self):
        return str(self.numpy_array)

    def __iter__(self):
        return iter(self.__covmats)
