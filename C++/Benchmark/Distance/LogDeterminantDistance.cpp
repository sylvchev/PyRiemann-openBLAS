#include <iostream>
#include <vector>
#include "../../SourceCode/CovMat.hpp"
#include "../../SourceCode/Distance.hpp"

#define NBREPET 20

using namespace std;

int main()
{
	//Variable initialization
	wall_clock timer;
	unsigned int v[9] = {10, 25, 50, 75, 100, 250, 500, 750, 1000};
	double time[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
	vector<CovMat> covMats1;
	vector<CovMat> covMats2;

	string completionText = "";

	for (unsigned int i = 0; i < 9; i++)
	{
		if(system("clear"));
		cout << completionText;
		cout << "Initializing variables : " << ((double)i/(double)9)*100 << "%" << endl;
		CovMat c1(v[i]);
		CovMat c2(v[i]);
		c1.Randomize();
		c2.Randomize();
		covMats1.push_back(c1);
		covMats2.push_back(c2);
	}
	completionText += "Initializing variables : 100%\n";

	//WARMUP
	for (unsigned int i = 0; i < NBREPET; i++)
	{
		if(system("clear"));
		cout << completionText;
		cout << "Warm up : " << ((double)i/(double)NBREPET)*100 << "%" << endl;
		CovMat c(500);
		c.Randomize();
		c.Logm();
	}
	completionText += "Warm up : 100%\n";

	//Benchmark
	for (unsigned int i = 0; i < 9; i++)
	{
		for (unsigned int j = 0; j < NBREPET; j++)
		{			
			if(system("clear"));
			cout << completionText;
			cout << "Benchmarking log determinant distance : " << ((double)(i*NBREPET + j)/(double)(9*NBREPET))*100 << "%" << endl;
			covMats1[i].DeleteAllocatedVar();
			covMats1[i].ConstructorInitialize();
			covMats2[i].DeleteAllocatedVar();
			covMats2[i].ConstructorInitialize();
			timer.tic();
			Distance::LogDeterminantDistance(covMats1[i], covMats2[i]);
			time[i] += timer.toc();
		}
	}
	completionText += "Benchmarking log determinant distance : 100%\n\n";

	//Print results
	if(system("clear"));
	cout << completionText << "Results :\n";

	for (unsigned int i = 0; i < 9; i++)
	{
		cout << "Matrix type : " << v[i] << "x" << v[i] << "	time : " << time[i]/NBREPET << " sec" << endl;
	}
} 
 
 
 
