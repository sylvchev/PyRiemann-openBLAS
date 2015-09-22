#ifndef COVMAT_HPP
#define COVMAT_HPP

#include <iostream>
#include <memory>
#include <armadillo>

using namespace std;
using namespace arma;

class CovMat
{
	private:
		//Fields
		shared_ptr<vec> eigenValues; bool b_eigenValues;
		shared_ptr<mat> eigenVectors; shared_ptr<mat> eigenVectorsTranspose; bool b_eigenVectors;
		double norm; bool b_norm;
		double determinant; bool b_determinant;
		shared_ptr<CovMat> inverse;
		shared_ptr<CovMat> sqrtm;
		shared_ptr<CovMat> invsqrtm;
		shared_ptr<CovMat> expm;
		shared_ptr<CovMat> logm;
		shared_ptr<CovMat> powm; double currentPower;

		//Methods
		void Copy(const CovMat& covMat);
		void ComputeEigen(bool eigenValuesOnly = false);

	public:
		//Fields		
		shared_ptr<mat> matrix;
		unsigned int matrixOrder;

		//Constructors
		CovMat(double* array, const unsigned matrixOrder);
		CovMat(const mat& matrix);
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
