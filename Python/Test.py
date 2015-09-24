#!/usr/bin/python 

from CovMat import CovMat
from Distance import Distance

covMat = CovMat(5)
covMat2 = CovMat(5)
covMat.Randomize()
covMat2.Randomize()

print("covMat :\n" + str(covMat) + "\n")

print("covMat.Sqrtm() :\n" + str(covMat.Sqrtm()) + "\n")
print("covMat.Invsqrtm() :\n" + str(covMat.Invsqrtm()) + "\n")
print("covMat.Expm() :\n" + str(covMat.Expm()) + "\n")
print("covMat.Logm() :\n" + str(covMat.Logm()) + "\n")
print("covMat.Powm(2) :\n" + str(covMat.Powm(2)) + "\n")

print("Distance.Euclidean(covMat, covMat2) :\n" + str(Distance.Euclidean(covMat, covMat2)) + "\n")
print("Distance.LogEuclidean(covMat, covMat2) :\n" + str(Distance.LogEuclidean(covMat, covMat2)) + "\n")
