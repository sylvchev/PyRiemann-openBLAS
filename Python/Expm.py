#!/usr/bin/python
 
import timeit
from CovMat import CovMat

for j in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] :
        A = CovMat(j)
        A.Randomize()

        #WARM UP
        for i in range(10) :
                B = CovMat(500)
                B.Randomize()
                B.Expm() 

        tps = 0 

        for i in range(20) :
                debut = timeit.default_timer()
                A.Expm()
                tps += timeit.default_timer() - debut
                A.Randomize()

        tps /= 20

        print("covmats type : " + str(j) + "x" + str(j) + "       time : " + str(tps))