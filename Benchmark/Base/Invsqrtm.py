#!/usr/bin/python
 
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "SourceCode")))

import time
from CovMat import CovMat

size = [10, 25, 50, 75, 100, 250, 500, 750, 1000]
tpsCovMat = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 9) :
	#WARMUP
	for j in range(0, 10) :
		C = CovMat.Random(500)
		C.Invsqrtm()

	for j in range(0, 10) :
		covMat = CovMat.Random(size[i])

		start = time.time()
		covMat.Invsqrtm()
		tpsCovMat[i] += time.time() - start

	tpsCovMat[i] /= 10
	print("CovMat size : " + str(size[i]) + "x" + str(size[i]) + "	speed up : " + str(tpsCovMat[i]) + " sec") 
