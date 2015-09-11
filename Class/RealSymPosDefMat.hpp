#ifndef REALSYMPOSDEFMAT
#define REALSYMPOSDEFMAT

#include <Eigen>
#include "../AbstractClass/AbsRealSymMat.hpp"
#include "RealSymRegMat.hpp"

using namespace Eigen;

class RealSymPosDefMat : public AbsRealSymMat
{
	private:
		RealSymPosDefMat* sqrtm;
		RealSymPosDefMat* invsqrtm;
		RealSymRegMat* logm;

	public:
		RealSymPosDefMat(double* array, unsigned int matrixOrder);
		RealSymPosDefMat(MatrixXd matrix);
		~RealSymPosDefMat();

		RealSymPosDefMat Powm(double power);
};

#endif
