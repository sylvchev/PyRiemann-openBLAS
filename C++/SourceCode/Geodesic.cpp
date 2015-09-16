#include <iostream>
#include <eigen3/Eigen/Dense>
#include "Geodesic.hpp"
#include "CovMat.hpp"

using namespace std;
using namespace Eigen; 
 
CovMat Geodesic::EuclideanGeodesic (const CovMat& covMat1, const CovMat& covMat2, double alpha)
{
	return (1 - alpha)*covMat1 + alpha * covMat2;
}

CovMat Geodesic::LogEuclideanGeodesic (CovMat& covMat1, CovMat& covMat2, double alpha)
{
	return ((1 - alpha)*covMat1.Logm() + alpha * covMat2.Logm()).Expm();
}

CovMat Geodesic::RiemannianGeodesic (CovMat& covMat1, CovMat& covMat2, double alpha)
{
	CovMat covMat1Sqrtm = covMat1.Sqrtm();
	CovMat covMat1Invsqrtm = covMat1.Invsqrtm();

	CovMat tmp(covMat1.matrixOrder);
	tmp.eigenMatrix.noalias() = covMat1Invsqrtm.eigenMatrix * covMat2.eigenMatrix;
	tmp.eigenMatrix *= covMat1Invsqrtm.eigenMatrix;

	CovMat result(covMat1.matrixOrder);
	result.eigenMatrix.noalias() = covMat1Sqrtm.eigenMatrix * tmp.Powm(alpha).eigenMatrix;
	result.eigenMatrix *= covMat1Sqrtm.eigenMatrix;

	return result;
}