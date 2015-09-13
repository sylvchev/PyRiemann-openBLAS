all : C++/CovMat.o Main

C++/CovMat.o : C++/CovMat.cpp
	g++ -Wall -O2 -march=native -I Eigen/ -c C++/CovMat.cpp -o C++/CovMat.o 

Main : Main.cpp
	g++ -I Eigen/ C++/CovMat.o Main.cpp -o Main