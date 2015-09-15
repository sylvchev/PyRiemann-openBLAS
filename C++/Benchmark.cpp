#include <iostream>
#include <sstream>
#include <ctime>
#include "SourceCode/CovMat.hpp"
#include "SourceCode/Distance.hpp"
#include "SourceCode/Geodesic.hpp" 
#include "SourceCode/Mean.hpp"

#define MATRIXSIZE 200
#define NBITER 20

int main()
{
	string completionText = "";

	CovMat covMat1(MATRIXSIZE); covMat1.Randomize();
	CovMat covMat2(MATRIXSIZE); covMat2.Randomize();
	CovMat covMat3(MATRIXSIZE); covMat3.Randomize();
	CovMat covMat4(MATRIXSIZE); covMat4.Randomize();
	CovMat covMat5(MATRIXSIZE); covMat5.Randomize();
	CovMat covMat6(MATRIXSIZE); covMat6.Randomize();
	CovMat covMat7(MATRIXSIZE); covMat7.Randomize();
	CovMat covMat8(MATRIXSIZE); covMat8.Randomize();
	CovMat covMat9(MATRIXSIZE); covMat9.Randomize();
	CovMat covMat10(MATRIXSIZE); covMat10.Randomize();

	vector<CovMat> covMats;
	covMats.push_back(covMat1);
	covMats.push_back(covMat2);
	covMats.push_back(covMat3);
	covMats.push_back(covMat4);
	covMats.push_back(covMat5);
	covMats.push_back(covMat6);
	covMats.push_back(covMat7);
	covMats.push_back(covMat8);
	covMats.push_back(covMat9);
	covMats.push_back(covMat10);

	completionText += "Variable initialization : 100%\n";
	cout << completionText;
	
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

	//EuclideanDistance benchmark
	double euclideanDistanceTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "EuclideanDistance progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		double start = clock();
		Distance::EuclideanDistance(covMat1, covMat2);
		euclideanDistanceTime += clock() - start;
	}
	euclideanDistanceTime /= NBITER;
	completionText += "EuclideanDistance progression benchmark : 100%\n";

	//LogEuclideanDistance benchmark
	double logEuclideanDistanceTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "LogEuclideanDistance progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		double start = clock();
		Distance::LogEuclideanDistance(covMat1, covMat2);
		logEuclideanDistanceTime += clock() - start;
	}
	logEuclideanDistanceTime /= NBITER;
	completionText += "LogEuclideanDistance progression benchmark : 100%\n";

	//LogDeterminantDistance benchmark
	double logDeterminantDistanceTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "LogDeterminantDistance progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		double start = clock();
		Distance::LogDeterminantDistance(covMat1, covMat2);
		logDeterminantDistanceTime += clock() - start;
	}
	logDeterminantDistanceTime /= NBITER;
	completionText += "LogDeterminantDistance progression benchmark : 100%\n";

	//RiemannianDistance benchmark
	double riemannianDistanceTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "RiemannianDistance progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		double start = clock();
		Distance::RiemannianDistance(covMat1, covMat2);
		riemannianDistanceTime += clock() - start;
	}
	riemannianDistanceTime /= NBITER;
	completionText += "RiemannianDistance progression benchmark : 100%\n";

	//EuclideanGeodesic benchmark
	double euclideanGeodesicTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "EuclideanGeodesic progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		double start = clock();
		Geodesic::EuclideanGeodesic(covMat1, covMat2, 0.5);
		euclideanGeodesicTime += clock() - start;
	}
	euclideanGeodesicTime /= NBITER;
	completionText += "EuclideanGeodesic progression benchmark : 100%\n";

	//LogEuclideanGeodesic benchmark
	double logEuclideanGeodesicTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "LogEuclideanGeodesic progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		double start = clock();
		Geodesic::EuclideanGeodesic(covMat1, covMat2, 0.5);
		logEuclideanGeodesicTime += clock() - start;
	}
	logEuclideanGeodesicTime /= NBITER;
	completionText += "LogEuclideanGeodesic progression benchmark : 100%\n";

	//RiemannianGeodesic benchmark
	double riemannianGeodesicTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "RiemannianGeodesic progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		double start = clock();
		Geodesic::RiemannianGeodesic(covMat1, covMat2, 0.5);
		riemannianGeodesicTime += clock() - start;
	}
	riemannianGeodesicTime /= NBITER;
	completionText += "RiemannianGeodesic progression benchmark : 100%\n";

	//Print result
	if(system("clear"));
	cout << completionText << endl;

	cout << "CovMat size :" << MATRIXSIZE << "x" << MATRIXSIZE << endl << endl;
	cout << "Results :" << endl;
	cout << "Sqrtm time : " << sqrtmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "Invsqrtm time : " << invsqrtmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "Expm time : " << expmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "Logm time : " << logmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "Powm time : " << powmTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "EuclideanDistance time : " << euclideanDistanceTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "LogEuclideanDistance time : " << logEuclideanDistanceTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "LogDeterminantDistance time : " << logDeterminantDistanceTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "RiemannianDistance time : " << riemannianDistanceTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "EuclideanGeodesic time : " << euclideanGeodesicTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "LogEuclideanGeodesic time : " << logEuclideanGeodesicTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "RiemannianGeodesic time : " << riemannianGeodesicTime / (double)CLOCKS_PER_SEC << "sec" << endl;


	cout << endl << endl;
}