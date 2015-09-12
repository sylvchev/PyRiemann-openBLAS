#include <Eigen>
#include "AbsRealSqMat.hpp"

using namespace Eigen;

double AbsRealSqMat::Determinant ()
{
	return this->eigenMatrix.determinant();
} 
