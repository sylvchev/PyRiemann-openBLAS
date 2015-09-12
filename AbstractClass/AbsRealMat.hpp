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
		//Fields
		MatrixXd eigenMatrix;

	public:
		//Methods
		double Norm();

		//<< operator overload
		friend ostream& operator << (ostream &output, const AbsRealMat& absRealMat);

		//Virtual destructors for polymorphism
		virtual ~AbsRealMat() {}
};

#endif