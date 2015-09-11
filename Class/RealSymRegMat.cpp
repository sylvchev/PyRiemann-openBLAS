#include <Eigen>
#include "RealSymRegMat.hpp" 

using namespace Eigen;

RealSymRegMat::RealSymRegMat(double* array, unsigned int matrixOrder)
{
	this->matrix = Map<MatrixXd, Aligned> (array, matrixOrder, matrixOrder);
	this->nbCols = matrixOrder;
	this->nbRows = matrixOrder;

	b_eigenvalues = false;
	b_eigenvectors = false;

	this->expm = NULL;
	this->powm = NULL;
}

RealSymRegMat::RealSymRegMat(MatrixXd matrix)
{
	this->matrix = matrix;
	this->nbCols = matrix.cols();
	this->nbRows = matrix.rows();

	b_eigenvalues = false;
	b_eigenvectors = false;

	this->expm = NULL;
	this->powm = NULL;
}

RealSymRegMat::~RealSymRegMat()
{
	
}

RealSymRegMat RealSymRegMat::Powm(double power)
{
	if (this->powm != NULL)
		return *(dynamic_cast<RealSymRegMat*>(this->powm));	

	this->ComputeEigen();

	VectorXd pow_eigenvalues(this->nbCols);
	for (unsigned int i = 0; i < this->nbCols; i++)
		pow_eigenvalues(i) = pow(eigenvalues(i), power);

	this->powm = new RealSymRegMat(this->eigenvectors * pow_eigenvalues.asDiagonal() * this->eigenvectors.transpose());

	return *(dynamic_cast<RealSymRegMat*>(this->powm));
}