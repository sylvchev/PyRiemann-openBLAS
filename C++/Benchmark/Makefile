BaseObjects = Base/Sqrtm Base/Invsqrtm Base/Expm Base/Logm Base/Powm
DistanceObjects = Distance/EuclideanDistance Distance/LogEuclideanDistance Distance/LogDeterminantDistance Distance/RiemannianDistance

all : $(BaseObjects) $(DistanceObjects)




Base/Sqrtm : Base/Sqrtm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Sqrtm.cpp -o Base/Sqrtm -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 

Base/Invsqrtm : Base/Invsqrtm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Invsqrtm.cpp -o Base/Invsqrtm -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 

Base/Expm : Base/Expm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Expm.cpp -o Base/Expm -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 

Base/Logm : Base/Logm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Logm.cpp -o Base/Logm -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 

Base/Powm : Base/Powm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Powm.cpp -o Base/Powm -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 





Distance/EuclideanDistance : Distance/EuclideanDistance.cpp
	g++ -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/EuclideanDistance.cpp -o Distance/EuclideanDistance -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 

Distance/LogEuclideanDistance : Distance/LogEuclideanDistance.cpp
	g++ -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/LogEuclideanDistance.cpp -o Distance/LogEuclideanDistance -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 

Distance/LogDeterminantDistance : Distance/LogDeterminantDistance.cpp
	g++ -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/LogDeterminantDistance.cpp -o Distance/LogDeterminantDistance -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 

Distance/RiemannianDistance : Distance/RiemannianDistance.cpp
	g++ -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/RiemannianDistance.cpp -o Distance/RiemannianDistance -L ../OpenBLAS/lib -lopenblas -DARMA_DONT_USE_WRAPPER -larmadillo 