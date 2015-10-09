#!/usr/bin/python 

import Utils.Environment as Environment
from Utils.CovMat import CovMat
from Utils.Distance import Distance
from Utils.Geodesic import Geodesic
from Utils.Mean import Mean

covmat1 = CovMat.random(5)
covmat2 = CovMat.random(5)

covmats = []
for i in range(0, 20):
    tmp = CovMat.random(200)
    covmats.append(tmp)

print("covmat1 :\n" + str(covmat1) + "\n")
print("covmat2 :\n" + str(covmat2) + "\n")

print("CovMat.zero(10) :\n" + str(CovMat.zero(10)) + "\n")
print("CovMat.identity(10) :\n" + str(CovMat.identity(10)) + "\n")
print("CovMat.random(10) :\n" + str(CovMat.random(10)) + "\n")

print("covmat1.sum() :\n" + str(covmat1.sum()) + "\n")
print("covmat1.sum(1) :\n" + str(covmat1.sum(1)) + "\n")
print("covmat1.product() :\n" + str(covmat1.product()) + "\n")
print("covmat1.product(1) :\n" + str(covmat1.product(1)) + "\n")
print("covmat1.column(1) :\n" + str(covmat1.column(1)) + "\n")
print("covmat1.row(1) :\n" + str(covmat1.row(1)) + "\n")
print("covmat1.maximum() :\n" + str(covmat1.maximum()) + "\n")
print("covmat1.maximum(0) :\n" + str(covmat1.maximum(0)) + "\n")
print("covmat1.minimum() :\n" + str(covmat1.minimum()) + "\n")
print("covmat1.minimum(0) :\n" + str(covmat1.minimum(0)) + "\n")
print("covmat1.mean() :\n" + str(covmat1.mean()) + "\n")
print("covmat1.mean(0) :\n" + str(covmat1.mean(0)) + "\n")
print("covmat1.variance() :\n" + str(covmat1.variance()) + "\n")
print("covmat1.variance(0) :\n" + str(covmat1.variance(0)) + "\n")
print("covmat1.norm() :\n" + str(covmat1.norm) + "\n")
print("covmat1.determinant() :\n" + str(covmat1.determinant) + "\n")

print("covmat1.inverse() :\n" + str(covmat1.inverse) + "\n")
print("covmat1.transpose() :\n" + str(covmat1.transpose) + "\n")
print("covmat1.sqrtm() :\n" + str(covmat1.sqrtm) + "\n")
print("covmat1.invsqrtm() :\n" + str(covmat1.invsqrtm) + "\n")
print("covmat1.expm() :\n" + str(covmat1.expm) + "\n")
print("covmat1.logm() :\n" + str(covmat1.logm) + "\n")
print("covmat1.powm(2) :\n" + str(covmat1.powm(2)) + "\n")

print("Distance.euclidean(covmat1, covmat2) :\n" + str(Distance.euclidean(covmat1, covmat2)) + "\n")
print("Distance.log_euclidean(covmat1, covmat2) :\n" + str(Distance.log_euclidean(covmat1, covmat2)) + "\n")
print("Distance.log_determinant(covmat1, covmat2) :\n" + str(Distance.log_determinant(covmat1, covmat2)) + "\n")
print("Distance.riemannian(covmat1, covmat2) :\n" + str(Distance.riemannian(covmat1, covmat2)) + "\n")
print("Distance.kullback(covmat1, covmat2) :\n" + str(Distance.kullback(covmat1, covmat2)) + "\n")
print("Distance.kullback_right(covmat1, covmat2) :\n" + str(Distance.kullback_right(covmat1, covmat2)) + "\n")
print("Distance.kullback_sym(covmat1, covmat2) :\n" + str(Distance.kullback_sym(covmat1, covmat2)) + "\n")

print("Geodesic.euclidean(covmat1, covmat2, 0.5) :\n" + str(Geodesic.euclidean(covmat1, covmat2, 0.5)) + "\n")
print("Geodesic.log_euclidean(covmat1, covmat2, 0.5) :\n" + str(Geodesic.log_euclidean(covmat1, covmat2, 0.5)) + "\n")
print("Geodesic.riemannian(covmat1, covmat2, 0.5) :\n" + str(Geodesic.riemannian(covmat1, covmat2, 0.5)) + "\n")

print("Mean.identity(covmats) :\n" + str(Mean.identity(covmats)) + "\n")
print("Mean.euclidean(covmats) :\n" + str(Mean.euclidean(covmats)) + "\n")
print("Mean.log_euclidean(covmats) :\n" + str(Mean.log_euclidean(covmats)) + "\n")
print("Mean.log_determinant(covmats) :\n" + str(Mean.log_determinant(covmats)) + "\n")
print("Mean.riemannian(covmats) :\n" + str(Mean.riemannian(covmats)) + "\n")
