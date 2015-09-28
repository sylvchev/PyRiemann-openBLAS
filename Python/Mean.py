#!/usr/bin/python

import numpy
from CovMat import CovMat

class Mean :
	@staticmethod
	def Identity (covMats) :
		return CovMat(numpy.matrix(numpy.identity(covMats.shape[0], numpy.dtype('d')), numpy.dtype('d'), False))



	@staticmethod
	def Euclidean (covMats) :
		output = CovMat(covMats[0].shape[0])

		for covMat in covMats :
			output += covMat

		output /= covMat.shape[0]

		return output