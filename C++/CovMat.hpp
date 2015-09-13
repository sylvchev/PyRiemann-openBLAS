#ifndef COVMAT_HPP
#define COVMAT_HPP

#include <iostream>
#include <Eigen>

using namespace std;
using namespace Eigen;

class CovMat
{
	private:
		//Fields
		MatrixXd eigenMatrix;
		unsigned int matrixOrder;
		bool b_eigenValues;
		bool b_eigenVectors;
		SelfAdjointEigenSolver<MatrixXd> es;
		CovMat* sqrtm;
		CovMat* invsqrtm;
		CovMat* expm;
		CovMat* logm;

		//Methods
		void ComputeEigen(bool eigenValuesOnly = false);

	public:
		//Fields

		//Constructors
		CovMat(double* array, unsigned matrixOrder);
		CovMat(const MatrixXd& eigenMatrix);

		//Destructors
		~CovMat();

		//Methods
		CovMat& Sqrtm();
		CovMat& Invsqrtm();
		CovMat& Expm();
		CovMat& Logm();

		//<< operator overload
		friend ostream& operator << (ostream &output, const CovMat& covMat);
};

#endif
