#include <iostream>
#include <Eigen>
#include "CovMat.hpp" 

using namespace std;
using namespace Eigen;

CovMat::CovMat(double* array, unsigned matrixOrder)
{
	this->eigenMatrix = Map<MatrixXd, Aligned> (array, matrixOrder, matrixOrder);
	this->matrixOrder = matrixOrder;

	this->b_eigenValues = false;
	this->b_eigenVectors = false;

	this->sqrtm = NULL;
	this->invsqrtm = NULL;
	this->expm = NULL;
	this->logm = NULL;

	this->currentPower = 1;
	this->powm = NULL;
}


CovMat::CovMat(const MatrixXd eigenMatrix)
{
	this->eigenMatrix = eigenMatrix;
	this->matrixOrder = eigenMatrix.cols();

	this->b_eigenValues = false;
	this->b_eigenVectors = false;

	this->sqrtm = NULL;
	this->invsqrtm = NULL;
	this->expm = NULL;
	this->logm = NULL;

	this->currentPower = 1;
	this->powm = NULL;
}

CovMat::~CovMat()
{
	delete this->sqrtm;
	delete this->invsqrtm;
	delete this->expm;
	delete this->logm;
}

double CovMat::Norm() const
{
	return this->eigenMatrix.norm();
}

double CovMat::Determinant() const
{
	return this->eigenMatrix.determinant();
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

CovMat CovMat::Powm(double power)
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