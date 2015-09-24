#!/usr/bin/python

import numpy
from CovMat import CovMat

class Distance :
  def __init__(self) :
  
  
  
  @staticmethod
  def Euclidean(covMat1, covMat2) :
    return (covMat1 - covMat2).Norm()



  @staticmethod
  def LogEuclidean(covMat1, covMat2) :
    return (covMat1.Logm() - covMat2.Logm()).Norm()
