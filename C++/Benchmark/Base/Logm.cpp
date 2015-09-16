#include <iostream>
#include <vector>
#include <ctime>
#include "../../SourceCode/CovMat.hpp"

#define NBREPET 20

using namespace std;

int main()
{
	//Variable initialization
	unsigned int v[9] = {10, 25, 50, 75, 100, 250, 500, 750, 1000};
	double time[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
	vector<CovMat> covMats;

	string completionText = "";

	for (unsigned int i = 0; i < 9; i++)
	{
		if(system("clear"));
		cout << completionText;
		cout << "Initializing variables : " << ((double)i/(double)9)*100 << "%" << endl;
		CovMat c(v[i]);
		c.Randomize();
		covMats.push_back(c);
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
			cout << "Benchmarking logm : " << ((double)(i*NBREPET + j)/(double)(9*NBREPET))*100 << "%" << endl;

			covMats[i].DeleteAllocatedVar();
			covMats[i].ConstructorInitialize();
			double start = clock();
			covMats[i].Logm();
			time[i] += clock() - start;
		}
	}
	completionText += "Benchmarking logm : 100%\n\n";

	//Print results
	if(system("clear"));
	cout << completionText << "Results :\n";

	for (unsigned int i = 0; i < 9; i++)
	{
		time[i] /= NBREPET;
		time[i] /= CLOCKS_PER_SEC;

		cout << "Matrix type : " << v[i] << "x" << v[i] << "	time : " << time[i] << " sec" << endl;
	}
} 
