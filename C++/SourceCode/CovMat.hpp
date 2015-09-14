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
		SelfAdjointEigenSolver<MatrixXd> eigenSolver;
		CovMat* sqrtm;
		CovMat* invsqrtm;
		CovMat* expm;
		CovMat* logm;
		CovMat* powm; double currentPower;

		//Methods
		void ComputeEigen(bool eigenValuesOnly = false);

	public:
		//Fields

		//Constructors
		CovMat(double* array, unsigned matrixOrder);
		CovMat(const MatrixXd eigenMatrix);

		//Destructors
		~CovMat();

		//Methods
		double Norm() const;
		double Determinant() const;
		CovMat Sqrtm();
		CovMat Invsqrtm();
		CovMat Expm();
		CovMat Logm();
		CovMat Powm(double power);

		//<< operator overload
		friend ostream& operator << (ostream &output, const CovMat& covMat);

		//<< operator overload
		double operator () (const int nCol, const int nRow);
};

#endif
