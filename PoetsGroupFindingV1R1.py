########################################################################################################################################################
# This small Python project was designed to find the friend-communication-groups for Poets in Tang Dynasty of China under the Harvard CBDB Work Group.
# 
# Three classical algorithms are used in this piece of code: Binary-search, minimum spanning trees, and depth-first-search. 
# Some code segments are obtained from public source with little modification. 
#
# The code is posted for public academic use as it is. The programmer/or Harvard CBDB takes no responsibility for any concerns regarding to the code.
# 
# Contact with the Harvard CBDB Work Group for database format issue. 
# The code was written by Dr. Li Chen (lchen@udc.edu) at the University of the District of Columbia.
# 
# 
# Version 1, revision 1.
# 7/25/2021
#   
#########################################################################################################################################################


import pandas as pd
import numpy as np
import math

#to plot within notebook
import matplotlib.pyplot as plt

#read the file
nodes = pd.read_csv('nodes.csv')
edges = pd.read_csv('edges.csv')

f100=nodes.iloc[0:1000,:]
print("nodes length:",len(nodes))

nd_id=nodes.iloc[:,0]
nd_name=nodes.iloc[:,1]

ed=[[edges.iloc[i,0],edges.iloc[i,1],edges.iloc[i,2]] for i in range(len(edges))]

print("nd_id\n", nd_id)
print("nd_name\n", nd_name)

#print("ed\n",ed)

"""x= np.zeros(len( f100 ))  
for i in range(len( dat2015 )):
    if isinstance(dat2015[i],float):
        x[i] = dat2015[i]
    else:
        x[i] = -1

"""
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph
 
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
   
    # function to add an edge with weight to graph
    def addEdge(self, ew):
        self.graph.append(ew)
     
    """# A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])"""

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if i< self.V:
            if parent[i] == i:
                return i
        else:
            print("error i=",i)
            return 0
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):
 
        result = []  # This will store the resultant MST
         
        # An index variable, used for sorted edges
        i = 0
         
        # An index variable, used for result[]
        e = 0
 
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
       
        """self.graph = sorted(self.graph,
                            key=lambda item: item[2])  
        
        reverse=True"""

        self.graph = sorted(self.graph,
                            key=lambda item: item[2],reverse=True) 
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            if weight>2: # Lee Added 
                print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)
        return result;

#This algorithm uses absolute index for vetices. i.e. 1,2,3,4,5,6,... 
#Need to re-arrange the vertices and edges

newV=[]
iNewV=[]
for i in range(len(nd_id)):
    newV.append(i)
    iNewV.append([i,nd_id[i]])




#Binary search using bisect_left
# need to use binary search for speeding-up to reset the index for
# vertices. 

from bisect import bisect_left
def binary_search(arr, x, lo=0, hi=None):
    if hi is None: hi = len(arr)
    pos = bisect_left(arr, x, lo, hi)                  # find insertion position
    return pos if pos != hi and arr[pos] == x else -1  # don't walk off the end

# if  binary_search(a, x)==-1 meaning not found 
# first need to split edge set into the first vertex (first,second)
# the list of first vertices is sorted.    
ed_first=[e[0] for e in ed]

print("ed :   ",ed[1:200]) # check if it is correct
print("ed_first :   ",ed_first[1:200]) # check if it is correct




print("newV",newV[0:10])
#nd_id[i] is the real index of newNode i in dictionary   



 
# Change newEdge based on newV
newEdge=[]
found = 0
k=0

##########################The following code is too slow  9 minutes ##########
"""for e in  ed:
      found=0
      k=k+1
      print("e :==", k )
      for i in range(len(newV)):
         if  e[0] == nd_id[i] and found==0:
           for j in range(len(newV)):
              if  e[1] == nd_id[j] :
                 newEdge.append([i, j, e[2]])
                 found=1

"""
##########################change to binary search for frist index "vertices" ##########
for e in  ed:
      found=0
      k=k+1
      print("e :==", k )
      i=binary_search(nd_id, e[0])
      if(i != -1 and found==0):  # it is a vertex in nodes then we need to find the second index
           for j in range(len(newV)):
              if  e[1] == nd_id[j] :
                 newEdge.append([i, j, e[2]])
                 found=1



g1TangShi=Graph(len(nd_id))
for ew in newEdge:
      g1TangShi.addEdge(ew)

# add more edges to make the graph to be connected
# If multipe extra edges exist, the algorithm will not pickup it
# 
for nT in range(1,len(newV)):
    g1TangShi.addEdge([0,nT,0])

MSTEdges=g1TangShi.KruskalMST() 

# export data to two sets

df = pd.DataFrame(MSTEdges, columns= ['id1','id2', 'wight'])

df.to_csv (r'exportMST.csv', index = False, header=True)


