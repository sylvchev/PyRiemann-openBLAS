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



	@staticmethod
	def LogDeterminant(covMat1, covMat2) :
		return numpy.sqrt(numpy.log(((covMat1 + covMat2)/2).Determinant()) - 0.5 * numpy.log((covMat1 * covMat2).Determinant()))



	@staticmethod
	def Riemannian(covMat1, covMat2) :
		return numpy.sqrt((numpy.log(CovMat.SolveProblem(covMat1, covMat2))**2).sum())