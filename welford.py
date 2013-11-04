#All class variables are prefixed by a __, this to prevent them from being so eaisly modified by the programer without going through methods. This is primarly because the programer should not need to change any values other than through a series of equations(aka the methods). This is pythons way of doing public vs. private.  


class Welford:
	def __init__(self, lag):
		self.__mean = 0.0
		self.__ivariance = 0.0
		self.__i = 0
		self.__debug = False #for debuging statements
		self.__lag = lag;

	#reset this particular welford object
	def reset(self):
		if self.__debug:
			print("Reseting mean, ivariance, and i to 0, maintaining lag")
		self.__mean = 0.0
		self.__ivariance = 0.0
		self.__i = 0

	#will update the mean, ivaraince, and i according to the welford equations.
	def addData(self, data):
		if self.__debug:
			print("Adding data point %f to welfordObject" % (data))
		self.__i = self.i+1
		previousMean = self.__mean #for use in variance equation
		self.__mean = previousMean + (data - previousMean)/float(self.__i) #typecast self.i to float to ensure floating point division at all times
		self.__ivariance = self.__ivariance + (self.__i -1/float(self.__i))*(data-previousMean)**2 #typecast self.i to ensure floating point division at all times.
		if self.__debug:
			print("Mean is now %f\niVariance is now %f\ni is now %i" % (self.__mean, self.__ivaraince, self.__i))

	#returns the variance, not the i*variance
	def getVariance(self):
		if self.__debug:
			print("Returning the ivariance/(i-1), resulting in variance")
		#
		"""
		The mean and variance are intilized to 0 for convience, so this method will return None if there are no points in the object, instead of returning a 0.
		This is incase there is a set of points where the mean or variance is 0, the user will not have to wonder if thoses values are actually 0 or just freshely instantieated.
		variance does not exist if there is only one point.
		"""
		if self.__i <= 1:
			return None
		else:
			return self.__ivariance/(float(self.__i) -1)
	
	#returns the mean, the user could also just call self.mean
	def getMean(self):
		if self.__debug:
			print("Returning the mean")

		#See variance method for explation of this check
		if self.__i: 
			return self.__mean
		else:
			return None		

	#returns i
	def getNumberOfPoints(self):
		if self.__debug:
			print("Returning the number of points used in welford object aka i")
		return self.__i

	#for convinence, since number of points is refered to as i everywhere else
	def geti(self):
		return self.__getNumberOfPoints()

	#incase user wants access to ivariance
	def getiVariance(self):
		if self.__debug:
			print("Returing the ivariance, not the actual variance")
		if self.__i <= 1:
			return None
		else:
			return self.__ivariance

	def getLag(self):
		#no debug statement, should be very simple
		return self.__lag

	def setDebug(self, debug):
		if self.__debug:
			print("Setting the debug flag to %b" % (debug))
		self.__debug = debug


	#print the stats
	def showStats(self):
		print("Mean: %f\ni*variance: %f\nNumber of points(i): %f" % (self.__mean, self.__ivariance, self.__i))
		#method is self explanitory, shouldn't need to debug explain it.

class WelfordCorrelation:
	def __init__(self, Wu, Wv): #Wu and Wv are assumed to be welford objects.
		self.__maxLag = Wu.getLag() #set maxlag
		self.__Wu = Wu
		self.__Wv = Wv

		self.__W = []#intilize lists
		self.__X = []
		if Wv.getLag() > self.__magLag:
			self.__maxLag = Wv.getLag()
		for i in range(0, self.__maxLag):#preallocate space, so all overhead is done before runtime
			self.__W.append(None)
			self.__X.append(None)
		self.__debug = False #for debuging

	def addDataBoth(self, data):
		if self.__debug:
			print("Adding data to both welford objects")

	def addData(self, data, welford):
		if welford == self.__Wu or welford == self.__Wv:
			if self.__debug:
				if welford == self.__Wu:
					print("Adding data to Wu welfrod object")
				else:
					print("Adding data to Wv welford object")
		else:
			print("ERROR: Trying to add data to a welford object not tied to this welford correlation")
			return 
	def setDebug(self, debug):
		if self.__debug:
			print("Setting the debug flag to %b" % (debug))
		self.__debug = debug
	
	def getMaxLag(self):
		return self.__maxLag
