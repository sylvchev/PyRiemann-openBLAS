#include <iostream>
#include <limits>
#include <Eigen>
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

	for (CovMat covMat : covMats)
		covMatResult += covMat;

	covMatResult /= covMats.size();

	return covMatResult;
}

CovMat Mean::LogEuclideanMean (const vector<CovMat>& covMats)
{
	CovMat covMatResult(covMats[0].matrixOrder);

	for (CovMat covMat : covMats)
		covMatResult += covMat.Logm();

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

		for (CovMat covMat : covMats)
			covMatTmp += (0.5 * (covMat + covMatResult)).Inverse();

		covMatTmp /= covMats.size();

		CovMat covMatResultNew = covMatTmp.Inverse();
		crit = (covMatResultNew - covMatResult).Norm();

		covMatResult = covMatResultNew;
	}

	if (k == maxIter)
		cout << "Max iter reach" << endl;

	return covMatResult;
}


CovMat Mean::RiemmanianMean (const vector<CovMat>& covMats, const double tol, const unsigned int maxIter, CovMat* covMatInit)
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

		CovMat covMatResultSqrtm = covMatResult.Sqrtm();
		CovMat covMatResultInvsqrtm = covMatResult.Invsqrtm();

		covMatTmp.SetToZero();

		for (CovMat covMat : covMats)
			covMatTmp += (covMatResultInvsqrtm * covMat * covMatResultInvsqrtm).Logm();

		covMatTmp /= covMats.size();

		crit = covMatTmp.Norm();
		const double h = nu * crit;

		covMatResult = covMatResultSqrtm * (nu * covMatTmp).Expm() * covMatResultSqrtm;

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
