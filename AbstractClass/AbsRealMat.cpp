#include <iostream>
#include <Eigen>
#include "AbsRealMat.hpp" 

using namespace std;
using namespace Eigen;

double AbsRealMat::Norm()
{
	return this->matrix.norm();
}

ostream& operator << (ostream &output, const AbsRealMat& absRealMat)
{ 
    output << absRealMat.matrix;
    return output;            
}