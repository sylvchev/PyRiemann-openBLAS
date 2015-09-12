#ifndef REALSYMREGMAT
#define REALSYMREGMAT

#include <Eigen>
#include "../AbstractClass/AbsRealSymMat.hpp"

using namespace Eigen;

class RealSymRegMat : public AbsRealSymMat
{
	private:
		RealSymRegMat* powm;

	public:
		RealSymRegMat(double* array, unsigned int matrixOrder);
		RealSymRegMat(MatrixXd matrix);
		~RealSymRegMat();

		//RealSymRegMat Powm(double power);
};

#endif