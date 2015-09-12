#ifndef ABSREALSQMAT
#define ABSREALSQMAT

#include "AbsRealMat.hpp"

class AbsRealSqMat : public AbsRealMat
{
	protected:
		bool b_eigenValues;
		bool b_eigenVectors;
		AbsRealMat* expm;
		AbsRealMat* powm;

	public:
		//Methods
		double Determinant();
		virtual void ComputeEigen(bool eigenValuesOnly = false) = 0;

		//Virtual destructors for polymorphism
		virtual ~AbsRealSqMat() {}
};

#endif