#!/usr/bin/python

import numpy
import Utils.OpenBLAS as OpenBLAS

# Used to set data type of matrix. Use only :
# 	- 'd' for double precision
# 	- 'f' for single precision, algorithms should be a little faster (≈ 10%)
data_type = numpy.dtype('d')

# Used to determine if data is copied when the CovMat class is created from an array or an existing matrix,
# or if the data is shared
# Used to avoid the memory allocation, and copy cost
memory_safe_state = False

# Number of thread used by those algorithm
# change by :
# nbThreads = X
# where X is the number of threads you want to use, or None if you want to use all disponible threads
# avoid hyperthreading, most of the time, alorithms are slower with it
nb_threads = 2


# ---------------------------------------------------------------------------- #
# ------------------------------- DO NOT TOUCH ------------------------------- #
# ---------------------------------------------------------------------------- #

if nb_threads is not None:
    OpenBLAS.set_nb_threads(nb_threads)
else:
    OpenBLAS.set_nb_threads(OpenBLAS.get_nb_procs())
