Objects = SourceCode/CovMat.o SourceCode/Distance.o SourceCode/Geodesic.o SourceCode/Mean.o

all : $(Objects) Main Benchmark

SourceCode/CovMat.o : SourceCode/CovMat.cpp
	g++ -Wall -O3 -march=native -fopenmp -c SourceCode/CovMat.cpp -o SourceCode/CovMat.o 

SourceCode/Distance.o : SourceCode/Distance.cpp
	g++ -Wall -O3 -march=native -fopenmp -c SourceCode/Distance.cpp -o SourceCode/Distance.o 

SourceCode/Geodesic.o : SourceCode/Geodesic.cpp
	g++ -Wall -O3 -march=native -fopenmp -c SourceCode/Geodesic.cpp -o SourceCode/Geodesic.o

SourceCode/Mean.o : SourceCode/Mean.cpp
	g++ -Wall -O3 -march=native -fopenmp -c SourceCode/Mean.cpp -o SourceCode/Mean.o 

Main : Main.cpp
	g++ -Wall -O3 -march=native -fopenmp $(Objects) Main.cpp -o Main

Benchmark : Benchmark.cpp
	g++ -Wall -O3 -march=native -fopenmp $(Objects) Benchmark.cpp -o Benchmark