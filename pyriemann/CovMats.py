# import os
# import sys
import numpy as np
# import numpy as np
# from numpy.linalg import inv

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .AbsClass import Abstract_Covariance_Matrix
from .CovMat import Covariance_Matrix
# from Utils.DataType import DataType
# import Utils.OpenBLAS
# from sklearn.base import BaseEstimator, TransformerMixin

class Covariance_Matrices(Abstract_Covariance_Matrix): # , BaseEstimator, TransformerMixin
    # ---------------------------------------------------------------------- #
    # ------------------------------- FIELDS ------------------------------- #
    # ---------------------------------------------------------------------- #

    __covmats = None

    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg=None, copy=True, dtype=np.double): # , estimator='scm'
        self._dtype = dtype
        # self.estimator = estimator
        if isinstance(arg, list):
            self.__covmats_from_list(arg, dtype)
        elif isinstance(arg, np.ndarray):
            self.__covmats_from_array(arg, copy, dtype)

    def __covmats_from_list(self, arg, dtype=np.double):
        if len(arg) == 0:
            raise ValueError("The list is empty.")
        self.reset_fields()
        self._array = np.array([covmat for covmat in arg], dtype=dtype)
        self.__covmats = arg
        for i, covmat in enumerate(self.__covmats):
            covmat[:] = self._array[i, :, :]

    def __covmats_from_array(self, arg, copy, dtype=np.double):
        self.reset_fields()
        self._array = np.array(arg, dtype=dtype, copy=copy)
        self.__covmats = [Covariance_Matrix(self._array[i, :, :], False)
                          for i in range(self.length)]

    @staticmethod
    def random(nb_mat, dim, dtype=np.double):
        return Covariance_Matrices([Covariance_Matrix.random(dim, dtype)
                                    for i in range(nb_mat)])
    
    # ----------------------------------------------------------------------- #
    # ------------------------------- GETTERS ------------------------------- #
    # ----------------------------------------------------------------------- #

    @property
    def length(self):
        return self._array.shape[0]

    @property
    def dim(self):
        return self._array.shape[1]

    def get_covmat(self, index):
        return self.__covmats[index]

    @property
    def transpose(self):
        return self._array.T

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def reset_fields(self):
        self.__mean = None

    def reset_covmats_fields(self):
        for covmat in self.__covmats:
            covmat.reset_fields()

    def get_list(self):
        return self.__covmats

    # See random
    # def randomize(self, dtype=np.double):
    #     self.__covmats_from_list([CovMat.random(self.dim, dtype)
    #                               for i in range(self.length)])

    
    def add(self, arg):
        self.__covmats.append(arg)
        self.__covmats_from_list(self.__covmats, self._dtype)

    def add_all(self, arg):
        self.__covmats += arg
        self.__covmats_from_list(self.__covmats, self._dtype)

    def remove(self, arg):
        self.__covmats.remove(arg)
        self.__covmats_from_list(self.__covmats, self._dtype)

    def remove_all(self, arg):
        self.__covmats = [covmat for covmat in self.__covmats if covmat not in arg]
        self.__covmats_from_list(self.__covmats, self._dtype)

    def pop(self, arg):
        self.__covmats.pop(arg)
        self.__covmats_from_list(self.__covmats, self._dtype)

    # ------------------------------------------------------------------------- #
    # ------------------------------- OPERATORS ------------------------------- #
    # ------------------------------------------------------------------------- #

    def __iter__(self):
        return iter(self.__covmats)

    def __setitem__(self, key, value):
        self._array[key] = value
        self.reset_fields()
        self.reset_covmats_fields()