MSTEdgesPlus=[]
for e in MSTEdges:
   MSTEdgesPlus.append([e[0],nd_id[e[0]],nd_name[e[0]],e[1],nd_id[e[1]],nd_name[e[1]],e[2]])

df2 = pd.DataFrame(MSTEdgesPlus, columns= ['id1','id1Pre','Name1','id2','id2Pre','Name2','wight'])

df2.to_csv (r'exportMSTPlus.csv', index = False, header=True)


# input a person's name to get his/her friend-group by maintaining the minimum Connectivity
# The maxmun # of people in the group is limited by a Limit-Number.


# Extract largest friends-group or friends-cycle with minimum Connectivity # of communications of poems
# Extract first three groups
#  

#Find new graph with minimum edge weight.
def NewGraph(gEdges, minWeight): 
  gNewEdge=[]
  for e in  gEdges:
    if e[2] >= minWeight:
       gNewEdge.append(e)
  return gNewEdge


#put minWeight as the average weight as default 

avgW=0.0
for e in  MSTEdges:
    avgW += e[2] 

if (len(MSTEdges) !=0):
   avgW = avgW/len(MSTEdges);

print("avg weight:",avgW)

graphNew=NewGraph(MSTEdges, avgW)

#Find all Connected component in this new Graph
#https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/

# Python program to print connected
# components in an undirected graph
# This code is contributed by Abhishek Valsan
 
 
class GraphCC:
 
    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
 
    def DFSUtil(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp
 
    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
 
    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
 
""" 
# Driver Code
if __name__ == "__main__":
 
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)
 
#  """

#Find Connected Components=FriendsGroups 
ccGraph = GraphCC(len(newV))

for e in graphNew: # new edges
  ccGraph.addEdge(e[0], e[1]) 

FriendsGroups = ccGraph.connectedComponents()

print("Friends' groups", FriendsGroups)

#TEST FILE WRITING
import csv

a_dict = {"a": [1,"S"], "b": [2], "c": [3,6,7]}

csv_file = open("csv_file.csv", "w")
writer = csv.writer(csv_file)
#writer=pd.write_csv(csv_file.csv)
for key, value in a_dict.items():
    writer.writerow([key, value])
csv_file.close()

"""
def add_element(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)

d = {}
add_element(d, 'foo', 'val1')
add_element(d, 'foo', 'val2')
add_element(d, 'bar', 'val3')
"""
def add_element(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)

ccDict = {}
i=0
for ele in FriendsGroups:
   if len(ele) >1:  # do not record any group having 1 person 
     add_element(ccDict,str(i), ele)
     i +=1




ccDict = {}
i=0
for ele in FriendsGroups:
   if len(ele) >1:  # do not record any group having 1 person 
     add_element(ccDict,str(i), ele)
     i +=1
     
     
#------------------

fgFile = open("FriendGroups.csv", "w")
writer = csv.writer(fgFile)
#writer=pd.write_csv(csv_file.csv)
for key, value in ccDict.items():
    writer.writerow([key, value])
fgFile.close()

#---------------------
# Add Real and id to FriendGroups
ccDictWithName=ccDict

for key in ccDictWithName:
    tempList=[]
   # print(key)
    vList=ccDictWithName[key][0]
  #  print (vList)
  #  print (len(vList))
    for i in range(0,len(vList)):
       tempList.append(nd_name[vList[i]])
   # print (tempList)
    ccDictWithName[key].append(tempList)
    
#--------------------------

fgFile = open("FriendGroups5WithName.csv", "w")
writer = csv.writer(fgFile)
#writer=pd.write_csv(csv_file.csv)
for key, value in ccDictWithName.items():
    writer.writerow([key, value])
fgFile.close()  


######### 7/25/ Working Version ## 8 communication based

# Search for the FriendGroup of a specific "ShiRen" 
# The purpose is to find the group #

print(ccDictWithName.items())

ShiRenName1 ="白居易"
ShiRenName2 ="杜甫"
ShiRenName3 ="孟浩然" 


#----search function not optimized 
def searchForShiRen(shiRen):
  newIndex=-1
  for i in range(len(newV)):
    if  shiRen == nd_name[i]:  # nd_name is listed as the same sequence of new_Nodes
       newIndex=i
       break
  if newIndex==-1:
    print(shiRen," was not in any Communication-Group or did not communicate with others enough.")
    return -1  # not found or not in any group

  iGroup=0
  found=0
  for ele in FriendsGroups:
    if len(ele) >1:  # do not count any group having 1 person 
      for xIndex in ele:
        if newIndex ==xIndex:  # do not record any group having 1 person 
          found = 1
          print(shiRen," is in the Communication-Group: ", iGroup)
          return iGroup
      iGroup +=1
  if found == 0:
    print(shiRen," was not in any Communication-Group or did not communicate with others enough.")
    return -1

#---------------------------
searchForShiRen(ShiRenName1)
searchForShiRen("丘丹")
searchForShiRen("溫庭永")

