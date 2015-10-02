#!/usr/bin/python

import numpy
from CovMat import CovMat 

class Geodesic :
	@staticmethod
	def Euclidean(covMat1, covMat2, alpha) :
		return (1 - alpha) * covMat1 +  alpha * covMat2



	@staticmethod
	def LogEuclidean(covMat1, covMat2, alpha) :
		return ((1 - alpha) * covMat1.Logm() +  alpha * covMat2.Logm()).Expm()



	@staticmethod
	def Riemannian(covMat1, covMat2, alpha) :
		return covMat1.Sqrtm() * (covMat1.Invsqrtm() * covMat2 * covMat1.Invsqrtm()).Powm(alpha) * covMat1.Sqrtm()