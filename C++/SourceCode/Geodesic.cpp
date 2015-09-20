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
	return CovMat(covMat1.Sqrtm() * (covMat1.Invsqrtm() * covMat2 * covMat1.Invsqrtm()).Powm(alpha) * covMat1.Sqrtm());
}
