#include <iostream>
#include <armadillo>
#include "Distance.hpp"
#include "CovMat.hpp"

using namespace std;
using namespace arma; 

double Distance::EuclideanDistance(const CovMat& covMat1, const CovMat& covMat2)
{
	return (covMat1 - covMat2).Norm();
}

double Distance::LogEuclideanDistance(CovMat& covMat1, CovMat& covMat2)
{
	return (covMat1.Logm() - covMat2.Logm()).Norm();
}
	
double Distance::LogDeterminantDistance(const CovMat& covMat1, const CovMat& covMat2)
{
	return sqrt(log(((covMat1 + covMat2)/2).Determinant()) - 0.5 * log((covMat1 * covMat2).Determinant()));
}
	
double Distance::RiemannianDistance(const CovMat& covMat1, const CovMat& covMat2)
{
	cx_vec eigenValues = eig_gen(inv_sympd(covMat1.matrix)*covMat2.matrix);	

	vec tmp(covMat1.matrixOrder);

	for (unsigned int i = 0; i < covMat1.matrixOrder; i++)
	{
		tmp(i) = log(real(eigenValues(i)));
		tmp(i) *= tmp(i);
	}

	return sqrt(sum(tmp));
}