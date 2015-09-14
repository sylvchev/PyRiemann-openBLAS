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
}


CovMat::CovMat(const MatrixXd& eigenMatrix)
{
	this->eigenMatrix = eigenMatrix;
	this->matrixOrder = eigenMatrix.cols();

	this->b_eigenValues = false;
	this->b_eigenVectors = false;

	this->sqrtm = NULL;
	this->invsqrtm = NULL;
	this->expm = NULL;
	this->logm = NULL;
}

CovMat::~CovMat()
{
	delete this->sqrtm;
	delete this->invsqrtm;
	delete this->expm;
	delete this->logm;
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

ostream& operator << (ostream &output, const CovMat& covMat)
{ 
    output << covMat.eigenMatrix;
    return output;            
}
