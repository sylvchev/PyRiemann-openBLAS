#!/usr/bin/python

# ---------------------------------------------------------------------------- #
# ------------------------------- DO NOT TOUCH ------------------------------- #
# ---------------------------------------------------------------------------- #

#solution find here : http://stackoverflow.com/questions/29559338/set-max-number-of-threads-at-runtime-on-numpy-openblas
#Thanks to : ali_m

import ctypes
from ctypes.util import find_library

openblas_lib = ctypes.cdll.LoadLibrary('/usr/local/lib/libopenblas.so')



def GetNbThreads():
	return openblas_lib.openblas_get_num_threads()



def SetNbThreads(n):
	openblas_lib.openblas_set_num_threads(n)



def GetNbProc():
	return openblas_lib.openblas_get_num_procs()



class NbThreads :
	def __init__(self, nbThreads):
		self.oldNbTreads = GetNbThreads()
		self.nbThreads = nbThreads



	def __enter__(self):
		SetNbThreads(self.nbThreads)



	def __exit__(self, *args):
		SetNbThreads(self.oldNbTreads)
