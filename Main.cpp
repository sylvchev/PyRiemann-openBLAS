#include <iostream>
#include "Class/RealSymPosDefMat.hpp"

using namespace std;

int main()
{
	double array[] = {2, -1, 0, -1, 2, -1, 0, -1, 2};
	double array2[] = {1, 2, 3, 2, 4, 5, 3, 5, 6};

	RealSymPosDefMat symPosDefMat((double*)(&array), 3);
	RealSymPosDefMat symRegMat((double*)(&array2), 3);

	cout << "sym reg mat\n" << symRegMat << endl << endl;

	cout << "sym reg mat expm\n" << symRegMat.Expm() << endl << endl;
	cout << "sym reg mat powm\n" << symRegMat.Powm(2) << endl << endl;

	cout << "sym pos def mat\n" << symPosDefMat << endl << endl;

	cout << "sym pos def mat expm\n" << symPosDefMat.Expm() << endl << endl;
	cout << "sym pos def mat powm\n" << symPosDefMat.Powm(2) << endl << endl;
}