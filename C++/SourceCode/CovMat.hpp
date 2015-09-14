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
		MatrixXd eigenMatrix;
		unsigned int matrixOrder;

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

		//<< operators overload
		friend ostream& operator << (ostream &output, const CovMat& covMat);
		double operator () (const int nCol, const int nRow);
		friend CovMat operator + (const CovMat& covMat1, const CovMat& covMat2);
		friend CovMat operator - (const CovMat& covMat1, const CovMat& covMat2);
		friend CovMat operator * (const double mul, const CovMat& covMat);
		friend CovMat operator * (const CovMat& covMat, const double mul);
		friend CovMat operator * (const CovMat& covMat1, const CovMat& covMat2);
		friend CovMat operator / (const CovMat& covMat, const double div);
};

#endif
