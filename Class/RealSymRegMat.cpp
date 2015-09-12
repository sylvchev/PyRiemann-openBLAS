#include <Eigen>
#include "RealSymRegMat.hpp" 

using namespace Eigen;

RealSymRegMat::RealSymRegMat(double* array, unsigned int matrixOrder)
{
	this->eigenMatrix = Map<MatrixXd, Aligned> (array, matrixOrder, matrixOrder);
	this->nbCols = matrixOrder;
	this->nbRows = matrixOrder;

	b_eigenValues = false;
	b_eigenVectors = false;

	this->expm = NULL;
	this->powm = NULL;
}

RealSymRegMat::RealSymRegMat(MatrixXd matrix)
{
	this->eigenMatrix = matrix;
	this->nbCols = matrix.cols();
	this->nbRows = matrix.rows();

	b_eigenValues = false;
	b_eigenVectors = false;

	this->expm = NULL;
	this->powm = NULL;
}

RealSymRegMat::~RealSymRegMat()
{
	
}

RealSymRegMat& RealSymRegMat::Powm(double power)
{
	if (this->powm != NULL)
		return *dynamic_cast<RealSymRegMat*>(this->powm);	

	this->ComputeEigen();

	VectorXd powEigenValues(this->nbCols);
	for (unsigned int i = 0; i < this->nbCols; i++)
		powEigenValues(i) = pow(this->eigenValues(i), power);

	this->powm = new RealSymRegMat(this->eigenVectors * powEigenValues.asDiagonal() * this->eigenVectors.transpose());

	return *dynamic_cast<RealSymRegMat*>(this->powm);
}