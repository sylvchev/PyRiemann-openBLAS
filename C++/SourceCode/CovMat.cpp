#include <iostream>
#include <memory>
#include <armadillo>
#include "CovMat.hpp" 

using namespace std;
using namespace arma;

void CovMat::ConstructorInitialize()
{
	this->b_eigenValues = false;
	this->b_eigenVectors = false;
	this->b_norm = false;
	this->b_determinant = false;

	this->eigenValues = shared_ptr<vec> (new vec);
	this->eigenVectors = shared_ptr<mat> (new mat);
	this->inverse = nullptr;
	this->sqrtm = nullptr;
	this->invsqrtm = nullptr;
	this->expm = nullptr;
	this->logm = nullptr;
	this->powm = nullptr;
	this->currentPower = 1;
}

void CovMat::DeleteAllocatedVar()
{

}

void CovMat::Copy(const CovMat& covMat)
{
	this->matrix = covMat.matrix;
	this->matrixOrder = covMat.matrixOrder;
	this->b_eigenValues = covMat.b_eigenValues; this->eigenValues = covMat.eigenValues;
	this->b_eigenVectors = covMat.b_eigenVectors; this->eigenVectors = covMat.eigenVectors; this->eigenVectorsTranspose = covMat.eigenVectorsTranspose;
	this->b_norm = covMat.b_norm; this->norm = covMat.norm;
	this->b_determinant = covMat.b_determinant; this->determinant = covMat.determinant;

	this->inverse = covMat.inverse;
	this->sqrtm = covMat.sqrtm;
	this->invsqrtm = covMat.invsqrtm;
	this->expm = covMat.expm;
	this->logm = covMat.logm;
	this->currentPower = covMat.currentPower; this->powm = covMat.powm;
}

CovMat::CovMat(double* array, const unsigned matrixOrder)
{
	this->matrix = shared_ptr<mat> (new mat(array, matrixOrder, matrixOrder, false, true));
	this->matrixOrder = matrixOrder;
	this->ConstructorInitialize();
}

CovMat::CovMat(const mat& matrix)
{
	this->matrix = make_shared<mat> (matrix);
	this->matrixOrder = matrix.n_cols;
	this->ConstructorInitialize();
}

CovMat::CovMat(const unsigned int matrixOrder)
{
	this->matrix = shared_ptr<mat> (new mat(matrixOrder, matrixOrder));
	this->matrix->zeros();
	this->matrixOrder = matrixOrder;
	this->ConstructorInitialize();
}

CovMat::CovMat(const CovMat& covMat)
{
	this->Copy(covMat);
}

CovMat::CovMat()
{
	this->ConstructorInitialize();
}

CovMat::~CovMat()
{
	this->DeleteAllocatedVar();
}

void CovMat::ComputeEigen(bool eigenValuesOnly)
{
	if ((this->b_eigenValues)&&(this->b_eigenVectors))
		return;
	
	if ((this->b_eigenValues)&&(eigenValuesOnly))
		return;

	if (eigenValuesOnly)
	{
		*this->eigenValues = eig_sym(*this->matrix);
		this->b_eigenValues = true;
		return;
	}

	eig_sym(*this->eigenValues, *this->eigenVectors, *this->matrix);
	this->eigenVectorsTranspose = make_shared<mat> (this->eigenVectors->t());
	this->b_eigenValues = true;
	this->b_eigenVectors = true;
}

void CovMat::SetToZero()
{
	this->matrix->zeros();
	this->DeleteAllocatedVar();
	this->ConstructorInitialize();
}

void CovMat::Randomize()
{
	mat tmp(this->matrixOrder, 2*this->matrixOrder);
	tmp.randu();
	*this->matrix = tmp * tmp.t();
	this->DeleteAllocatedVar();
	this->ConstructorInitialize();
}

double CovMat::Norm()
{
	if (this->b_norm)
		return this->norm;

	this->norm = arma::norm(*this->matrix, "fro");
	this->b_norm = true; 

	return this->norm;
}

