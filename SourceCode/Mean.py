#!/usr/bin/python

import Environment
import numpy
from CovMat import CovMat

class Mean :
	@staticmethod
	def SampleWeight(sampleWeight, covMats) :
		if (sampleWeight is None) :
			sampleWeight = numpy.ones(len(covMats))

		if (len(covMats) != len(sampleWeight)) :
			raise ValueError("len of sample_weight must be equal to len of data.")

		sampleWeight /= numpy.sum(sampleWeight)

		return sampleWeight



	@staticmethod
	def Identity (covMats) :
		matrixOrder = covMats[0].MatrixOrder()
		return CovMat.Identity(matrixOrder)



	@staticmethod
	def Euclidean (covMats, sampleWeight = None) :
		nbCovMats = len(covMats)
		matrixOrder = covMats[0].MatrixOrder()
		sampleWeight = Mean.SampleWeight(sampleWeight, covMats)

		output = CovMat.Zero(matrixOrder)

		for i in range(nbCovMats) :
			output += sampleWeight[i] * covMats[i]

		return output




	@staticmethod
	def LogEuclidean (covMats, sampleWeight = None) :
		nbCovMats = len(covMats)
		matrixOrder = covMats[0].MatrixOrder()
		sampleWeight = Mean.SampleWeight(sampleWeight, covMats)

		output = CovMat.Zero(matrixOrder)

		for i in range(nbCovMats) :
			output += sampleWeight[i] * covMats[i].Logm()

		return output.Expm()




	@staticmethod
	def LogDeterminant (covMats, tol=10e-5, maxIter=50, init=None, sampleWeight = None) :
		nbCovMats = len(covMats)
		matrixOrder = covMats[0].MatrixOrder()
		sampleWeight = Mean.SampleWeight(sampleWeight, covMats)

		if (init is None) :
			output = Mean.Euclidean(covMats)
		else :
			output = init

		k = 0
		crit = numpy.finfo(Environment.dataType).max
		tmp = CovMat(matrixOrder)

		while ((crit > tol) & (k < maxIter)) :
			k = k + 1
			tmp.Fill(0)

			for i in range(nbCovMats) :
				tmp += sampleWeight[i] * (0.5 * (covMats[i] + output)).Inverse()

			newOutput = tmp.Inverse()
			crit = (newOutput - output).Norm()
			output = newOutput

		if (k == maxIter) :
			print("Max iter reach")

		return output




	@staticmethod
	def Riemannian (covMats, tol=10e-9, maxIter=50, init=None, sampleWeight = None) :
		sampleWeight = Mean.SampleWeight(sampleWeight, covMats)
		nbCovMats = len(covMats)
		matrixOrder = covMats[0].MatrixOrder()

		if (init is None) :
			output = Mean.Euclidean(covMats)
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

			for i in range(nbCovMats) :
				tmp += sampleWeight[i] * (output.Invsqrtm() * covMats[i] * output.Invsqrtm()).Logm()

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

		return output
