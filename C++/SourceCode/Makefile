all : CovMat.o Distance.o Geodesic.o Mean.o TestSourceCode

CovMat.o : CovMat.cpp
	g++ -std=c++11 -Wall -c -O3 -march=native CovMat.cpp -o CovMat.o -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Distance.o : Distance.cpp
	g++ -std=c++11 -Wall -c -O3 -march=native Distance.cpp -o Distance.o -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Geodesic.o : Geodesic.cpp
	g++ -std=c++11 -Wall -c -O3 -march=native Geodesic.cpp -o Geodesic.o -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Mean.o : Mean.cpp
	g++ -std=c++11 -Wall -c -O3 -march=native Mean.cpp -o Mean.o -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

TestSourceCode : TestSourceCode.cpp
	g++ -std=c++11 -Wall CovMat.o Distance.o Geodesic.o Mean.o TestSourceCode.cpp -o TestSourceCode -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo
