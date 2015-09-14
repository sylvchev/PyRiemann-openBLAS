Objects = SourceCode/CovMat.o SourceCode/Distance.o SourceCode/Geodesic.o SourceCode/Mean.o

all : $(Objects) Main

SourceCode/CovMat.o : SourceCode/CovMat.cpp
	g++ -std=c++11 -Wall -O2 -march=native -I Eigen/ -c SourceCode/CovMat.cpp -o SourceCode/CovMat.o 

SourceCode/Distance.o : SourceCode/Distance.cpp
	g++ -std=c++11 -Wall -O2 -march=native -I Eigen/ -c SourceCode/Distance.cpp -o SourceCode/Distance.o 

SourceCode/Geodesic.o : SourceCode/Geodesic.cpp
	g++ -std=c++11 -Wall -O2 -march=native -I Eigen/ -c SourceCode/Geodesic.cpp -o SourceCode/Geodesic.o

SourceCode/Mean.o : SourceCode/Mean.cpp
	g++ -std=c++11 -Wall -O2 -march=native -I Eigen/ -c SourceCode/Mean.cpp -o SourceCode/Mean.o 

Main : Main.cpp
	g++ -std=c++11 -I Eigen/ $(Objects) Main.cpp -o Main