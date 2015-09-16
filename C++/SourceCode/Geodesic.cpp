#include <iostream>
#include <armadillo>
#include "Geodesic.hpp"
#include "CovMat.hpp"

using namespace std;
using namespace arma; 
 
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

	CovMat tmp = covMat1Invsqrtm * covMat2 * covMat1Invsqrtm;

	return CovMat(covMat1Sqrtm * tmp.Powm(alpha) * covMat1Sqrtm);
}