#ifndef MEAN_HPP
#define MEAN_HPP

#include <iostream>
#include <vector>
#include <Eigen>
#include "CovMat.hpp"

using namespace std;
using namespace Eigen;

class Mean
{
	private:

	public:
		static CovMat EuclideanMean (const vector<CovMat>& covMats);
};
 
#endif 
