#!/usr/bin/python 

import Environment
from CovMat import CovMat
from Distance import Distance
from Geodesic import Geodesic
from Mean import Mean

covMat1 = CovMat.Random(5)
covMat2 = CovMat.Random(5)

covMats = []
for i in range(0, 20) :
	tmp = CovMat.Random(200)
	covMats.append(tmp)

print("covMat1 :\n" + str(covMat1) + "\n")
print("covMat2 :\n" + str(covMat2) + "\n")

print("CovMat.Zero(10) :\n" + str(CovMat.Zero(10)) + "\n")
print("CovMat.Identity(10) :\n" + str(CovMat.Identity(10)) + "\n")
print("CovMat.Random(10) :\n" + str(CovMat.Random(10)) + "\n")

print("covMat1.Sum() :\n" + str(covMat1.Sum()) + "\n")
print("covMat1.Sum(1) :\n" + str(covMat1.Sum(1)) + "\n")
print("covMat1.Product() :\n" + str(covMat1.Product()) + "\n")
print("covMat1.Product(1) :\n" + str(covMat1.Product(1)) + "\n")
print("covMat1.Column(1) :\n" + str(covMat1.Column(1)) + "\n")
print("covMat1.Row(1) :\n" + str(covMat1.Row(1)) + "\n")
print("covMat1.Maximum() :\n" + str(covMat1.Maximum()) + "\n")
print("covMat1.Maximum(0) :\n" + str(covMat1.Maximum(0)) + "\n")
print("covMat1.Minimum() :\n" + str(covMat1.Minimum()) + "\n")
print("covMat1.Minimum(0) :\n" + str(covMat1.Minimum(0)) + "\n")
print("covMat1.Mean() :\n" + str(covMat1.Mean()) + "\n")
print("covMat1.Mean(0) :\n" + str(covMat1.Mean(0)) + "\n")
print("covMat1.Variance() :\n" + str(covMat1.Variance()) + "\n")
print("covMat1.Variance(0) :\n" + str(covMat1.Variance(0)) + "\n")
print("covMat1.Norm() :\n" + str(covMat1.Norm()) + "\n")
print("covMat1.Determinant() :\n" + str(covMat1.Determinant()) + "\n")

print("covMat1.Inverse() :\n" + str(covMat1.Inverse()) + "\n")
print("covMat1.Transpose() :\n" + str(covMat1.Transpose()) + "\n")
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

print("Mean.Identity(covMats) :\n" + str(Mean.Identity(covMats)) + "\n")
print("Mean.Euclidean(covMats) :\n" + str(Mean.Euclidean(covMats)) + "\n")
print("Mean.LogEuclidean(covMats) :\n" + str(Mean.LogEuclidean(covMats)) + "\n")
print("Mean.LogDeterminant(covMats) :\n" + str(Mean.LogDeterminant(covMats)) + "\n")
print("Mean.Riemannian(covMats) :\n" + str(Mean.Riemannian(covMats)) + "\n")