#include <Eigen>
#include "RealSymPosDefMat.hpp"

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

RealSymPosDefMat& RealSymPosDefMat::Powm(double power)
{
	if (this->powm != NULL)
		return *dynamic_cast<RealSymPosDefMat*>(this->powm);	

	this->ComputeEigen();

	VectorXd powEigenValues(this->nbCols);
	for (unsigned int i = 0; i < this->nbCols; i++)
		powEigenValues(i) = pow(this->eigenValues(i), power);

	this->powm = new RealSymPosDefMat(this->eigenVectors * powEigenValues.asDiagonal() * this->eigenVectors.transpose());

	return *dynamic_cast<RealSymPosDefMat*>(this->powm);
}