double CovMat::Determinant()
{
	if (this->b_determinant)
		return this->determinant;

	this->determinant = det(*this->matrix);
	this->b_determinant = true;

	return this->determinant;
}

CovMat& CovMat::Transpose()
{
	return *this;
}

CovMat& CovMat::Inverse()
{
	if (this->inverse != nullptr)
		return *(this->inverse);

	this->inverse = shared_ptr<CovMat> (new CovMat(inv_sympd(*this->matrix)));

	return *(this->inverse);
}

CovMat& CovMat::Sqrtm()
{
	if (this->sqrtm != nullptr)
		return *(this->sqrtm);

	this->ComputeEigen();
	
	this->sqrtm = shared_ptr<CovMat> (new CovMat(*this->eigenVectors * diagmat(sqrt(*this->eigenValues)) * *this->eigenVectorsTranspose));

	return *(this->sqrtm);
}

CovMat& CovMat::Invsqrtm()
{
	if (this->invsqrtm != nullptr)
		return *(this->invsqrtm);

	this->ComputeEigen();

	this->invsqrtm = shared_ptr<CovMat> (new CovMat(*this->eigenVectors * diagmat(pow(*this->eigenValues, -0.5)) * *this->eigenVectorsTranspose));

	return *(this->invsqrtm);
}

CovMat& CovMat::Expm()
{
	if (this->expm != nullptr)
		return *(this->expm);

	this->ComputeEigen();

	this->expm = shared_ptr<CovMat> (new CovMat(*this->eigenVectors * diagmat(exp(*this->eigenValues)) * *this->eigenVectorsTranspose));

	return *(this->expm);
}

CovMat& CovMat::Logm()
{
	if (this->logm != nullptr)
		return *(this->logm);

	this->ComputeEigen();

	this->logm = shared_ptr<CovMat> (new CovMat(*this->eigenVectors * diagmat(log(*this->eigenValues)) * *this->eigenVectorsTranspose));

	return *(this->logm);
}

CovMat& CovMat::Powm(const double power)
{
	if (power == 1)
		return *this;

	if (power == this->currentPower)
		return *(this->powm);

	this->ComputeEigen();

	this->powm = shared_ptr<CovMat> (new CovMat(*this->eigenVectors * diagmat(pow(*this->eigenValues, power)) * *this->eigenVectorsTranspose));
	this->currentPower = power;

	return *(this->powm);
}

ostream& operator << (ostream &output, const CovMat& covMat)
{ 
    output << *covMat.matrix;
    return output;            
}

double CovMat::operator () (const int nCol, const int nRow)
{
	return (*this->matrix)(nCol, nRow);
}

CovMat& CovMat::operator = (const CovMat& covMat)
{
	this->DeleteAllocatedVar();
	this->Copy(covMat);

	return *this;
}

CovMat operator + (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(*covMat1.matrix + *covMat2.matrix);
}

CovMat operator - (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(*covMat1.matrix - *covMat2.matrix);
}

CovMat operator * (const double mul, const CovMat& covMat)
{
	return CovMat(mul * *covMat.matrix);
}

CovMat operator * (const CovMat& covMat, const double mul)
{
	return CovMat(mul * *covMat.matrix);
}

CovMat operator * (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(*covMat1.matrix * *covMat2.matrix);
}

CovMat operator / (const CovMat& covMat, const double div)
{
	return CovMat(*covMat.matrix / div);
}

CovMat& CovMat::operator += (const CovMat& covMat)
{
	*this->matrix += *covMat.matrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator -= (const CovMat& covMat)
{
	*this->matrix -= *covMat.matrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator *= (const double mul)
{
	*this->matrix *= mul;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator *= (const CovMat& covMat)
{
	*this->matrix *= *covMat.matrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator /= (const double mul)
{
	*this->matrix /= mul;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}
