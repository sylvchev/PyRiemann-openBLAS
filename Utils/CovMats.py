#!/usr/bin/python

import sys
import os
import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Utils.Environment as Environment
from Utils.CovMat import CovMat


class CovMats(object):
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg=None, memory_safe_state=Environment.memory_safe_state):
        if arg is None:
            self.__covmats = []
            self.__numpy_array = None
            self.__modif = True
        elif isinstance(arg, list):
            self.__covmats = arg
            self.__numpy_array = None
            self.__modif = True
        elif isinstance(arg, numpy.ndarray):
            self.__covmats = []
            for i in range(arg.shape[0]):
                self.__covmats.append(CovMat(arg[i, :, :], memory_safe_state))
            if memory_safe_state:
                self.__numpy_array = arg.copy().view(Environment.data_type, numpy.ndarray)
            else:
                self.__numpy_array = arg.view(Environment.data_type, numpy.ndarray)
            self.__modif = False

    @staticmethod
    def random(matrices_order, size):
        covmats = CovMats()
        covmats.randomize(matrices_order, size)

        return covmats

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def size(self):
        return len(self.__covmats)

    @property
    def matrices_order(self):
        if self.size == 0:
            raise ValueError("the array is empty...")
        else:
            return self.__covmats[0].matrix_order

    @property
    def numpy_array(self):
        if self.__modif:
            self.__modif = False
            self.__numpy_array = numpy.array(
                [numpy.array(covmat.matrix, dtype=Environment.data_type, copy=False) for covmat in self.__covmats],
                dtype=Environment.data_type, copy=False)
            return self.__numpy_array
        else:
            return self.__numpy_array

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def to_list(self):
        return self.__covmats

    def append(self, arg):
        if isinstance(arg, CovMat):
            self.__covmats.append(arg)
        elif isinstance(arg, list):
            self.__covmats += arg

        self.__modif = True

    def remove(self, arg):
        if isinstance(arg, int):
            self.__covmats.pop(arg)
        elif isinstance(arg, CovMat):
            self.__covmats.remove(arg)

        self.__modif = True

    def randomize(self, matrices_order, size):
        self.__modif = True
        self.__covmats = []
        for i in range(size):
            self.__covmats.append(CovMat.random(matrices_order))

    def reset_matrices_fields(self):
        for covmat in self.__covmats:
            covmat.reset_fields()

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

    def __add__(self, other):
        return CovMats(self.__covmats + other.to_list())

    def __iadd__(self, other):
        self.__covmats += other.to_list()
        self.__modif = True
        return self

    def __sub__(self, other):
        return CovMats([covmat for covmat in self.__covmats if covmat not in other.to_list()])

    def __isub__(self, other):
        self.__covmats -= other.to_list()
        self.__modif = True
        return self