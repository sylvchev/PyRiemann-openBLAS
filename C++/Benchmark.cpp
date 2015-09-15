#include <iostream>
#include <sstream>
#include <ctime>
#include "SourceCode/CovMat.hpp"
#include "SourceCode/Distance.hpp"
#include "SourceCode/Geodesic.hpp" 
#include "SourceCode/Mean.hpp"

#define MATRIXSIZE 100
#define COVMATSSIZE 10
#define NBITER 10

void RandomizeCovMats(vector<CovMat>& covMats)
{
	for (unsigned int i = 0; i < COVMATSSIZE; i++)
	{
		CovMat c(MATRIXSIZE);
		c.Randomize();
		covMats.push_back(c);
	}
}

int main()
{
	string completionText = "";

	CovMat covMat1(MATRIXSIZE);
	CovMat covMat2(MATRIXSIZE);

	vector<CovMat> covMats;
	RandomizeCovMats(covMats);

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
		covMat1.Randomize();
		covMat2.Randomize();
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
		covMat1.Randomize();
		covMat2.Randomize();
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
		covMat1.Randomize();
		covMat2.Randomize();
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
		covMat1.Randomize();
		covMat2.Randomize();
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
		covMat1.Randomize();
		covMat2.Randomize();
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
		covMat1.Randomize();
		covMat2.Randomize();
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
		covMat1.Randomize();
		covMat2.Randomize();
		double start = clock();
		Geodesic::RiemannianGeodesic(covMat1, covMat2, 0.5);
		riemannianGeodesicTime += clock() - start;
	}
	riemannianGeodesicTime /= NBITER;
	completionText += "RiemannianGeodesic progression benchmark : 100%\n";

	//IdentityMean benchmark
	double identityMeanTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "IdentityMean progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		RandomizeCovMats(covMats);
		double start = clock();
		Mean::IdentityMean(covMats);
		identityMeanTime += clock() - start;
	}
	identityMeanTime /= NBITER;
	completionText += "IdentityMean progression benchmark : 100%\n";

	//EuclideanMean benchmark
	double euclideanMeanTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "EuclideanMean progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		RandomizeCovMats(covMats);
		double start = clock();
		Mean::EuclideanMean(covMats);
		euclideanMeanTime += clock() - start;
	}
	euclideanMeanTime /= NBITER;
	completionText += "EuclideanMean progression benchmark : 100%\n";

	//LogEuclideanMean benchmark
	double logEuclideanMeanTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "LogEuclideanMean progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		RandomizeCovMats(covMats);
		double start = clock();
		Mean::LogEuclideanMean(covMats);
		logEuclideanMeanTime += clock() - start;
	}
	logEuclideanMeanTime /= NBITER;
	completionText += "LogEuclideanMean progression benchmark : 100%\n";

	//LogDeterminantMean benchmark
	double logDeterminantMeanTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "LogDeterminantMean progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		RandomizeCovMats(covMats);
		double start = clock();
		Mean::LogDeterminantMean(covMats);
		logDeterminantMeanTime += clock() - start;
	}
	logDeterminantMeanTime /= NBITER;
	completionText += "LogDeterminantMean progression benchmark : 100%\n";

	//RiemannianMean benchmark
	double riemannianMeanTime = 0;
	for (unsigned int i = 1; i <= NBITER; i++)
	{	
		if(system("clear"));
		cout << completionText;
		cout << "RiemannianMean progression benchmark : " << (double)(i*100)/(double)NBITER << "%" << endl;
		RandomizeCovMats(covMats);
		double start = clock();
		Mean::RiemannianMean(covMats);
		riemannianMeanTime += clock() - start;
	}
	riemannianMeanTime /= NBITER;
	completionText += "RiemannianMean progression benchmark : 100%\n";

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
	cout << "IdentityMean time : " << identityMeanTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "EuclideanMean time : " << euclideanMeanTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "LogEuclideanMean time : " << logEuclideanMeanTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "LogDeterminantMean time : " << logDeterminantMeanTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << "RiemannianMean time : " << riemannianMeanTime / (double)CLOCKS_PER_SEC << "sec" << endl;
	cout << endl << endl;
}