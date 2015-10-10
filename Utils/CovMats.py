#!/usr/bin/python

import numpy
from Utils.CovMat import CovMat


class CovMats(object) :
  # ----------------------------------------------------------------------------------- #
  # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
  # ----------------------------------------------------------------------------------- #
  
  def __ini__(self, arg, memory_safe_state=Environment.memory_safe_state):
    if isinstance(arg, list):
      self._covmats = list
    elif isinstance(arg, numpy.ndarray):
      self._covmats = []
      for i in range(arg.shape[0]):
        self._covmats.append(CovMat.(arg[i, :, :], memory_safe_state))
    else:
      self._covmats = []
  
  # ----------------------------------------------------------------------- #
  # ------------------------------- GETTERS ------------------------------- #
  # ----------------------------------------------------------------------- #
  
  def __getitem__(self, i):
    return self._covmats[i]
  
  @property
  def size(self):
    return len(self._covmats)
  
  @property
  def matrices_order(self):
    return self._covmats[0].matrix_order
  
  # ------------------------------------------------------------------------------ #
  # ------------------------------- USUAL FUNCTIONS ------------------------------ #
  # ------------------------------------------------------------------------------ #
  
  def append(self, covmat):
    self._covmats.append(covmat)
  
  def to_numpy_array(self) :
    return numpy.dstack(self._covmats)
