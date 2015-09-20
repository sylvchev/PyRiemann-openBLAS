#ifndef COVMAT_HPP
#define COVMAT_HPP

#include <iostream>
#include <armadillo>

using namespace std;
using namespace arma;

class CovMat
{
	private:
		//Fields
		vec vecEigenValues; mat matEigenValues; bool b_eigenValues;
		mat matEigenVectors; mat matEigenVectorsTranspose; bool b_eigenVectors;
		double norm; bool b_norm;
		double determinant; bool b_determinant;
		CovMat* inverse;
		CovMat* sqrtm;
		CovMat* invsqrtm;
		CovMat* expm;
		CovMat* logm;
		CovMat* powm; double currentPower;

		//Methods
		void Copy(const CovMat& covMat);
		void ComputeEigen(bool eigenValuesOnly = false);

	public:
		//Fields		
		mat matrix;
		unsigned int matrixOrder;

		//Constructors
		CovMat(double* array, const unsigned matrixOrder);
		CovMat(const mat matrix);
		CovMat(const unsigned int matrixOrder);
		CovMat(const CovMat& covMat);
		CovMat();

		//Destructors
		~CovMat();

		//Methods		
		void ConstructorInitialize();		
		void DeleteAllocatedVar();
		void Randomize();
		void SetToZero();
		double Norm();
		double Determinant();
		CovMat& Transpose();
		CovMat& Inverse();
		CovMat& Sqrtm();
		CovMat& Invsqrtm();
		CovMat& Expm();
		CovMat& Logm();
		CovMat& Powm(const double power);

		//<< operators overload
		friend ostream& operator << (ostream &output, const CovMat& covMat);
		double operator () (const int nCol, const int nRow);
		CovMat& operator = (const CovMat& covMat);
		friend CovMat operator + (const CovMat& covMat1, const CovMat& covMat2);
		friend CovMat operator - (const CovMat& covMat1, const CovMat& covMat2);
		friend CovMat operator * (const double mul, const CovMat& covMat);
		friend CovMat operator * (const CovMat& covMat, const double mul);
		friend CovMat operator * (const CovMat& covMat1, const CovMat& covMat2);
		friend CovMat operator / (const CovMat& covMat, const double div);
		CovMat& operator += (const CovMat& covMat);
		CovMat& operator -= (const CovMat& covMat);
		CovMat& operator *= (const double mul);
		CovMat& operator *= (const CovMat& covMat);
		CovMat& operator /= (const double div);
};

#endif
