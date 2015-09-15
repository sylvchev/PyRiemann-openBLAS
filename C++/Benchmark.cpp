#include <iostream>
#include <sstream>
#include <ctime>
#include "SourceCode/CovMat.hpp"
#include "SourceCode/Distance.hpp"
#include "SourceCode/Geodesic.hpp" 
#include "SourceCode/Mean.hpp"

#define MATRIXSIZE 200
#define NBITER 30

int main()
{
	CovMat covMat1(MATRIXSIZE);
	string completionText = "";
	
	//Sqrtm benchmark
	double sqrtmTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "Sqrtm progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		covMat1.Randomize();
		double start = clock();
		covMat1.Sqrtm();
		sqrtmTime += clock() - start;
	}
	sqrtmTime /= NBITER;
	completionText += "Sqrtm progression benchmark : 100%\n";

	//Invsqrtm benchmark
	double invsqrtmTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "Invsqrtm progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		covMat1.Randomize();
		double start = clock();
		covMat1.Invsqrtm();
		invsqrtmTime += clock() - start;
	}
	invsqrtmTime /= NBITER;
	completionText += "Invsqrtm progression benchmark : 100%\n";

	//Expm benchmark
	double expmTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "Expm progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		covMat1.Randomize();
		double start = clock();
		covMat1.Expm();
		expmTime += clock() - start;
	}
	expmTime /= NBITER;
	completionText += "Expm progression benchmark : 100%\n";

	//Logm benchmark
	double logmTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "Logm progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		covMat1.Randomize();
		double start = clock();
		covMat1.Logm();
		logmTime += clock() - start;
	}
	logmTime /= NBITER;
	completionText += "Logm progression benchmark : 100%\n";

	//Powm benchmark
	double powmTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "Powm progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		covMat1.Randomize();
		double start = clock();
		covMat1.Powm(2);
		powmTime += clock() - start;
	}
	powmTime /= NBITER;
	completionText += "Powm progression benchmark : 100%\n";


	//Print result
	if(system("clear"));
	cout << completionText << endl;

	cout << "Sqrtm time : " << sqrtmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "Invsqrtm time : " << invsqrtmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "Expm time : " << expmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "Logm time : " << logmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "Powm time : " << powmTime / (double)CLOCKS_PER_SEC << "sec" << endl;



	/*cout << "covMat1.Invsqrtm() :\n" << covMat1.Invsqrtm() << endl << endl;
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
*/
}