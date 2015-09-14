#include <iostream>
#include "SourceCode/CovMat.hpp"
#include "SourceCode/Distance.hpp"
#include "SourceCode/Geodesic.hpp"

using namespace std;

int main()
{
	double array[] = {2, -1, 0, -1, 2, -1, 0, -1, 2};
	double array2[] = {4, -2, 0, -2, 4, -2, 0, -2, 4};

	CovMat covMat1(array, 3);
	CovMat covMat2(array2, 3);

	cout << "covMat1 :\n" << covMat1 << endl << endl;
	cout << "covMat2 :\n" << covMat2 << endl << endl;

	cout << "covMat1.Sqrtm() :\n" << covMat1.Sqrtm() << endl << endl;
	cout << "covMat1.Invsqrtm() :\n" << covMat1.Invsqrtm() << endl << endl;
	cout << "covMat1.Expm() :\n" << covMat1.Expm() << endl << endl;
	cout << "covMat1.Logm() :\n" << covMat1.Logm() << endl << endl;
	cout << "covMat1.powm(2) :\n" << covMat1.Powm(2) << endl << endl;

	cout << "EuclideanDistance(covMat1, covMat2)\n" << Distance::EuclideanDistance(covMat1, covMat2) << endl << endl;
	cout << "LogEuclideanDistance(covMat1, covMat2)\n" << Distance::LogEuclideanDistance(covMat1, covMat2) << endl << endl;
	cout << "LogDeterminantDistance(covMat1, covMat2)\n" << Distance::LogDeterminantDistance(covMat1, covMat2) << endl << endl;
	cout << "RiemannianDistance(covMat1, covMat2)\n" << Distance::RiemannianDistance(covMat1, covMat2) << endl << endl;

	cout << "EuclideanGeodesic(covMat1, covMat2, 0.5)\n" << Geodesic::EuclideanGeodesic(covMat1, covMat2, 0.5) << endl << endl;
	cout << "LogEuclideanGeodesic(covMat1, covMat2, 0.5)\n" << Geodesic::LogEuclideanGeodesic(covMat1, covMat2, 0.5) << endl << endl;
	cout << "RiemannianGeodesic(covMat1, covMat2, 0.5)\n" << Geodesic::RiemannianGeodesic(covMat1, covMat2, 0.5) << endl << endl;
}