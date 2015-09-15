#include <iostream>
#include <vector>
#include "SourceCode/CovMat.hpp"
#include "SourceCode/Distance.hpp"
#include "SourceCode/Geodesic.hpp"
#include "SourceCode/Mean.hpp"

using namespace std;

int main()
{
	double array[] = {2, -1, 0, -1, 2, -1, 0, -1, 2};
	double array2[] = {4, -2, -6, -2, 10, 9, -6, 9, 14};
	double array3[] = {1, 0, 3, 0, 4, 2, 3, 2, 11};

	CovMat covMat1(array, 3);
	CovMat covMat2(array2, 3);
	CovMat covMat3(array3, 3);

	vector<CovMat> covMats;
	covMats.push_back(covMat1);
	covMats.push_back(covMat2);
	covMats.push_back(covMat3);

	cout << "covMat1 :\n" << covMat1 << endl << endl;
	cout << "covMat2 :\n" << covMat2 << endl << endl;
	cout << "covMat3 :\n" << covMat3 << endl << endl;

	cout << "covMat1.Determinant() :\n" << covMat1.Determinant() << endl << endl;
	cout << "covMat1.Norm() :\n" << covMat1.Norm() << endl << endl;
	cout << "covMat1.Inverse() :\n" << covMat1.Inverse() << endl << endl;
	cout << "covMat1.Transpose() :\n" << covMat1.Transpose() << endl << endl;
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

	cout << "IdentityMean(covMats)\n" << Mean::IdentityMean(covMats) << endl << endl;
	cout << "EucldieanMean(covMats)\n" << Mean::EuclideanMean(covMats) << endl << endl;
	cout << "LogEuclideanMean(covMats)\n" << Mean::LogEuclideanMean(covMats) << endl << endl;
	cout << "LogDeterminantMean(covMats)\n" << Mean::LogDeterminantMean(covMats) << endl << endl;
	cout << "RiemmanianMean(covMats)\n" << Mean::RiemmanianMean(covMats) << endl << endl;
}