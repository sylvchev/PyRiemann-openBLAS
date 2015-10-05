#!/usr/bin/python
 
class Geodesic :
	@staticmethod
	def Euclidean(covMat1, covMat2, alpha) :
		return covMat1 + alpha * (covMat2 - covMat1)



	@staticmethod
	def LogEuclidean(covMat1, covMat2, alpha) :
		return (covMat1.Logm() + alpha * (covMat2.Logm() - covMat1.Logm())).Expm()



	@staticmethod
	def Riemannian(covMat1, covMat2, alpha) :
		return covMat1.Sqrtm() * (covMat1.Invsqrtm() * covMat2 * covMat1.Invsqrtm()).Powm(alpha) * covMat1.Sqrtm()
