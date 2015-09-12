#ifndef ABSREALSYMMAT
#define ABSREALSYMMAT

#include <Eigen>
#include "AbsRealSqMat.hpp"
class RealSymPosDefMat; //#include "../Class/RealSymPosDefMat.hpp"

using namespace Eigen;

class AbsRealSymMat : public AbsRealSqMat
{
	protected:
		VectorXd eigenValues;
		MatrixXd eigenVectors;		
		RealSymPosDefMat* expm;

	public:
		void ComputeEigen(bool eigenValuesOnly = false);
		RealSymPosDefMat& Expm();

		//Virtual destructors for polymorphism
		virtual ~AbsRealSymMat() {}
};

#endif