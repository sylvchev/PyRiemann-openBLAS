all : SourceCode/CovMat.o Main

SourceCode/CovMat.o : SourceCode/CovMat.cpp
	g++ -Wall -O2 -march=native -I Eigen/ -c SourceCode/CovMat.cpp -o SourceCode/CovMat.o 

Main : Main.cpp
	g++ -I Eigen/ SourceCode/CovMat.o Main.cpp -o Main