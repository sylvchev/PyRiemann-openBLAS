#include <iostream>
#include <limits>
#include <armadillo>
#include "Mean.hpp"
#include "CovMat.hpp"

using namespace std;
using namespace arma;  

CovMat Mean::IdentityMean (const vector<CovMat>& covMats)
{
	unsigned int matrixOrder = covMats[0].matrixOrder;

	return CovMat(eye<mat>(matrixOrder, matrixOrder));
}

CovMat Mean::EuclideanMean (const vector<CovMat>& covMats)
{
	CovMat covMatResult(covMats[0].matrixOrder);

	for (unsigned int i = 0; i < covMats.size(); i++)
		covMatResult += covMats[i];

	covMatResult /= covMats.size();

	return covMatResult;
}

CovMat Mean::LogEuclideanMean (vector<CovMat>& covMats)
{
	CovMat covMatResult(covMats[0].matrixOrder);

	for (unsigned int i = 0; i < covMats.size(); i++)
		covMatResult += covMats[i].Logm();

	covMatResult /= covMats.size();

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

	while ((crit > tol) && (k < maxIter))
	{
		k++;

		covMatTmp.SetToZero();

		for (unsigned int i = 0; i < covMats.size(); i++)
			covMatTmp += (0.5 * (covMats[i] + covMatResult)).Inverse();

		covMatTmp /= covMats.size();

		crit = (covMatTmp.Inverse() - covMatResult).Norm();

		covMatResult = covMatTmp.Inverse();
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

	while ((crit > tol)&&(k < maxIter)&&(nu > tol))
	{
		k++;

		covMatTmp.SetToZero();

		for (unsigned int i = 0; i < covMats.size(); i++)
			covMatTmp += (covMatResult.Invsqrtm() * covMats[i] * covMatResult.Invsqrtm()).Logm();

		covMatTmp /= covMats.size();

		crit = covMatTmp.Norm();
		const double h = nu * crit;

		covMatResult = covMatResult.Sqrtm() * (nu * covMatTmp).Expm() * covMatResult.Sqrtm();

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
