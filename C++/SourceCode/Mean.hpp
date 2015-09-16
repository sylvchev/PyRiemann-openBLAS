#ifndef MEAN_HPP
#define MEAN_HPP

#include <iostream>
#include <vector>
#include <armadillo>
#include "CovMat.hpp"

using namespace std;
using namespace arma;

class Mean
{
	private:

	public:
		static CovMat IdentityMean (const vector<CovMat>& covMats);
		static CovMat EuclideanMean (const vector<CovMat>& covMats);
		static CovMat LogEuclideanMean (vector<CovMat>& covMats);
		static CovMat LogDeterminantMean (const vector<CovMat>& covMats, const double tol = 10e-5, const unsigned int maxIter = 50, CovMat* covMatInit = NULL);
		static CovMat RiemannianMean (const vector<CovMat>& covMats, const double tol = 10e-9, const unsigned int maxIter = 50, CovMat* covMatInit = NULL);
};
 
#endif 
