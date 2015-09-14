#include <iostream>
#include "SourceCode/CovMat.hpp"

using namespace std;

int main()
{
	double array[] = {2, -1, 0, -1, 2, -1, 0, -1, 2};

	cout << "toto" << endl;

	CovMat covMat(array, 3);

	cout << "toto" << endl;

	cout << covMat << endl << endl;
	cout << covMat.Sqrtm() << endl << endl;
	cout << covMat.Invsqrtm() << endl << endl;
	cout << covMat.Expm() << endl << endl;
	cout << covMat.Logm() << endl << endl;
	cout << covMat.Powm(2) << endl << endl;
}