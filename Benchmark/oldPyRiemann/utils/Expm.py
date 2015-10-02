#!/usr/bin/python
 
import numpy
import timeit
from base import expm

for j in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] :
        Q = numpy.random.rand(j, 20*j)
        A = numpy.dot(Q, Q.T)

        #WARM UP
        for i in range(10) :
                tmp = expm(A)

        debut = timeit.default_timer()
        for i in range(20) :
                tmp = expm(A)
        fin = timeit.default_timer()

        time = (fin-debut)/20

        print("covmats type : " + str(j) + "x" + str(j) + "       time : " + str(time))