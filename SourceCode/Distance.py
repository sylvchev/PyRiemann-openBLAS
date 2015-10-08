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



	@staticmethod
	def Kullback(covMat1, covMat2) :
		return 0.5 * ((covMat2.Inverse() * covMat1).Trace() - covMat1.MatrixOrder() + numpy.log(covMat2.Determinant() / covMat1.Determinant()))



	@staticmethod
	def KullbackRight(covMat1, covMat2) :
		return Distance.Kullback(covMat2, covMat1)



	@staticmethod
	def KullbackSym(covMat1, covMat2) :
		return Distance.Kullback(covMat1, covMat2) + Distance.KullbackRight(covMat1, covMat2)