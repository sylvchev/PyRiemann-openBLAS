#ifndef ABSREALMAT
#define ABSREALMAT

#include <iostream>
#include <Eigen>
#include "AbsMat.hpp"

using namespace std;
using namespace Eigen;

class AbsRealMat : public AbsMat
{
	protected:

	public:
		//Fields
		MatrixXd matrix;

		//Virtual destructors for polymorphism
		virtual ~AbsRealMat() {}

		//Methods
		double Norm();

		//<< operator overload
		friend ostream& operator << (ostream &output, const AbsRealMat& absRealMat);
};

#endif