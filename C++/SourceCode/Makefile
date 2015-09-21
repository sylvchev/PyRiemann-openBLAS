all : CovMat.o Distance.o Geodesic.o Mean.o TestSourceCode

CovMat.o : CovMat.cpp
	g++ -Wall -c -O3 -march=native CovMat.cpp -o CovMat.o -L ../OpenBLAS/lib -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -larmadillo 

Distance.o : Distance.cpp
	g++ -Wall -c -O3 -march=native Distance.cpp -o Distance.o -L ../OpenBLAS/lib -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -larmadillo 

Geodesic.o : Geodesic.cpp
	g++ -Wall -c -O3 -march=native Geodesic.cpp -o Geodesic.o -L ../OpenBLAS/lib -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -larmadillo 

Mean.o : Mean.cpp
	g++ -Wall -c -O3 -march=native Mean.cpp -o Mean.o -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -larmadillo 

TestSourceCode : TestSourceCode.cpp
	g++ -Wall CovMat.o Distance.o Geodesic.o Mean.o TestSourceCode.cpp -o TestSourceCode -L ../OpenBLAS/lib -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo
