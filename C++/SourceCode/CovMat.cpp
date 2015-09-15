#include <iostream>
#include <eigen3/Eigen/Dense>
#include "CovMat.hpp" 

using namespace std;
using namespace Eigen;

void CovMat::ConstructorInitialize()
{
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
	delete this->inverse;
	delete this->sqrtm;
	delete this->invsqrtm;
	delete this->expm;
	delete this->logm;
	delete this->powm;
}

void CovMat::Copy(const CovMat& covMat)
{
	this->eigenMatrix = covMat.eigenMatrix;
	this->matrixOrder = covMat.matrixOrder;
	this->b_eigenValues = covMat.b_eigenValues;
	this->b_eigenVectors = covMat.b_eigenVectors;
	this->eigenSolver = covMat.eigenSolver;
	this->norm = covMat.norm;
	this->b_norm = covMat.b_norm;
	this->determinant = covMat.determinant;
	this->b_determinant = covMat.b_determinant;

	this->inverse = NULL;
	if (covMat.inverse != NULL)
		this->inverse = new CovMat(*(covMat.inverse));

	this->sqrtm = NULL;
	if (covMat.sqrtm != NULL)
		this->sqrtm = new CovMat(*(covMat.sqrtm));

	this->invsqrtm = NULL;
	if (covMat.invsqrtm != NULL)
		this->invsqrtm = new CovMat(*(covMat.invsqrtm));

	this->expm = NULL;
	if (covMat.expm != NULL)
		this->expm = new CovMat(*(covMat.expm));

	this->logm = NULL;
	if (covMat.logm != NULL)
		this->logm = new CovMat(*(covMat.logm));

	this->currentPower = covMat.currentPower;
	this->powm = NULL;
	if (covMat.powm != NULL)
		this->powm = new CovMat(*(covMat.powm));
}

CovMat::CovMat(double* array, const unsigned matrixOrder)
{
	this->eigenMatrix = Map<MatrixXd, Aligned> (array, matrixOrder, matrixOrder);
	this->matrixOrder = matrixOrder;

	this->ConstructorInitialize();
}


CovMat::CovMat(const MatrixXd eigenMatrix)
{
	this->eigenMatrix = eigenMatrix;
	this->matrixOrder = eigenMatrix.cols();

	this->ConstructorInitialize();
}

CovMat::CovMat(const unsigned int matrixOrder)
{
	this->eigenMatrix = MatrixXd::Zero(matrixOrder, matrixOrder);
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

void CovMat::SetToZero()
{
	this->eigenMatrix.setZero();

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();
}

void CovMat::Randomize()
{
	MatrixXd tmp = MatrixXd::Random(this->matrixOrder, 2 * this->matrixOrder);
	this->eigenMatrix = tmp * tmp.transpose();

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();
}

double CovMat::Norm()
{
	if (this->b_norm)
		return this->norm;

	this->norm = this->eigenMatrix.norm();
	this->b_norm = true;

	return this->b_norm;
}

double CovMat::Determinant()
{
	if (this->b_determinant)
		return this->determinant;

	this->determinant = this->eigenMatrix.determinant();
	this->b_determinant = true;

	return this->determinant;
}

CovMat CovMat::Transpose()
{
	return *this;
}

CovMat CovMat::Inverse()
{
	if (this->inverse != NULL)
		return *(this->inverse);

	this->inverse = new CovMat(this->eigenMatrix.inverse());

	return *(this->inverse);
}

void CovMat::ComputeEigen(bool eigenValuesOnly)
{
	if ((this->b_eigenValues)&&(this->b_eigenVectors))
		return;
	
	if ((this->b_eigenValues)&&(eigenValuesOnly))
		return;

	if (eigenValuesOnly)
	{
		this->eigenSolver.compute(this->eigenMatrix, EigenvaluesOnly);
		this->b_eigenValues = true;
		return;
	}

	this->eigenSolver.compute(this->eigenMatrix);
	this->b_eigenValues = true;
	this->b_eigenVectors = true;
}

CovMat CovMat::Sqrtm()
{
	if (this->sqrtm != NULL)
		return *(this->sqrtm);

	this->ComputeEigen();

	VectorXd tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = sqrt(this->eigenSolver.eigenvalues()(i));

	this->sqrtm = new CovMat(this->eigenSolver.eigenvectors() * tmp.asDiagonal() * this->eigenSolver.eigenvectors().transpose());

	return *(this->sqrtm);
}

CovMat CovMat::Invsqrtm()
{
	if (this->invsqrtm != NULL)
		return *(this->invsqrtm);

	this->ComputeEigen();

	VectorXd tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = 1/sqrt(this->eigenSolver.eigenvalues()(i));

	this->invsqrtm = new CovMat(this->eigenSolver.eigenvectors() * tmp.asDiagonal() * this->eigenSolver.eigenvectors().transpose());

	return *(this->invsqrtm);
}

CovMat CovMat::Expm()
{
	if (this->expm != NULL)
		return *(this->expm);

	this->ComputeEigen();

	VectorXd tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = exp(this->eigenSolver.eigenvalues()(i));

	this->expm = new CovMat(this->eigenSolver.eigenvectors() * tmp.asDiagonal() * this->eigenSolver.eigenvectors().transpose());

	return *(this->expm);
}

CovMat CovMat::Logm()
{
	if (this->logm != NULL)
		return *(this->logm);

	this->ComputeEigen();

	VectorXd tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = log(this->eigenSolver.eigenvalues()(i));

	this->logm = new CovMat(this->eigenSolver.eigenvectors() * tmp.asDiagonal() * this->eigenSolver.eigenvectors().transpose());

	return *(this->logm);
}

CovMat CovMat::Powm(const double power)
{
	if (power == 1)
		return *this;

	if (power == this->currentPower)
		return *(this->powm);

	delete this->powm;

	this->ComputeEigen();

	VectorXd tmp(this->matrixOrder);
	for (unsigned int i = 0; i < this->matrixOrder; i++)
		tmp(i) = pow(this->eigenSolver.eigenvalues()(i), power);

	this->powm = new CovMat(this->eigenSolver.eigenvectors() * tmp.asDiagonal() * this->eigenSolver.eigenvectors().transpose());
	this->currentPower = power;

	return *(this->powm);
}

ostream& operator << (ostream &output, const CovMat& covMat)
{ 
    output << covMat.eigenMatrix;
    return output;            
}

double CovMat::operator () (const int nCol, const int nRow)
{
	return this->eigenMatrix(nCol, nRow);
}

CovMat& CovMat::operator = (const CovMat& covMat)
{
	this->DeleteAllocatedVar();
	this->Copy(covMat);

	return *this;
}

CovMat operator + (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(covMat1.eigenMatrix + covMat2.eigenMatrix);
}

CovMat operator - (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(covMat1.eigenMatrix - covMat2.eigenMatrix);
}

CovMat operator * (const double mul, const CovMat& covMat)
{
	return CovMat(mul * covMat.eigenMatrix);
}

CovMat operator * (const CovMat& covMat, const double mul)
{
	return CovMat(mul * covMat.eigenMatrix);
}

CovMat operator * (const CovMat& covMat1, const CovMat& covMat2)
{
	return CovMat(covMat1.eigenMatrix * covMat2.eigenMatrix);
}

CovMat operator / (const CovMat& covMat, const double div)
{
	return CovMat(covMat.eigenMatrix / div);
}

CovMat& CovMat::operator += (const CovMat& covMat)
{
	this->eigenMatrix += covMat.eigenMatrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator -= (const CovMat& covMat)
{
	this->eigenMatrix -= covMat.eigenMatrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator *= (const double mul)
{
	this->eigenMatrix *= mul;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator *= (const CovMat& covMat)
{
	this->eigenMatrix *= covMat.eigenMatrix;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}

CovMat& CovMat::operator /= (const double mul)
{
	this->eigenMatrix /= mul;

	this->DeleteAllocatedVar();
	this->ConstructorInitialize();

	return *this;
}