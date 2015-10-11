#!/usr/bin/python

import numpy
from Utils.CovMat import CovMat
import Utils.Environment as Environment


class CovMats(object) :
  # ----------------------------------------------------------------------------------- #
  # ------------------------------- COVMATS CONSTRUCTORS ------------------------------ #
  # ----------------------------------------------------------------------------------- #
  
  def __init__(self, arg, memory_safe_state=Environment.memory_safe_state):
    if isinstance(arg, list):
      self._covmats = arg
      self._modif = True
    elif isinstance(arg, numpy.ndarray):
      self._covmats = []
      for i in range(arg.shape[0]):
        self._covmats.append(CovMat.(arg[i, :, :], memory_safe_state))
        
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
  
  def __getitem__(self, i, j = None, k = None):
    if j is None and k is None:
      return self._covmats[i]
    elif j is not None and k is not None:
      return self.numpy_array[i, j, k]
    else:
      raise ValueError("second and third parameter have to be both set or not")
  
  @property
  def size(self):
    return len(self._covmats)
  
  @property
  def matrices_order(self):
    return self._covmats[0].matrix_order
  
  @property
  def numpy_array(self):
    if self._modif:
      self._modif = False
      self._numpy_array = numpy.dstack(self._covmats)
      return self._numpy_array
    else:
      return self._numpy_array
  
  # ------------------------------------------------------------------------------ #
  # ------------------------------- USUAL FUNCTIONS ------------------------------ #
  # ------------------------------------------------------------------------------ #
  
  def append(self, covmat):
    self._covmats.append(covmat)
    self._modif = True
