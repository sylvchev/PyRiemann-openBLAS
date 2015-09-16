BaseObjects = Base/Sqrtm Base/Invsqrtm Base/Expm Base/Logm Base/Powm
DistanceObjects = Distance/EuclideanDistance Distance/LogEuclideanDistance Distance/LogDeterminantDistance Distance/RiemannianDistance

all : $(BaseObjects) $(DistanceObjects)




Base/Sqrtm : Base/Sqrtm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Sqrtm.cpp -o Base/Sqrtm -larmadillo

Base/Invsqrtm : Base/Invsqrtm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Invsqrtm.cpp -o Base/Invsqrtm -larmadillo

Base/Expm : Base/Expm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Expm.cpp -o Base/Expm -larmadillo

Base/Logm : Base/Logm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Logm.cpp -o Base/Logm -larmadillo

Base/Powm : Base/Powm.cpp
	g++ -Wall ../SourceCode/CovMat.o Base/Powm.cpp -o Base/Powm -larmadillo





Distance/EuclideanDistance : Distance/EuclideanDistance.cpp
	g++ -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/EuclideanDistance.cpp -o Distance/EuclideanDistance -larmadillo

Distance/LogEuclideanDistance : Distance/LogEuclideanDistance.cpp
	g++ -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/LogEuclideanDistance.cpp -o Distance/LogEuclideanDistance -larmadillo

Distance/LogDeterminantDistance : Distance/LogDeterminantDistance.cpp
	g++ -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/LogDeterminantDistance.cpp -o Distance/LogDeterminantDistance -larmadillo

Distance/RiemannianDistance : Distance/RiemannianDistance.cpp
	g++ -Wall ../SourceCode/CovMat.o ../SourceCode/Distance.o Distance/RiemannianDistance.cpp -o Distance/RiemannianDistance -larmadillo