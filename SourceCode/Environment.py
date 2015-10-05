#!/usr/bin/python

import numpy
import OpenBLAS

#Used to set data type of matrix. Use only :
#	- 'd' for double precision
#	- 'f' for single precision, algorithms should be a little faster (≈ 10%)
dataType = numpy.dtype('d')

#Used to determine if data is copied when the CovMat class is created from an array or an existing matrix, or if the data is shared
#Used to avoid the memory allocation, and copy cost
memorySafeState = False

#Number of thread used by those algorithm
#change by : 
#nbThreads = X
#where X is the number of threads you want to use, or None if you want to use all disponible threads
#avoid hyperthreading, most of the time, alorithms are slower with it
nbThreads = 2



# ---------------------------------------------------------------------------- #
# ------------------------------- DO NOT TOUCH ------------------------------- #
# ---------------------------------------------------------------------------- #

if (nbThreads is not None) :
	OpenBLAS.SetNbThreads(nbThreads)
else :
	OpenBLAS.SetNbThreads(OpenBLAS.GetNbProc())
