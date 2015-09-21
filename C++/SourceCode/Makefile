all : CovMat.o Distance.o Geodesic.o Mean.o TestSourceCode

CovMat.o : CovMat.cpp
	g++ -Wall -c -O3 -march=native CovMat.cpp -o CovMat.o -larmadillo -lopenblas

Distance.o : Distance.cpp
	g++ -Wall -c -O3 -march=native Distance.cpp -o Distance.o -larmadillo -lopenblas

Geodesic.o : Geodesic.cpp
	g++ -Wall -c -O3 -march=native Geodesic.cpp -o Geodesic.o -larmadillo -lopenblas

Mean.o : Mean.cpp
	g++ -Wall -c -O3 -march=native Mean.cpp -o Mean.o -larmadillo -lopenblas

TestSourceCode : TestSourceCode.cpp
	g++ -Wall CovMat.o Distance.o Geodesic.o Mean.o TestSourceCode.cpp -o TestSourceCode -larmadillo
