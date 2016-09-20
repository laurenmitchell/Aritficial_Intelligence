#!/usr/bin/python
import Queue 

import sys
txtfilename = sys.argv[-1]



class Vertex:
    def __init__(self, value):
        self.id = value
        self.adjacent = {}
        self.solved = False
        self.cost = 0
    
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
        #adds the weight from the two current nodes 

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    def get_neighbors(self):
        return self.adjacent.keys()

class Graph:
    def __init__(self):

        self.graph_dictionary = {}
        self.num_vertices = 0 
        self.Heuristic = {}
        #create an empty dictionary
        #initiatzle total number of vertices 

    def vertices(self):
        #returning all the vertices of graph (keys)
        return list(self.graph_dictionary.keys())
    def edges(self):
        #returning all edges of graph 
        return self.addEdge()

    def addVertex(self, value):
        self.num_vertices = self.num_vertices + 1 
        new_vertex = Vertex(value)
        self.graph_dictionary[value] = new_vertex
        return new_vertex
        
    def getVertex(self, value):
        if value in self.graph_dictionary:
           return self.graph_dictionary[value]
        else:
            return None
    def addEdge(self, start, end, cost = 0):
        if start not in self.graph_dictionary:
            self.addVertex(start)
        if end not in self.graph_dictionary:
            self.addVertex(end)
        self.graph_dictionary[start].add_neighbor(end, cost)
        self.graph_dictionary[end].add_neighbor(start, cost)
    

def aStar(graph, start, end):
    solvedPath = []
    pQueue = Queue.PriorityQueue()
    pQueue.put(start,0)
    previous = {}
    cost = {}
    previous[start] = None
    cost[start] = 0 
    COUNTER = 0

    while not pQueue.empty():
        current = pQueue.get()

        if current == end:
            break 
        for nextNode in graph.graph_dictionary[current].get_neighbors():
            newCost = cost[current] + int(graph.graph_dictionary[current].get_weight(nextNode))
            if nextNode not in cost or newCost < cost[nextNode]:
                cost[nextNode] = newCost
                COUNTER += 1 
                #updating the cost 
                priority = newCost + int(graph.Heuristic[nextNode])
                pQueue.put(nextNode,priority)
                #putting the node and value into the queue 
                previous[nextNode] = current
            #COUNTER += 1 
    solvedPath.append(end)
    final = previous[end]
    solvedPath.append(final)
    while final != start:
        final = previous[final]
        solvedPath.append(final)


    #path = previous[end]
    print "A Star Algorithm:"
    for i in reversed(solvedPath):
        print i
    print "cost:", cost[end]
    print "Number of nodes evaluated:", COUNTER 


def Dijkstra(graph, start, end):
    solved = []
    solvedPath = []
    previous = {}
    previous['S'] = None
    startV = graph.graph_dictionary['S']
    endV = graph.graph_dictionary['F']
    startV.solved = True 
    startV.cost = 0 
    solved.append(startV)
    COUNTER = 0 
    while  endV.solved is not True:
        minCost = 2147483647
        parent = None 
        for s in solved:
            for y in graph.graph_dictionary[s.id].get_neighbors():
                y = graph.graph_dictionary[y]
                if y.solved is not True:
                    newCost = s.cost + int(graph.graph_dictionary[y.id].get_weight(s.id))
                    if newCost < minCost:
                        solvedV = y
                        minCost = newCost
                        parent = s 
                        previous[y.id] = s.id
                        COUNTER += 1
                       
        
        solvedV.cost = minCost
        solvedV.parent = parent
        solvedV.solved = True 
        solved.append(solvedV)

    solvedPath.append('F')
    final = previous['F']
    solvedPath.append(final)
    while final != 'S':
        final = previous[final]
        solvedPath.append(final)

    print "Dijkstra Algorithm:"
    for i in reversed(solvedPath):
        print i
    print "Cost:", endV.cost
    print "Number of nodes evaluated:", COUNTER, "\n"
    




#Graph test 

#if __name__ == '__main__':

g = Graph()

with open(txtfilename, "r") as F:
    state = 0 
    for line in F.readlines():
        if line.isspace():
            state = 1
            continue
        if state == 0:
            commasplit = line.split(",")
            if commasplit[0][1:] not in g.graph_dictionary:
                g.addVertex(commasplit[0][1:])
            if commasplit[1] not in g.graph_dictionary:
                g.addVertex(commasplit[1])

            g.addEdge(commasplit[0][1:], commasplit[1], commasplit[2][:len(commasplit[2])-2])

        if state == 1:
            equalsplit =line.split("=")
            g.Heuristic[equalsplit[0]] = equalsplit[1] 



Dijkstra(g,'S', 'F')
aStar(g,'S','F')
 

