#ifndef ABSREALSQMAT
#define ABSREALSQMAT

#include "AbsRealMat.hpp"

class AbsRealSqMat : public AbsRealMat
{
	protected:
		bool b_eigenValues;
		bool b_eigenVectors;

	public:
		//Methods
		double Determinant();

		//Virtual destructors for polymorphism
		virtual ~AbsRealSqMat() {}
};

#endif