#!/usr/bin/python

# ---------------------------------------------------------------------------- #
# ------------------------------- DO NOT TOUCH ------------------------------- #
# ---------------------------------------------------------------------------- #

import ctypes
from ctypes.util import find_library

# enforces priority of hand-compiled OpenBLAS library over version in /usr/lib
# that comes from Ubuntu repos
try_paths = ['/opt/OpenBLAS/lib/libopenblas.so', '/lib/libopenblas.so', '/usr/lib/libopenblas.so.0', find_library('openblas')]
openblas_lib = None
for libpath in try_paths :
	try :
		openblas_lib = ctypes.cdll.LoadLibrary(libpath)
		break
	except OSError:
		continue
if openblas_lib is None :
	raise EnvironmentError('Could not locate an OpenBLAS shared library', 2)



def GetNbThreads():
	return openblas_lib.openblas_get_num_threads()



def SetNbThreads(n):
	openblas_lib.openblas_set_num_threads(int(n))



def NbThreads(n):
	return ThreadContext(n)


class ThreadContext(object):
	def __init__(self, num_threads):
		self._old_num_threads = GetNbThreads()
		self.num_threads = num_threads

	def __enter__(self):
		SetNbThreads(self.num_threads)

	def __exit__(self, *args):
		SetNbThreads(self._old_num_threads)