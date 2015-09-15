#include <iostream>
#include <eigen3/Eigen/Dense>
#include "Distance.hpp"
#include "CovMat.hpp"

using namespace std;
using namespace Eigen; 

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
	GeneralizedSelfAdjointEigenSolver<MatrixXd> gsaes(covMat1.eigenMatrix, covMat2.eigenMatrix, EigenvaluesOnly);

	VectorXd eigenvalues = gsaes.eigenvalues();

	for (unsigned int i = 0; i < covMat1.matrixOrder; i++)
	{
		eigenvalues(i) = log(eigenvalues(i));
		eigenvalues(i) *= eigenvalues(i);
	}

	return sqrt(eigenvalues.sum());
}