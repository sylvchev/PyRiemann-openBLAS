BaseObjects = Base/Sqrtm Base/Invsqrtm Base/Expm Base/Logm Base/Powm
DistanceObjects = Distance/EuclideanDistance Distance/LogEuclideanDistance Distance/LogDeterminantDistance Distance/RiemannianDistance

all : $(BaseObjects) $(DistanceObjects)



Base/Sqrtm : Base/Sqrtm.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o Base/Sqrtm.cpp -o Base/Sqrtm -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Base/Invsqrtm : Base/Invsqrtm.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o Base/Invsqrtm.cpp -o Base/Invsqrtm -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Base/Expm : Base/Expm.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o Base/Expm.cpp -o Base/Expm -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Base/Logm : Base/Logm.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o Base/Logm.cpp -o Base/Logm -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Base/Powm : Base/Powm.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o Base/Powm.cpp -o Base/Powm -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 





Distance/EuclideanDistance : Distance/EuclideanDistance.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/EuclideanDistance.cpp -o Distance/EuclideanDistance -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Distance/LogEuclideanDistance : Distance/LogEuclideanDistance.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/LogEuclideanDistance.cpp -o Distance/LogEuclideanDistance -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 

Distance/LogDeterminantDistance : Distance/LogDeterminantDistance.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/LogDeterminantDistance.cpp -o Distance/LogDeterminantDistance -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 
Distance/RiemannianDistance : Distance/RiemannianDistance.cpp
	g++-4.9 -std=c++11 -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/RiemannianDistance.cpp -o Distance/RiemannianDistance -DARMA_DONT_USE_WRAPPER -DARMA_USE_BLAS -DARMA_USE_LAPACK -lopenblas -llapack -larmadillo 
