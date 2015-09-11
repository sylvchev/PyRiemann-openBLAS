#ifndef ABSREALSYMMAT
#define ABSREALSYMMAT

#include <Eigen>
#include "AbsRealSqMat.hpp"
class RealSymPosDefMat; //#include "../Class/RealSymPosDefMat.hpp"

using namespace Eigen;

class AbsRealSymMat : public AbsRealSqMat
{
	protected:
		VectorXd eigenvalues;
		MatrixXd eigenvectors;

	public:
		void ComputeEigen(bool eigenvaluesOnly = false);
		RealSymPosDefMat Expm();

		//Virtual destructors for polymorphism
		virtual ~AbsRealSymMat() {}
};

#endif