#ifndef ABSREALSQMAT
#define ABSREALSQMAT

#include "AbsRealMat.hpp"

class AbsRealSqMat : public AbsRealMat
{
	protected:
		bool b_eigenvalues;
		bool b_eigenvectors;
		AbsRealSqMat* expm;
		AbsRealSqMat* powm;

	public:
		//Methods
		double Determinant();

		//Virtual destructors for polymorphism
		virtual ~AbsRealSqMat() {}
};

#endif