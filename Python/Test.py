#!/usr/bin/python 

from CovMat import CovMat
from Distance import Distance
from Geodesic import Geodesic

covMat1 = CovMat(5)
covMat2 = CovMat(5)
covMat1.Randomize()
covMat2.Randomize()

print("covMat1 :\n" + str(covMat1) + "\n")
print("covMat1 :\n" + str(covMat2) + "\n")

print("covMat1.Norm() :\n" + str(covMat1.Norm()) + "\n")
print("covMat1.Determinant() :\n" + str(covMat1.Determinant()) + "\n")
print("covMat1.Sqrtm() :\n" + str(covMat1.Sqrtm()) + "\n")
print("covMat1.Invsqrtm() :\n" + str(covMat1.Invsqrtm()) + "\n")
print("covMat1.Expm() :\n" + str(covMat1.Expm()) + "\n")
print("covMat1.Logm() :\n" + str(covMat1.Logm()) + "\n")
print("covMat1.Powm(2) :\n" + str(covMat1.Powm(2)) + "\n")

print("Distance.Euclidean(covMat1, covMat2) :\n" + str(Distance.Euclidean(covMat1, covMat2)) + "\n")
print("Distance.LogEuclidean(covMat1, covMat2) :\n" + str(Distance.LogEuclidean(covMat1, covMat2)) + "\n")
print("Distance.LogDeterminant(covMat1, covMat2) :\n" + str(Distance.LogDeterminant(covMat1, covMat2)) + "\n")
print("Distance.Riemannian(covMat1, covMat2) :\n" + str(Distance.Riemannian(covMat1, covMat2)) + "\n")

print("Geodesic.Euclidean(covMat1, covMat2, 0.5) :\n" + str(Geodesic.Euclidean(covMat1, covMat2, 0.5)) + "\n")
print("Geodesic.LogEuclidean(covMat1, covMat2, 0.5) :\n" + str(Geodesic.LogEuclidean(covMat1, covMat2, 0.5)) + "\n")
print("Geodesic.Riemannian(covMat1, covMat2, 0.5) :\n" + str(Geodesic.Riemannian(covMat1, covMat2, 0.5)) + "\n")