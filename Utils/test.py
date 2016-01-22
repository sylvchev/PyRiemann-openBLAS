from oldPyRiemann.base import expm
from Utils.CovMats import CovMats
import numpy

a = CovMats.random(2, 3)
print(a)
print()
print(a.numpy_array.T)
