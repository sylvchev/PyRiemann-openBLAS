#!/usr/bin/python

import numpy
from CovMat import CovMat

class Distance :
  @staticmethod
  def Euclidean(covMat1, covMat2) :
    return (covMat1 - covMat2).Norm()



  @staticmethod
  def LogEuclidean(covMat1, covMat2) :
    return (covMat1.Logm() - covMat2.Logm()).Norm()
