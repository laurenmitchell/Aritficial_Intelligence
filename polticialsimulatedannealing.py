#politicalDistrcits 
#simulated annealing 

import sys
import copy
import random
from math import exp

dataDistricts = []
dataHouses = []
txtfilename = sys.argv[-1]

district1 = []
district2 = []
district3 = []
district4 = []
district5 = []
district6 = []
district7 = []
district8 = []
district9 = []
district10 = []

totalRcount = 0 
totalDcount = 0
Rcount = 0
Dcount = 0 





with open(txtfilename, "r") as f:
	for line in f:
		line = line.strip()
		if len(line) > 0:
			dataHouses.append(map(str, line.split()))	
		totalRcount = sum(x.count("R") for x in data)
		totalDcount = sum(x.count("D") for x in data)
		print "Total R Count:", totalRcount/100,"%"
		print "Total D Count:", totalDcount/100,"%"
		
if len(dataHouses) == 8:
	for i in range(8):
		district = []
		for j in range (8):
			district.append((i,j))
		dataDistricts.append(district)
elif len(dataHouses) == 10:
	for i in range(10):
		district = []
		for j in range (10):
			district.append((i,j))
		dataDistricts.append(district)

#print dataDistricts

#check the size of district number of members 
def costFunc(solution):
	district_r = 0
	district_d = 0
	for arr in solution:
		count = 0
		for c in arr:
			if dataHouses[c[0]][c[1]] == 'R':
				count += 1
			else:
				count -= 1
		if count < 0:
			district_d += 1
		elif count > 0:
			district_r +=1

	#print ("R districts:"), district_r
	#print ("D districts:"), district_d
	if district_d != 0:
		fitness = abs(1-(district_r *1.0 / district_d))
	elif district_r !=0:
		fitness = abs(1-(district_d *1.0 / district_r))		
		
	else: 
		fitness = 0 

	#print fitness
	return fitness
	#print(fitness)



def newsolution(dataDistricts):
	firstdist = random.randint(0, len(dataHouses)-1)
	#d0 = random.choice(dataDistricts[firstdist])
	randomnum = random.randint(0,len(dataHouses)-1)
	d0 = dataDistricts[firstdist][randomnum]
	findneighbor = random.choice(getneighbors(d0[0],d0[1]))
	counter = 0
	for d in dataDistricts:
		if findneighbor in d:
			break
		counter += 1
	#print findneighbor
	#print dataDistricts
	var = dataDistricts[counter].index(findneighbor)
	dataDistricts[counter][var] = d0
	dataDistricts[firstdist][randomnum] = findneighbor
	

		#print dataDistricts
	# elif len(dataHouses) == 10:
	# 	firstdist = random.randint(0,9)
	# 	d0 = random.choice(dataDistricts[firstdist])
	# 	dataDistricts[firstdist].remove(d0)
	# 	seconddist = random.randint(0,9) 
	# 	d1 = random.choice(dataDistricts[seconddist])
	# 	dataDistricts[seconddist].remove(d1)
	# 	dataDistricts[seconddist].append(d1)
	# 	dataDistricts[firstdist].append(d0)

	return dataDistricts


	#if fitness != 0.0:

		#generate a new solution. 
		#pick two random houses and swap them 


#checking the neighbor of swapped nodes 

def getneighbors(nodex,nodey):
	neighbors = []
	if (nodex - 1) <= 7 and (nodex - 1) >= 0:
		neighbors.append(((nodex -1), nodey))
	if (nodey - 1) <= 7 and nodey - 1 >= 0:
		neighbors.append((nodex, (nodey -1)))
	if ((nodex - 1 <= 7 and nodey -1 <= 7 )) and ((nodex -1 >= 0 and nodey -1 >= 0)):
		neighbors.append((nodex-1, nodey-1))
	if (nodex + 1) <= 7 and nodex + 1 >= 0:
		neighbors.append(((nodex + 1), nodey))
	if nodey + 1 <= 7 and nodey + 1 >= 0:
		neighbors.append((nodex, nodey+1))
	if (nodex + 1 <=7 and nodey + 1 <=7) and (nodex  + 1 >= 0 and nodey + 1 >=0 ) :
		neighbors.append((nodex + 1, nodey + 1))
	if (nodex + 1 <= 7 and nodey - 1 <= 7) and (nodex +1 >=0 and nodey -1 >=0):
		neighbors.append((nodex +1, nodey -1))
	if (nodex - 1 <=7 and nodey + 1 <=7 )  and (nodex -1 >=0  and nodey + 1 >=0):
		neighbors.append((nodex -1 , nodey + 1))
	return neighbors

# [i-1][j]
# [i][j-1]
# [i-1][j-1]
# [i+1][j]
# [i][j+1]
# [i+1][j+1]
# [i+1][j-1]
# [i-1][j+1]


#dfs search
def validateDistrict(district, neighbor_dict):
	for v in district:
		Neighborfound = False
		for u in district:
			if u in neighbor_dict[v]:
				Neighborfound = True
		if not Neighborfound:
			return False
	return True

dict_dist = {}
def checksolution():
	for d in dataDistricts:
		for h in d:
			dict_dist[h] = getneighbors(h[0],h[1])
		validateDistrict(d[0], dict_dist)

#check to make sure all nodes are visited, otherwise district is invalid



# print data
# print Rcount
# print Dcount

def acceptance_probability(old_fitness, new_fitness, K, T):
	if new_fitness < old_fitness:
		return 1

	else:
		exp((new_fitness - old_fitness)/(K*T))
		#print new_fitness, old_fitness, K, T

def simulatedAnnealing(solution):
	old_fitness = costFunc(solution)
	Tmax = 10000
	T = Tmax
	Tmin = 0.01
	alpha = 0.9 
	K = 10
	while T > Tmin:
		i = 1
		while i <= 100:
			new_solution = newsolution(solution)
			new_fitness = costFunc(new_solution)
			probability = acceptance_probability(old_fitness, new_fitness, K, T)
			if probability > random.random():
				solution = new_solution
				old_fitness = new_fitness
			i += 1 
		T = T * alpha
 		#print solution
 	print solution, old_fitness
	return solution, old_fitness

simulatedAnnealing(dataDistricts)
