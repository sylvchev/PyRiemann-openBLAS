#ifndef ABSREALNONSYMMAT
#define ABSREALNONSYMMAT

#include <Eigen>
#include "AbsRealSqMat.hpp" 

using namespace Eigen;

class AbsRealNonSymMat : public AbsRealSqMat
{
	protected:
		VectorXcd eigenValues;
		MatrixXcd eigenVectors;
		void ComputeEigen(bool eigenValuesOnly = false);

	public:
		//Virtual destructors for polymorphism
		virtual ~AbsRealNonSymMat() {}
};

#endif