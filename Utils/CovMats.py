#!/usr/bin/python

import numpy
from Utils.CovMat import CovMat
import Utils.Environment as Environment


class CovMats(object):
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg, memory_safe_state=Environment.memory_safe_state):
        if isinstance(arg, list):
            self._covmats = arg
            self._numpy_array = None
            self._modif = True
        elif isinstance(arg, numpy.ndarray):
            self._covmats = []
            for i in range(arg.shape[0]):
                self._covmats.append(CovMat(arg[i, :, :], memory_safe_state))

            if memory_safe_state:
                self._numpy_array = arg.copy()
            else:
                self._numpy_array = arg

            self._modif = False
        else:
            self._covmats = []
            self._numpy_array = None
            self._modif = True

    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def size(self):
        return len(self._covmats)

    @property
    def matrices_order(self):
        if self.size == 0:
            raise ValueError("the array is empty...")
        else:
            return self._covmats[0].matrix_order

    @property
    def numpy_array(self):
        if self._modif:
            self._modif = False
            self._numpy_array = numpy.dstack([covmat.matrix for covmat in self._covmats])
            return self._numpy_array
        else:
            return self._numpy_array

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def append(self, covmat):
        self._covmats.append(covmat)
        self._modif = True

    def remove(self, arg):
        if isinstance(arg, int):
            self._covmats.pop(arg)
        elif isinstance(arg, CovMat):
            self._covmats.remove(arg)

        self._modif = True

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __getitem__(self, slice):
        return self.numpy_array[slice]

    def __str__(self):
        return str(self.numpy_array)
