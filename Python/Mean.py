#!/usr/bin/python

import numpy
from CovMat import CovMat

class Mean :
	@staticmethod
	def Identity (covMats) :
		matrixOrder = covMats[0].GetMatrixOrder()
		return CovMat.Identity(matrixOrder)



	@staticmethod
	def Euclidean (covMats) :
		nbCovMats = len(covMats)
		matrixOrder = covMats[0].GetMatrixOrder()

		output = CovMat.Zeros(matrixOrder)

		for covMat in covMats :
			output += covMat

		output /= nbCovMats

		return output




	@staticmethod
	def LogEuclidean (covMats) :
		nbCovMats = len(covMats)
		matrixOrder = covMats[0].GetMatrixOrder()

		output = CovMat.Zeros(matrixOrder)

		for covMat in covMats :
			output += covMat.Logm()

		output = (output/nbCovMats).Expm()

		return output




	@staticmethod
	def LogDeterminant (covMats, tol=10e-5, maxIter=50, init=None) :
		nbCovMats = len(covMats)
		matrixOrder = covMats[0].GetMatrixOrder()

		if (init is None) :
			output = self.Euclidean(covMats)
		else :
			output = init

		k = 0
		crit = numpy.finfo(Environment.dataType).max
		tmp = CovMat(matrixOrder)

		while ((crit > tol) & (k < maxIter)) :
			k = k + 1
			tmp.Fill(0)

			for covMat in covMats :
				tmp += (0.5 * (covMat + output)).Inverse()
			tmp /= nbCovMats

			newOutput = tmp.Inverse()
			crit = (newOutput - output).Norm()
			output = newOutput

		if (k == maxIter) :
    		print("Max iter reach")

		return output




	@staticmethod
	def Riemann (covMats, tol=10e-9, maxIter=50, init=None) :
		nbCovMats = len(covMats)
		matrixOrder = covMats[0].GetMatrixOrder()

		if (init is None) :
			output = self.Euclidean(covMats)
		else :
			output = init

		k = 0
		nu = 1.0
		tau = numpy.finfo(Environment.dataType).max
		crit = numpy.finfo(Environment.dataType).max
		tmp = CovMat(matrixOrder)

		while ((crit > tol) & (k < maxIter) & (nu > tol)) :
			k = k + 1
			tmp.Fill(0)

			for covMat in covMats :
				tmp += (output.Invsqrtm() * covMat * output.Invsqrtm()).Logm()
			tmp /= nbCovMats

			crit = tmp.Norm()
			h = nu*crit

			output = output.Sqrtm() * (nu * tmp).Expm() * output.Sqrtm()

			if h < tau:
				nu = 0.95 * nu
				tau = h
			else:
				nu = 0.5 * nu

			if (k == maxIter) :
    			print("Max iter reach")

		return C