#!/usr/bin/python

import numpy

#Used to set data type of matrix. Use only :
#	- 'd' for double precision
#	- 'f' for single precision, algorithme should be a little faster
dataType = numpy.dtype('d')

#Used to determine if data is copied when the CovMat class is created from an array or an existing matrix, or if the data is shared
#Used to avoid the memory allocation, and copy cost
copyArrayMemoryCovMatConstructor = True