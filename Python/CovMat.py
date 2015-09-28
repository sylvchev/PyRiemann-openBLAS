#!/usr/bin/python
 
import numpy

class CovMat :
	def __init__(self, arg) :
		if (isinstance(arg, int)) : 														#arg is an int
			self.matrix = numpy.matrix(numpy.array((arg, arg)), numpy.dtype('d'), False)
			self.matrixOrder = arg
			self.FieldsInitialization()
		elif (isinstance(arg, numpy.ndarray)) :												#arg is an ndarray
			self.matrix = numpy.matrix(arg, numpy.dtype('d'), False)
			self.matrixOrder = arg.shape[0]
			self.FieldsInitialization()
		elif (isinstance(arg, numpy.matrix)) :												#arg is a matrix
			self.matrix = arg
			self.matrixOrder = arg.shape[0]
			self.FieldsInitialization()



	def NumpyMatrix(self) :
		return self.matrix



	def MatrixOrder(self) :
		return self.matrixOrder



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



	def SetToZero(self) :
		self.matrix = numpy.matrix(numpy.zeros(self.matrixOrder, self.matrixOrder), numpy.dtype('d'), False)
		self.FieldsInitialization()



	def Randomize(self) :
		tmp = numpy.random.rand(self.matrixOrder, self.matrixOrder)
		self.matrix = numpy.matrix(numpy.dot(tmp, numpy.transpose(tmp))/100, numpy.dtype('d'), False)
		self.FieldsInitialization()



	def ComputeEigen(self, eigenValuesOnly = False) :
		if ((self.eigenValues is not None)&(self.eigenVectors is not None)) :
			return
		
		if (eigenValuesOnly) :
			if (self.eigenValues is not None) :
				return

			self.eigenValues = numpy.linalg.eigvalsh(self.matrix)
		else :
			self.eigenValues, self.eigenVectors = numpy.linalg.eigh(self.matrix)
			self.eigenVectors = numpy.matrix(self.eigenVectors, numpy.dtype('d'), False)
			self.eigenVectorsTranspose = self.eigenVectors.transpose()



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

		self.inverse = numpy.matrix(numpy.linalg.inv(self.matrix), numpy.dtype('d'), False)
		return self.inverse



	def Sqrtm (self) :
		if (self.sqrtm is not None) :
			return self.sqrtm

		self.ComputeEigen()
		self.sqrtm = CovMat(self.eigenVectors * numpy.matrix(numpy.diag(numpy.sqrt(self.eigenValues)), numpy.dtype('d'), False) * self.eigenVectorsTranspose)
		return self.sqrtm



	def Invsqrtm (self) :
		if (self.invsqrtm is not None) :
			return self.invsqrtm

		self.ComputeEigen()
		self.invsqrtm = CovMat(self.eigenVectors * numpy.matrix(numpy.diag(1.0/numpy.sqrt(self.eigenValues)), numpy.dtype('d'), False) * self.eigenVectorsTranspose)
		return self.invsqrtm



	def Expm (self) :
		if (self.expm is not None) :
			return self.expm

		self.ComputeEigen()
		self.expm = CovMat(self.eigenVectors * numpy.matrix(numpy.diag(numpy.exp(self.eigenValues)), numpy.dtype('d'), False) * self.eigenVectorsTranspose)
		return self.expm



	def Logm (self) :
		if (self.logm is not None) :
			return self.logm

		self.ComputeEigen()
		self.logm = CovMat(self.eigenVectors * numpy.matrix(numpy.diag(numpy.log(self.eigenValues)), numpy.dtype('d'), False) * self.eigenVectorsTranspose)
		return self.logm



	def Powm (self, power) :
		if (power == 1) :
			return self

		if (self.power == power) :
			return self.powm

		self.ComputeEigen()
		self.powm = CovMat(self.eigenVectors * numpy.matrix(numpy.diag(self.eigenValues)**power, numpy.dtype('d'), False) * self.eigenVectorsTranspose)
		self.power = power
		return self.powm		



	def __str__(self) :
		return str(self.matrix)



	def __call__(self, x, y) :
		return self.matrix[x, y]



	def __add__(self, arg) :
		return CovMat(self.matrix + arg.matrix)



	def __radd__(self, arg) :
		return self.__add__(arg.matrix)



	def __iadd__(self, arg) :
		self.matrix += arg.matrix
		self.FieldsInitialization()
		return self



	def __sub__(self, arg) :
		return CovMat(self.matrix - arg.matrix)



	def __rsub__(self, arg) :
		return CovMat(-1 * self.matrix + arg.matrix)



	def __isub__(self, arg) :
		self.matrix -= arg.matrix
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
