all : CovMat.o Distance.o Geodesic.o Mean.o TestSourceCode

CovMat.o : CovMat.cpp
	g++ -Wall -O3 -march=native -fopenmp -c CovMat.cpp -o CovMat.o 

Distance.o : Distance.cpp
	g++ -Wall -O3 -march=native -fopenmp -c Distance.cpp -o Distance.o 

Geodesic.o : Geodesic.cpp
	g++ -Wall -O3 -march=native -fopenmp -c Geodesic.cpp -o Geodesic.o

Mean.o : Mean.cpp
	g++ -Wall -O3 -march=native -fopenmp -c Mean.cpp -o Mean.o 

TestSourceCode : TestSourceCode.cpp
	g++ -Wall -O3 -march=native -fopenmp CovMat.o Distance.o Geodesic.o Mean.o TestSourceCode.cpp -o TestSourceCode