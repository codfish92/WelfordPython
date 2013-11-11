#All class variables are prefixed by a _, this to prevent them from being so eaisly modified by the programer without hopefully throwing some sort of flag. This is primarly because the programer should not need to change any values other than through a series of equations(aka the methods), but the options are available for easy access. 

from __future__ import division

class Welford:
	def __init__(self, lag):
		self._mean = 0.0
		self._ivariance = 0.0
		self._i = 0
		self._debug = False #for debuging statements
		self._lag = lag;
		self._X = [] #list used for holding lagged entries, for auto correlation
		for i in range(lag):
			self._X.append(None)
		self._lastAddedPoint = None #holds previous point for covariance
		self._previousMean = None #holds previous mean for covariance

	#reset this particular welford object
	def reset(self):
		if self._debug:
			print("Reseting mean, ivariance, and i to 0, maintaining lag")
		self._mean = 0.0
		self._ivariance = 0.0
		self._i = 0
		self._X = [] #list used for holding lagged entries, for auto correlation
		self._W = [] #list used for holding the autocorrelation lags.
		for i in range(lag):
			self._X.append(None)
		self._lastAddedPoint = None #holds previous point for covariance
		self._previousMean = None #holds previous mean for covariance

	#will update the mean, ivaraince, and i according to the welford equations.
	def addData(self, data):
		if self._debug:
			print("Adding data point %f to welfordObject" % (data))
		#update number of points
		self._i = self._i+1 

		#update mean and variance
		self._previousMean = self._mean #for use in covariance equation
		self._mean = self._previousMean + (data - self._previousMean)/float(self._i) #typecast self.i to float to ensure floating point division at all times
		self._ivariance = self._ivariance + ((self._i-1)/float(self._i))*(data-self._previousMean)**2 #typecast self.i to ensure floating point division at all times.

		#update the last added point
		self._lastAddedPoint = data
	

		if self._i > 1: #if there is a pair of correlation to calculate
			if self._i < self._lag:
				for j in range(0, i):
					self._W[j] = self._W[j] + ((self._i-1)/self._1)*(self._lastAddedPoint - self._previousMean)(self._X[(self._i-j) %self._lag] -self._previousMean)
			else:
				for j in range(0, self._lag):
					self._W[j] = self._W[j] + ((self._i-1)/self._1)*(self._lastAddedPoint - self._previousMean)(self._X[(self._i-j) %self._lag] -self._previousMean)
		
		#add data to laged list
		self._X[self._i%self._lag] = data

		if self._debug:
			print("Mean is now %f\niVariance is now %f\ni is now %i" % (self._mean, self._ivariance, self._i))
		

	#returns the variance, not the i*variance
	def getVariance(self):
		if self._debug:
			print("Returning the ivariance/(i-1), resulting in variance")
		#
		"""
		The mean and variance are intilized to 0 for convience, so this method will return None if there are no points in the object, instead of returning a 0.
		This is incase there is a set of points where the mean or variance is 0, the user will not have to wonder if thoses values are actually 0 or just freshely instantieated.
		variance does not exist if there is only one point.
		"""
		if self._i <= 1:
			return None
		else:
			return self._ivariance/(float(self._i) )
	
	#returns the mean, the user could also just call self.mean
	def getMean(self):
		if self._debug:
			print("Returning the mean")

		#See variance method for explation of this check
		if self._i: 
			return self._mean
		else:
			return None		

	#returns i
	def getNumberOfPoints(self):
		if self._debug:
			print("Returning the number of points used in welford object aka i")
		return self._i

	#for convinence, since number of points is refered to as i everywhere else
	def geti(self):
		return self.getNumberOfPoints()

	#incase user wants access to ivariance
	def getiVariance(self):
		if self._debug:
			print("Returing the ivariance, not the actual variance")
		if self._i <= 1:
			return None
		else:
			return self._ivariance

	def getLag(self):
		#no debug statement, should be very simple
		return self._lag

	def setDebug(self, debug):
		if self._debug:
			print("Setting the debug flag to %b" % (debug))
		self._debug = debug


	#print the stats
	def showStats(self):
		print("Mean: %f\nvariance: %f\nNumber of points(i): %f" % (self._mean, self.getVariance(), self._i))
		#method is self explanitory, shouldn't need to debug explain it.

