class Welford:
	def __init__(self):
		self.mean = 0.0
		self.ivariance = 0.0
		self.i = 0
		self.debug = False #for debuging statements

	#reset this particular welford object
	def reset(self):
		if self.debug:
			print("Reseting mean, ivariance, and i to 0")
		self.mean = 0.0
		self.ivariance = 0.0
		self.i = 0

	#will update the mean, ivaraince, and i according to the welford equations.
	def addData(self, data):
		if self.debug:
			print("Adding data point %f to welfordObject" % (data))
		self.i = self.i+1
		previousMean = self.mean #for use in variance equation
		self.mean = previousMean + (data - previousMean)/float(self.i) #typecast self.i to float to ensure floating point division at all times
		self.ivariance = self.ivariance + (data - previousMean)*(data - self.mean)
		if self.debug:
			print("Mean is now %f\niVariance is now %f\ni is now %i" % (self.mean, self.ivaraince, self.i))

	#returns the variance, not the i*variance
	def getVariance(self):
		if self.debug:
			print("Returning the ivariance/(i-1), resulting in variance")
		#
		if self.i <= 1:
			return None
		else:
			return self.ivariance/(float(self.i) -1)
	
	#returns the mean, the user could also just call self.mean
	def getMean(self):
		if self.debug:
			print("Returning the mean")
		return self.mean

	#returns i
	def getNumberOfPoints(self):
		if self.debug:
			print("Returning the number of points used in welford object aka i")
		return self.i

	#for convinence, since number of points is refered to as i everywhere else
	def geti(self):
		return self.getNumberOfPoints()

	#incase user wants access to ivariance
	def getiVariance(self):
		if self.debug:
			print("Returing the ivariance, not the actual variance")
		if self.i <= 1:
			return None
		else:
			return self.ivariance

	#print the stats
	def showStats(self):
		print("Mean: %f\ni*variance: %f\nNumber of points(i): %f" % (self.mean, self.ivariance, self.i))

class Welford2Var:
	def __init__(self):
		self.mean = 0
		self.ivariance = 0
		self.i = 0


