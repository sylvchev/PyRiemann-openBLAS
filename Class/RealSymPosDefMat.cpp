#include <Eigen>
#include "RealSymPosDefMat.hpp" 

#include <iostream>
using namespace std;

using namespace Eigen;

RealSymPosDefMat::RealSymPosDefMat(double* array, unsigned int matrixOrder)
{
	this->eigenMatrix = Map<MatrixXd, Aligned> (array, matrixOrder, matrixOrder);
	this->nbCols = matrixOrder;
	this->nbRows = matrixOrder;

	b_eigenValues = false;
	b_eigenVectors = false;

	this->sqrtm = NULL;
	this->invsqrtm = NULL;
	this->expm = NULL;
	this->logm = NULL;
	this->powm = NULL;
}

RealSymPosDefMat::RealSymPosDefMat(MatrixXd matrix)
{
	this->eigenMatrix = matrix;
	this->nbCols = matrix.cols();
	this->nbRows = matrix.rows();

	b_eigenValues = false;
	b_eigenVectors = false;

	this->sqrtm = NULL;
	this->invsqrtm = NULL;
	this->expm = NULL;
	this->logm = NULL;
	this->powm = NULL;
}

RealSymPosDefMat::~RealSymPosDefMat()
{
	
}

/*RealSymPosDefMat RealSymPosDefMat::Powm(double power)
{
	if (this->powm != NULL)
		return *(dynamic_cast<RealSymPosDefMat*>(this->powm));	

	this->ComputeEigen();

	VectorXd pow_eigenvalues(this->nbCols);
	for (unsigned int i = 0; i < this->nbCols; i++)
		pow_eigenvalues(i) = pow(eigenvalues(i), power);

	this->powm = new RealSymPosDefMat(this->eigenvectors * pow_eigenvalues.asDiagonal() * this->eigenvectors.transpose());

	return *(this->powm);
}*/