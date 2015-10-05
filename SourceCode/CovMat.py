#!/usr/bin/python
 
import Environment
import numpy
import scipy.linalg

class CovMat :
	# ----------------------------------------------------------------------------------- #
	# ------------------------------- COVMAT CONSTRUCTORS ------------------------------- #
	# ----------------------------------------------------------------------------------- #

	def __init__(self, arg, memorySafeState = Environment.memorySafeState) :
		if (isinstance(arg, int)) :																	#arg is an it
			self.matrixOrder = arg																	#alloc memory only. matrix isn't sym def pos (use randomise() function fot it)
			self.matrix = self.MatrixFromArray(numpy.array((arg, arg)))
			self.FieldsInitialization()
		elif (isinstance(arg, numpy.ndarray)) :														#arg is an ndarray
			self.matrix = self.MatrixFromArray(arg, memorySafeState)										#map an ndarray into a matrix array
			self.matrixOrder = arg.shape[0]
			self.FieldsInitialization()
		elif (isinstance(arg, numpy.matrix)) :														#arg is a matrix
			self.matrix = self.MatrixFromArray(arg, memorySafeState)
			self.matrixOrder = arg.shape[0]
			self.FieldsInitialization()



	@staticmethod
	def MatrixFromArray(numpyArray, memorySafeState = False) :
		return numpy.matrix(numpyArray, Environment.dataType, memorySafeState)



	@staticmethod
	def Zero(matrixOrder) :
		return CovMat(numpy.zeros((matrixOrder, matrixOrder)), False)



	@staticmethod
	def Identity(matrixOrder) :
		return CovMat(numpy.eye(matrixOrder), False)



	@staticmethod
	def Random(matrixOrder) :
		covMat = CovMat(matrixOrder)
		covMat.Randomize()

		return covMat



	def FieldsInitialization(self) :
		self.eigenValues = None
		self.eigenVectors = None
		self.norm = None
		self.determinant = None
		self.inverse = None
		self.sqrtm = None
		self.invsqrtm = None
		self.expm = None
		self.logm = None
		self.powm = None
		self.power = 1



	# ----------------------------------------------------------------------- #
	# ------------------------------- GETTERS ------------------------------- #
	# ----------------------------------------------------------------------- #

	def GetMatrix(self) :
		return self.matrix



	def GetMatrixOrder(self) :
		return self.matrixOrder



	def GetEigenValues(self) :
		if (self.eigenValues is not None) :
			return self.eigenValues
			
		self.ComputeEigen(true)
		return self.eigenValues



	def GetEigenVectors(self) :
		if (self.eigenVectors is not None) :
			return self.eigenVectors
			
		self.ComputeEigen()
		return self.eigenVectors



	def GetEigenVectorsTranspose(self) :
		if (self.eigenVectorsTranspose is not None) :
			return self.eigenVectorsTranspose
			
		self.ComputeEigen()
		return self.eigenVectorsTranspose



	# ------------------------------------------------------------------------------ #
	# ------------------------------- USUAL FUNCTIONS ------------------------------- #
	# ------------------------------------------------------------------------------ #

	def Fill(self, value) :
		self.matrix.fill(value)
		self.FieldsInitialization()



	def Randomize(self) :
		tmp = numpy.random.rand(self.matrixOrder, self.matrixOrder)
		self.matrix = self.MatrixFromArray(numpy.dot(tmp, numpy.transpose(tmp))/100)
		self.FieldsInitialization()



	def Diagonal(self, offset = 0) :
		return self.matrix.diagonal(offset)



	def Column(self, i) :
		return self.matrix[:, i]



	def Row(self, i) :
		return self.matrix[i, :]



	def Maximum(self, axis = None) :
		return self.matrix.max(axis)



	def Minimum(self, axis = None) :
		return self.matrix.min(axis)



	def Mean(self, axis = None) :
		return self.matrix.mean(axis)



	def Variance(self, axis = None) :
		return self.matrix.var(axis)



	def Sum(self, axis = None) :
		return self.matrix.sum(axis)



	def Product(self, axis = None) :
		return self.matrix.prod(axis)



	def Norm(self) :
		if (self.norm is not None) :
			return self.norm

		self.norm = numpy.linalg.norm(self.matrix)
		return self.norm



	def Determinant(self) :
		if (self.determinant is not None) :
			return self.determinant

		self.determinant = numpy.linalg.det(self.matrix)
		return self.determinant



	def Transpose (self) :
		return self



	def Inverse(self) :
		if (self.inverse is not None) :
			return self.inverse

		self.inverse = CovMat(numpy.linalg.inv(self.matrix))
		return self.inverse



	def ComputeEigen(self, eigenValuesOnly = False) :
		if ((self.eigenValues is not None)&(self.eigenVectors is not None)) :
			return
		
		if (eigenValuesOnly) :
			if (self.eigenValues is not None) :
				return

			self.eigenValues = numpy.linalg.eigvalsh(self.matrix)
		else :
			self.eigenValues, self.eigenVectors = numpy.linalg.eigh(self.matrix)
			self.eigenVectors = self.MatrixFromArray(self.eigenVectors)
			self.eigenVectorsTranspose = self.eigenVectors.transpose()



	def Sqrtm (self) :
		if (self.sqrtm is not None) :
			return self.sqrtm

		self.ComputeEigen()
		self.sqrtm = CovMat(self.eigenVectors * self.MatrixFromArray(numpy.diag(numpy.sqrt(self.eigenValues))) * self.eigenVectorsTranspose)
		return self.sqrtm



	def Invsqrtm (self) :
		if (self.invsqrtm is not None) :
			return self.invsqrtm

		self.ComputeEigen()
		self.invsqrtm = CovMat(self.eigenVectors * self.MatrixFromArray(numpy.diag(1.0/numpy.sqrt(self.eigenValues))) * self.eigenVectorsTranspose)
		return self.invsqrtm



	def Expm (self) :
		if (self.expm is not None) :
			return self.expm

		self.ComputeEigen()
		self.expm = CovMat(self.eigenVectors * self.MatrixFromArray(numpy.diag(numpy.exp(self.eigenValues))) * self.eigenVectorsTranspose)
		return self.expm



	def Logm (self) :
		if (self.logm is not None) :
			return self.logm

		self.ComputeEigen()
		self.logm = CovMat(self.eigenVectors * self.MatrixFromArray(numpy.diag(numpy.log(self.eigenValues))) * self.eigenVectorsTranspose)
		return self.logm



	def Powm (self, power) :
		if (power == 1) :
			return self

		if (self.power == power) :
			return self.powm

		self.ComputeEigen()
		self.powm = CovMat(self.eigenVectors * self.MatrixFromArray(numpy.diag(self.eigenValues**power)) * self.eigenVectorsTranspose)
		self.power = power
		return self.powm



	@staticmethod
	def SolveProblem(covMat1, covMat2) :
		return scipy.linalg.eigvalsh(covMat1.matrix, covMat2.matrix)



	# ------------------------------------------------------------------------- #
	# ------------------------------- OPERATORS ------------------------------- #
	# ------------------------------------------------------------------------- #

	def __str__(self) :
		return str(self.matrix)



	def __call__(self, x, y) :
		return self.matrix[x, y]



	def __add__(self, arg) :
		if (isinstance(arg, CovMat)) :
			return CovMat(self.matrix + arg.matrix)
		else :
			return CovMat(self.matrix + arg)



	def __radd__(self, arg) :
		return self.__add__(arg)



	def __iadd__(self, arg) :
		if (isinstance(arg, CovMat)) :
			self.matrix += arg.matrix
		else :
			self.matrix += arg

		self.FieldsInitialization()
		return self



	def __sub__(self, arg) :
		if (isinstance(arg, CovMat)) :
			return CovMat(self.matrix - arg.matrix)
		else :
			return CovMat(self.matrix - arg)



	def __rsub__(self, arg) :
		return CovMat(-1 * self.matrix + arg.matrix)



	def __isub__(self, arg) :
		if (isinstance(arg, CovMat)) :
			self.matrix -= arg.matrix
		else :
			self.matrix -= arg

		self.FieldsInitialization()
		return self



	def __mul__(self, arg) :
		if (isinstance(arg, CovMat)) :
			return CovMat(self.matrix * arg.matrix)
		else :
			return CovMat(self.matrix * arg)



	def __rmul__(self, arg) :
		return self.__mul__(arg)



	def __imul__(self, arg) :
		if (isinstance(arg, CovMat)) :
			self = CovMat(self.matrix * arg.matrix)
		else :
			self = CovMat(self.matrix * arg)

		self.FieldsInitialization()
		return self



	@staticmethod
	def ElementWiseProduct (covMat1, covMat2) :
		return self.MatrixFromArray(numpy.multiply(covMat1, covMat2))



	def __truediv__(self, arg) :
		return CovMat(self.matrix / arg)



	def __rtruediv__(self, arg) :
		return CovMat(arg / self.matrix)



	def __itruediv__(self, arg) :
		self.matrix /= arg
		self.FieldsInitialization()
		return self



	def __pow__(self, arg) :
		return self.Powm(arg)



	def __ipow__(self, arg) :
		self = self.Powm(arg)
		return self
