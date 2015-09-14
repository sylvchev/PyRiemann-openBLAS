#include <iostream>
#include <Eigen>
#include "Mean.hpp"
#include "CovMat.hpp"

using namespace std;
using namespace Eigen;  

CovMat Mean::EuclideanMean (const vector<CovMat>& covMats)
{
	CovMat covMatResult();

	for (CovMat covMat : covMats)
		covMatResult += covMat;

	covMatResult /= covMats.size();

	return covMatResult;
}
