#include <Eigen>
#include "AbsRealSymMat.hpp"
#include "../Class/RealSymPosDefMat.hpp"

using namespace Eigen;

void AbsRealSymMat::ComputeEigen(bool eigenValuesOnly)
{
	if ((this->b_eigenValues)&&(this->b_eigenVectors))
		return;
	
	if ((this->b_eigenValues)&&(eigenValuesOnly))
		return;

	if (eigenValuesOnly)
	{
		SelfAdjointEigenSolver<MatrixXd> es(this->eigenMatrix, EigenvaluesOnly);
		this->eigenValues = es.eigenvalues().real();
		this->b_eigenValues = true;
		return;
	}

	SelfAdjointEigenSolver<MatrixXd> es(this->eigenMatrix);
	this->eigenValues = es.eigenvalues().real();
	this->eigenVectors = es.eigenvectors().real();
	this->b_eigenValues = true;
	this->b_eigenVectors = true;
}

RealSymPosDefMat& AbsRealSymMat::Expm()
{
	if (this->expm != NULL)
		return *dynamic_cast<RealSymPosDefMat*>(this->expm);	

	this->ComputeEigen();

	VectorXd expEigenValues(this->nbCols);
	for (unsigned int i = 0; i < this->nbCols; i++)
		expEigenValues(i) = exp(this->eigenValues(i));

	this->expm = new RealSymPosDefMat(this->eigenVectors * expEigenValues.asDiagonal() * this->eigenVectors.transpose());

	return *dynamic_cast<RealSymPosDefMat*>(this->expm);
}