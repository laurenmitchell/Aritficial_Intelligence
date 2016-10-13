import random

def simulatedAnnealing:
	s = 1
	T = 100
	tMin = 0.000001 
	alpha = 0.9
	deltaE = 0
	while T > tMin:
		while deltaE:
			ss = random(s)
			