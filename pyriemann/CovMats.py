# import os
# import sys
import numpy
import numpy as np
from numpy.linalg import inv

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .AbsClass import AbsClass
from .CovMat import CovMat
# from Utils.DataType import DataType
# import Utils.OpenBLAS
from sklearn.base import BaseEstimator, TransformerMixin

class CovMats(AbsClass, BaseEstimator, TransformerMixin):
    # ---------------------------------------------------------------------- #
    # ------------------------------- FIELDS ------------------------------- #
    # ---------------------------------------------------------------------- #

    __covmats = None

    # ----------------------------------------------------------------------------------- #
    # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
    # ----------------------------------------------------------------------------------- #

    def __init__(self, arg=None, copy=True, data_type=np.double, estimator='scm'):
        self._data_type = data_type
        self.estimator = estimator
        if isinstance(arg, list):
            self.__covmats_from_list(arg, data_type)
        elif isinstance(arg, numpy.ndarray):
            self.__covmats_from_numpy_array(arg, copy, data_type)

    def __covmats_from_list(self, arg, data_type=np.double):
        if len(arg) == 0:
            raise ValueError("The list is empty.")
        self.reset_fields()
        self._numpy_array = numpy.array([covmat.numpy_array for covmat in arg], dtype=data_type)
        self.__covmats = arg
        for i, covmat in enumerate(self.__covmats):
            covmat[:] = self._numpy_array[i, :, :]

    def __covmats_from_numpy_array(self, arg, copy, data_type=np.double):
        self.reset_fields()
        self._numpy_array = numpy.array(arg, dtype=data_type, copy=copy)
        self.__covmats = [CovMat(self._numpy_array[i, :, :], False) for i in range(self.length)]

    @staticmethod
    def random(length, matrices_order, data_type=np.double):
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
    def transpose(self):
        return self._numpy_array.T

    # ------------------------------------------------------------------------------ #
    # ------------------------------- USUAL FUNCTIONS ------------------------------ #
    # ------------------------------------------------------------------------------ #

    def reset_fields(self):
        self._determinant = None
        self._inverse = None

    def reset_covmats_fields(self):
        for covmat in self.__covmats:
            covmat.reset_fields()

    def get_list(self):
        return self.__covmats

    def randomize(self, data_type=np.double):
        self.__covmats_from_list([CovMat.random(self.matrices_order, data_type) for i in range(self.length)])

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

    def __setitem__(self, key, value):
        self._numpy_array[key] = value
        self.reset_fields()
        self.reset_covmats_fields()

    # ------------------------------------------------------------------------- #
    # -------------------------------- SKLEARN -------------------------------- #
    # ------------------------------------------------------------------------- #
    
    def fit(self, X, y=None):
        """Fit.

        Do nothing. For compatibility purpose.

        Parameters
        ----------
        X : ndarray, shape (n_trials, n_channels, n_samples)
            ndarray of trials.
        y : ndarray shape (n_trials, 1)
            labels corresponding to each trial, not used.

        Returns
        -------
        self : Covariances instance
            The Covariances instance.
        """
        return self

    def transform(self, X):
        """Estimate covariance matrices.

        Parameters
        ----------
        X : ndarray, shape (n_trials, n_channels, n_samples)
            ndarray of trials.

        Returns
        -------
        covmats : ndarray, shape (n_trials, n_channels, n_channels)
            ndarray of covariance matrices for each trials.
        """
        # covmats = covariances(X, estimator=self.estimator)
        # return covmats
        return self
        
