#include <iostream>
#include <limits>
#include <eigen3/Eigen/Dense>
#include "Mean.hpp"
#include "CovMat.hpp"

using namespace std;
using namespace Eigen;  

CovMat Mean::IdentityMean (const vector<CovMat>& covMats)
{
	unsigned int matrixOrder = covMats[0].matrixOrder;

	return CovMat(MatrixXd::Identity(matrixOrder, matrixOrder));
}

CovMat Mean::EuclideanMean (const vector<CovMat>& covMats)
{
	CovMat covMatResult(covMats[0].matrixOrder);

	for (unsigned int i = 0; i < covMats.size(); i++)
		covMatResult.eigenMatrix += covMats[i].eigenMatrix;

	covMatResult.eigenMatrix /= covMats.size();

	return covMatResult;
}

CovMat Mean::LogEuclideanMean (vector<CovMat>& covMats)
{
	CovMat covMatResult(covMats[0].matrixOrder);

	for (unsigned int i = 0; i < covMats.size(); i++)
		covMatResult.eigenMatrix += covMats[i].Logm().eigenMatrix;

	covMatResult.eigenMatrix /= covMats.size();

	return covMatResult.Expm();
}

CovMat Mean::LogDeterminantMean (const vector<CovMat>& covMats, const double tol, const unsigned int maxIter, CovMat* covMatInit)
{
	CovMat covMatResult;

	if (covMatInit == NULL)
		covMatResult = Mean::EuclideanMean(covMats);
	else
		covMatResult = *covMatInit;

	unsigned int k = 0;
	double crit = numeric_limits<double>::max();
	CovMat covMatTmp(covMats[0].matrixOrder);
	CovMat covMatResultNew;

	while ((crit > tol) && (k < maxIter))
	{
		k++;

		covMatTmp.SetToZero();

		for (unsigned int i = 0; i < covMats.size(); i++)
			covMatTmp.eigenMatrix += (0.5 * (covMats[i].eigenMatrix + covMatResult.eigenMatrix)).inverse();

		covMatTmp.eigenMatrix /= covMats.size();

		covMatResultNew = covMatTmp.Inverse();
		crit = (covMatResultNew - covMatResult).Norm();

		covMatResult = covMatResultNew;
	}

	if (k == maxIter)
		cout << "Max iter reach" << endl;

	return covMatResult;
}


CovMat Mean::RiemannianMean (const vector<CovMat>& covMats, const double tol, const unsigned int maxIter, CovMat* covMatInit)
{
	CovMat covMatResult;

	if (covMatInit == NULL)
		covMatResult = Mean::EuclideanMean(covMats);
	else
		covMatResult = *covMatInit;

	unsigned int k = 0;
	double nu = 1.0;
	double tau = numeric_limits<double>::max();
	double crit = numeric_limits<double>::max();
	CovMat covMatTmp(covMats[0].matrixOrder);
	CovMat covMatResultSqrtm;
	CovMat covMatResultInvsqrtm;

	MatrixXd m(covMats[0].matrixOrder, covMats[0].matrixOrder);
	CovMat c(covMats[0].matrixOrder);

	while ((crit > tol)&&(k < maxIter)&&(nu > tol))
	{
		k++;

		covMatResultSqrtm = covMatResult.Sqrtm();
		covMatResultInvsqrtm = covMatResult.Invsqrtm();

		covMatTmp.SetToZero();

		for (unsigned int i = 0; i < covMats.size(); i++)
		{			
			m.noalias() = covMatResultInvsqrtm.eigenMatrix * covMats[i].eigenMatrix;
			c.eigenMatrix.noalias() = m * covMatResultInvsqrtm.eigenMatrix;
			c.DeleteAllocatedVar();
			c.ConstructorInitialize();
			covMatTmp += c.Logm();
		}

		covMatTmp.eigenMatrix /= covMats.size();

		crit = covMatTmp.Norm();
		const double h = nu * crit;

		m.noalias() = covMatResultSqrtm.eigenMatrix * (nu * covMatTmp).Expm().eigenMatrix;
		covMatResult.DeleteAllocatedVar();
		covMatResult.ConstructorInitialize();
		covMatResult.eigenMatrix.noalias() = m * covMatResultSqrtm.eigenMatrix;

		if (h < tau)
		{
			nu *= 0.95;
			tau = h;
		}
		else
			nu *= 0.5;
	}

	return covMatResult;
}
