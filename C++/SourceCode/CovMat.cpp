#include <iostream>
#include <armadillo>
#include "CovMat.hpp" 

using namespace std;
using namespace arma;

void CovMat::ConstructorInitialize()
{
	this->copy = false;
	this->b_eigenValues = false;
	this->b_eigenVectors = false;
	this->b_norm = false;
	this->b_determinant = false;

	this->inverse = NULL;
	this->sqrtm = NULL;
	this->invsqrtm = NULL;
	this->expm = NULL;
	this->logm = NULL;
	this->powm = NULL; this->currentPower = 1;
}

void CovMat::DeleteAllocatedVar()
{
	if (this->copy)
	{
		delete this->inverse;
		delete this->sqrtm;
		delete this->invsqrtm;
		delete this->expm;
		delete this->logm;
		delete this->powm;
	}
}

void CovMat::Copy(const CovMat& covMat)
{
	this->copy = true;
	this->matrix = covMat.matrix;
	this->matrixOrder = covMat.matrixOrder;
	this->b_eigenValues = covMat.b_eigenValues; this->vecEigenValues = covMat.vecEigenValues; this->matEigenValues = covMat.matEigenValues;
	this->b_eigenVectors = covMat.b_eigenVectors; this->matEigenVectors = covMat.matEigenVectors;
	this->norm = covMat.norm;
	this->b_norm = covMat.b_norm;
	this->determinant = covMat.determinant;
	this->b_determinant = covMat.b_determinant;

	this->inverse = covMat.inverse;
	this->sqrtm = covMat.sqrtm;
	this->invsqrtm = covMat.invsqrtm;
	this->expm = covMat.expm;
	this->logm = covMat.logm;
	this->powm = covMat.powm; this->currentPower = covMat.currentPower;
}

CovMat::CovMat(double* array, const unsigned matrixOrder)
{
	this->matrix = mat(array, matrixOrder, matrixOrder, false, true);
	this->matrixOrder = matrixOrder;
	this->ConstructorInitialize();
}

CovMat::CovMat(const mat matrix)
{
	this->matrix = matrix;
	this->matrixOrder = matrix.n_cols;
	this->ConstructorInitialize();
}

CovMat::CovMat(const unsigned int matrixOrder)
{
	this->matrix = mat(matrixOrder, matrixOrder);
	this->matrix.zeros();
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
		this->vecEigenValues = eig_sym(this->matrix);
		this->matEigenValues = diagmat(this->vecEigenValues);
		this->b_eigenValues = true;
		return;
	}

	eig_sym(this->vecEigenValues, this->matEigenVectors, this->matrix);
	this->matEigenValues = diagmat(this->vecEigenValues);
	this->matEigenVectorsTranspose = this->matEigenVectors.t();
	this->b_eigenValues = true;
	this->b_eigenVectors = true;
}

void CovMat::SetToZero()
{
	this->matrix.zeros();
	this->DeleteAllocatedVar();
	this->ConstructorInitialize();
}

void CovMat::Randomize()
{
	mat tmp(this->matrixOrder, 2*this->matrixOrder);
	tmp.randu();
	this->matrix = tmp * tmp.t();
	this->DeleteAllocatedVar();
	this->ConstructorInitialize();
}

double CovMat::Norm()
{
	if (this->b_norm)
		return this->norm;

	this->norm = arma::norm(this->matrix, "fro");
	this->b_norm = true; 

	return this->b_norm;
}

double CovMat::Determinant()
{
	if (this->b_determinant)
		return this->determinant;

	this->determinant = det(this->matrix);
	this->b_determinant = true;

	return this->determinant;
}

CovMat& CovMat::Transpose()
{
	return *this;
}

CovMat& CovMat::Inverse()
{
	if (this->inverse != NULL)
		return *(this->inverse);

	this->inverse = new CovMat(inv_sympd(this->matrix));

	return *(this->inverse);
}

CovMat& CovMat::Sqrtm()
{
	if (this->sqrtm != NULL)
		return *(this->sqrtm);

	this->ComputeEigen();

	vec tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = sqrt(this->vecEigenValues(i));

	this->sqrtm = new CovMat(this->matEigenVectors * diagmat(tmp) * this->matEigenVectorsTranspose);

	return *(this->sqrtm);
}

CovMat& CovMat::Invsqrtm()
{
	if (this->invsqrtm != NULL)
		return *(this->invsqrtm);

	this->ComputeEigen();

	vec tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = 1/sqrt(this->vecEigenValues(i));

	this->invsqrtm = new CovMat(this->matEigenVectors * diagmat(tmp) * this->matEigenVectorsTranspose);

	return *(this->invsqrtm);
}

CovMat& CovMat::Expm()
{
	if (this->expm != NULL)
		return *(this->expm);

	this->ComputeEigen();

	vec tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = exp(this->vecEigenValues(i));

	this->expm = new CovMat(this->matEigenVectors * diagmat(tmp) * this->matEigenVectorsTranspose);

	return *(this->expm);
}

CovMat& CovMat::Logm()
{
	if (this->logm != NULL)
		return *(this->logm);

	this->ComputeEigen();

	vec tmp(this->matrixOrder);

	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = log(this->vecEigenValues(i));

	this->logm = new CovMat(this->matEigenVectors * diagmat(tmp) * this->matEigenVectorsTranspose);

	return *(this->logm);
}

CovMat& CovMat::Powm(const double power)
{
	if (power == 1)
		return *this;

	if (power == this->currentPower)
		return *(this->powm);

	delete this->powm;

	this->ComputeEigen();

	vec tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = pow(this->vecEigenValues(i), power);

	this->powm = new CovMat(this->matEigenVectors * diagmat(tmp) * this->matEigenVectorsTranspose);
	this->currentPower = power;

	return *(this->powm);
}

ostream& operator << (ostream &output, const CovMat& covMat)
{ 
    output << covMat.matrix;
    return output;            
}

double CovMat::operator () (const int nCol, const int nRow)
{
	return this->matrix(nCol, nRow);
}

CovMat& CovMat::operator = (const CovMat& covMat)
{
	this->DeleteAllocatedVar();
	this->Copy(covMat);

	return *this;
}

CovMat operator + (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(covMat1.matrix + covMat2.matrix);
}

CovMat operator - (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(covMat1.matrix - covMat2.matrix);
}

CovMat operator * (const double mul, const CovMat& covMat)
{
	return CovMat(mul * covMat.matrix);
}

CovMat operator * (const CovMat& covMat, const double mul)
{
	return CovMat(mul * covMat.matrix);
}

CovMat operator * (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(covMat1.matrix * covMat2.matrix);
}

CovMat operator / (const CovMat& covMat, const double div)
{
	return CovMat(covMat.matrix / div);
}

CovMat& CovMat::operator += (const CovMat& covMat)
{
	this->matrix += covMat.matrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator -= (const CovMat& covMat)
{
	this->matrix -= covMat.matrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator *= (const double mul)
{
	this->matrix *= mul;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator *= (const CovMat& covMat)
{
	this->matrix *= covMat.matrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator /= (const double mul)
{
	this->matrix /= mul;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}
