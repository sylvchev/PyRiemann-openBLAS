AbstractObjects = AbstractClass/AbsMat.o AbstractClass/AbsRealMat.o AbstractClass/AbsRealSqMat.o AbstractClass/AbsRealSymMat.o AbstractClass/AbsRealNonSymMat.o
InstanciableOjects = Class/RealSymRegMat.o Class/RealSymPosDefMat.o Class/RealSqPosDefRegMat.o
Objects = $(AbstractObjects) $(InstanciableOjects)

All : $(AbstractObjects) $(InstanciableOjects) Main

AbstractClass/AbsMat.o : AbstractClass/AbsMat.cpp
	g++ -Wall -O3 -march=native -I Eigen/ -c AbstractClass/AbsMat.cpp -o AbstractClass/AbsMat.o

AbstractClass/AbsRealMat.o : AbstractClass/AbsRealMat.cpp
	g++ -Wall -O3 -march=native -I Eigen/ -c AbstractClass/AbsRealMat.cpp -o AbstractClass/AbsRealMat.o

AbstractClass/AbsRealSqMat.o : AbstractClass/AbsRealSqMat.cpp
	g++ -Wall -O3 -march=native -I Eigen/ -c AbstractClass/AbsRealSqMat.cpp -o AbstractClass/AbsRealSqMat.o

AbstractClass/AbsRealSymMat.o : AbstractClass/AbsRealSymMat.cpp
	g++ -Wall -O3 -march=native -I Eigen/ -c AbstractClass/AbsRealSymMat.cpp -o AbstractClass/AbsRealSymMat.o

AbstractClass/AbsRealNonSymMat.o : AbstractClass/AbsRealNonSymMat.cpp
	g++ -Wall -O3 -march=native -I Eigen/ -c AbstractClass/AbsRealNonSymMat.cpp -o AbstractClass/AbsRealNonSymMat.o

Class/RealSymRegMat.o : Class/RealSymRegMat.cpp
	g++ -Wall -O3 -march=native -I Eigen/ -c Class/RealSymRegMat.cpp -o Class/RealSymRegMat.o

Class/RealSymPosDefMat.o : Class/RealSymPosDefMat.cpp
	g++ -Wall -O3 -march=native -I Eigen/ -c Class/RealSymPosDefMat.cpp -o Class/RealSymPosDefMat.o

Class/RealSqPosDefRegMat.o : Class/RealSqPosDefRegMat.cpp
	g++ -Wall -O3 -march=native -I Eigen/ -c Class/RealSqPosDefRegMat.cpp -o Class/RealSqPosDefRegMat.o

Main : Main.cpp
	g++ -Wall -I Eigen/ Main.cpp $(Objects) -o Main
	