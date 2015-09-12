#include <Eigen>
#include "AbsRealNonSymMat.hpp" 

void AbsRealNonSymMat::ComputeEigen(bool eigenValuesOnly)
{
	if ((this->b_eigenValues)&&(this->b_eigenVectors))
		return;
	
	if ((this->b_eigenValues)&&(eigenValuesOnly))
		return;

	if (eigenValuesOnly)
	{
		EigenSolver<MatrixXd> es(this->eigenMatrix, EigenvaluesOnly);
		this->eigenValues = es.eigenvalues();
		this->b_eigenValues = true;
		return;
	}

	EigenSolver<MatrixXd> es(this->eigenMatrix);
	this->eigenValues = es.eigenvalues();
	this->eigenVectors = es.eigenvectors();
	this->b_eigenValues = true;
	this->b_eigenVectors = true;
}
