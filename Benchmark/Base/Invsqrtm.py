#!/usr/bin/python
 
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Utils")))

import time
from CovMat import CovMat

def PrintProgress (i) :
	text = "Progress : " + str(i) + "%"
	sys.stdout.write(" " * 20)
	sys.stdout.write("\b" * 20)
	sys.stdout.write(text)
	sys.stdout.write("\b" * len(text))
	sys.stdout.flush()

nbRepet = 5
size = [10, 25, 50, 75, 100, 250, 500, 750, 1000]
tpsCovMat = [0, 0, 0, 0, 0, 0, 0, 0, 0]

warmUpCovMat = CovMat.Random(500)

PrintProgress(0)

for i in range(0, len(size)) :
	#WARMUP
	for j in range(0, nbRepet) :
		warmUpCovMat.FieldsInitialization()
		warmUpCovMat.Invsqrtm()

	covMat = CovMat.Random(size[i])
	for j in range(0, nbRepet) :
		covMat.FieldsInitialization()

		start = time.time()
		covMat.Invsqrtm()
		tpsCovMat[i] += time.time() - start
		PrintProgress(round((i*nbRepet + j)*100/(nbRepet * len(size)), 2))

PrintProgress(100)

for i in range(0, len(size)) :
	tpsCovMat[i] /= nbRepet
	print("CovMat size : " + str(size[i]) + "x" + str(size[i]) + "	speed up : " + str(tpsCovMat[i]) + " sec") 