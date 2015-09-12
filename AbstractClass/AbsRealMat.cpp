#include <iostream>
#include <Eigen>
#include "AbsRealMat.hpp" 

using namespace std;
using namespace Eigen;

double AbsRealMat::Norm()
{
	return this->eigenMatrix.norm();
}

ostream& operator << (ostream &output, const AbsRealMat& absRealMat)
{ 
    output << absRealMat.eigenMatrix;
    return output;            
}