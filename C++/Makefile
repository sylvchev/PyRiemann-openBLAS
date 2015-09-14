Objects = SourceCode/CovMat.o SourceCode/Distance.o SourceCode/Geodesic.o

all : $(Objects) Main

SourceCode/CovMat.o : SourceCode/CovMat.cpp
	g++ -Wall -O2 -march=native -I Eigen/ -c SourceCode/CovMat.cpp -o SourceCode/CovMat.o 

SourceCode/Distance.o : SourceCode/Distance.cpp
	g++ -Wall -O2 -march=native -I Eigen/ -c SourceCode/Distance.cpp -o SourceCode/Distance.o 

SourceCode/Geodesic.o : SourceCode/Geodesic.cpp
	g++ -Wall -O2 -march=native -I Eigen/ -c SourceCode/Geodesic.cpp -o SourceCode/Geodesic.o

SourceCode/Mean.o : SourceCode/Mean.cpp
	g++ -Wall -O2 -march=native -I Eigen/ -c SourceCode/Mean.cpp -o SourceCode/Mean.o 

Main : Main.cpp
	g++ -I Eigen/ $(Objects) Main.cpp -o Main