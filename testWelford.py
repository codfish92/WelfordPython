#This is a script to test the welford objects, it does an 8, 100, 1000 size sample. Keep in mind that the covariance calculation could be off on the 8 sample, but this error should become neglabile with the 100 and 1000 size samples.
#uses 1e-10 as an acceptable tolerance. 

import random
import welford

random.seed(1) #this will ensure random, but reproducable results

sample8 = []
sample100 = []
sample1000 = []
for i in range(0, 8):
	sample8.append(random.uniform(0, 100))

for i in range(0, 100):
	sample100.append(random.uniform(0, 100))

for i in range(0, 1000):
	sample1000.append(random.uniform(0, 100))

if len(sample8) != 8 or len(sample100) != 100 or len(sample1000) != 1000:
	print "Samples not created properly, aborting"
	exit(1)

x = welford.Welford(0) #intiate welford with 0 lag

def testBasicSample(sample, welfordObject): #runs basic tests on mean, variance, and number of points
	welfordObject.reset() #re intilize welford
	mean = 0
	variance = 0
	numPoints = 0
	temp = 0
	for i in range(0, len(sample)):
		#add to welford
		welfordObject.addData(sample[i])
		#old way
		temp = temp + sample[i]
		numPoints = numPoints + 1
	mean = temp/float(numPoints)
	temp = 0
	for i in range(0, len(sample)):
		temp = temp + (sample[i] - mean)**2
	variance = temp/float(numPoints)
	print "Welford object has:"
	welfordObject.showStats()
	print "\n2 pass got:\nMean %f\nVaraince %f\nNumber of points %i" % (mean, variance, numPoints)
	if abs(welfordObject.getMean() - mean)>1e-10 or abs(welfordObject.getVariance() - variance) > 1e-10 or welfordObject.geti() != numPoints:
		print "Warning Mismatch\n;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
		if welfordObject.getMean() != mean:
			print "it was mean"
		elif welfordObject.getVariance() != variance:
			print "it was variance"
		else:
			print "it was points"

testBasicSample(sample8, x)
print ""
testBasicSample(sample100, x)
print ""
testBasicSample(sample1000, x)
