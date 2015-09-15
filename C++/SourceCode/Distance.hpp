#ifndef DISTANCE_HPP
#define DISTANCE_HPP

#include <iostream>
#include <eigen3/Eigen/Dense>
#include "CovMat.hpp"

using namespace std;
using namespace Eigen;

class Distance
{
	private:

	public:
		static double EuclideanDistance(const CovMat& covMat1, const CovMat& covMat2);
		static double LogEuclideanDistance(CovMat& covMat1, CovMat& covMat2);
		static double LogDeterminantDistance(const CovMat& covMat1, const CovMat& covMat2);
		static double RiemannianDistance(const CovMat& covMat1, const CovMat& covMat2);

};

#endif 
