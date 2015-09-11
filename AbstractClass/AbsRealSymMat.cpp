#include <Eigen>
#include "AbsRealSymMat.hpp"
#include "../Class/RealSymPosDefMat.hpp"

using namespace Eigen;

void AbsRealSymMat::ComputeEigen(bool eigenvaluesOnly)
{
	if ((this->b_eigenvalues)&&(this->b_eigenvectors))
		return;
	
	if ((this->b_eigenvalues)&&(eigenvaluesOnly))
		return;

	if (eigenvaluesOnly)
	{
		SelfAdjointEigenSolver<MatrixXd> es(this->matrix, EigenvaluesOnly);
		this->eigenvalues = es.eigenvalues().real();
		this->b_eigenvalues = true;
		return;
	}

	SelfAdjointEigenSolver<MatrixXd> es(this->matrix);
	this->eigenvalues = es.eigenvalues().real();
	this->eigenvectors = es.eigenvectors().real();
	this->b_eigenvalues = true;
	this->b_eigenvectors = true;
}

RealSymPosDefMat AbsRealSymMat::Expm()
{
	if (this->expm != NULL)
		return *(dynamic_cast<RealSymPosDefMat*>(this->expm));	

	this->ComputeEigen();

	VectorXd exp_eigenvalues(this->nbCols);
	for (unsigned int i = 0; i < this->nbCols; i++)
		exp_eigenvalues(i) = exp(eigenvalues(i));

	this->expm = new RealSymPosDefMat(this->eigenvectors * exp_eigenvalues.asDiagonal() * this->eigenvectors.transpose());

	return *(dynamic_cast<RealSymPosDefMat*>(this->expm));
}