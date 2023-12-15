import numpy as np
import pandas as pd
import networkx as nx
import csv
import random
import matplotlib.pyplot as plt

# read in data into a numpy array
file = open('surveyResponses.csv')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
data = np.array(rows)

# makes empty graph
G = nx.Graph()
G_noWeights = nx.Graph()

# define index for each connection type
connectionTypes = ["Zee Group/Orientation", "Class", "Academic/Career-focused Club", "Athletic Club/Team","Other Type of Club", "Mutual Friend", "Party/Social Event", "Professional Event/Program/Internship", "High School", "Other"]
conTypesCount = np.full(10, 0)

# type of search
searchType = input("Type 1 to search path, type 2 to graph, type 3 to draw the connections of one person: ")

# search shortest path between two people
if searchType == "1":
  source = input("\nEnter source name: ")
  destination = input("\nEnter destination name: ")
  for i in range(1, len(data)):
    sourceName = data[i][1]
    if data[i][2] == '2026':
      for j in range(3, len(data[0]), 2):
        toName = data[i][j]
        toConnection = data[i][j+1]
      
        # if not empty toConnection
        if len(toConnection) != 0:
          G.add_edge(sourceName, toName, weight=connectionTypes.index(toConnection))
          G_noWeights.add_edge(sourceName, toName)
          conTypesCount[connectionTypes.index(toConnection)] += 1
          

  # get shortest path between two people
  path = nx.shortest_path(G_noWeights, source, destination)
  edge = []

  # collect edges of each path
  for i in range(len(path) - 1):
    edge.append(G.get_edge_data(path[i], path[i+1]))
  edgeString = str(edge)

  for i in range(len(path) - 1):
    print(path[i])
    print(connectionTypes[edge[i].get("weight")])
  print(path[len(path) - 1])


  ## draw graph
  # fig = plt.figure(figsize=(12,12))
  edge_nodes = set(G)
  # Ensures the nodes around the circle are evenly distributed
  pos = nx.circular_layout(G.subgraph(edge_nodes))

  for i in G.nodes:
    pos[i] = np.array([random.randrange(200), random.randrange(200)])

  nx.draw(G, pos, with_labels=True, node_size = 7, font_size=6, width = 1, edge_color = (0.1, 0.1, 0.1, 0.1))

  plt.savefig("Graph.png", format="PNG")
  plt.show()




###
# draw graph os a specific connection type
elif searchType == "1":
  requestConnection = input("\nType of the number corresponding to the connection type you want to see \n1: All\n2: Zee Group/Orientation\n3: Class\n4: Academic/Career-focused Club\n5: Athletic Club/Team\n6: Other Type of Club\n7: Mutual Friend\n8: Party/Social Event\n9: Professional Event/Program/Internship\n10: High School\n11: Other\n")
  requestConnection = int(requestConnection) # degrees = input("\nNumber of Degrees you want to display: ")
  print(requestConnection)
  ## populates the weighted and unweighted graph
  i = 1
  for i in range(1, len(data)):
    sourceName = data[i][1]
    if data[i][2] == '2026':
      for j in range(3, len(data[0]), 2):
        toName = data[i][j]
        toConnection = data[i][j+1]
      
        # specific type
        if requestConnection != 1:
          if len(toConnection) != 0 and connectionTypes.index(toConnection) == requestConnection - 2:
            G.add_edge(sourceName, toName, weight=connectionTypes.index(toConnection))
            G_noWeights.add_edge(sourceName, toName)
            conTypesCount[connectionTypes.index(toConnection)] += 1
        else: # add all
          if len(toConnection) != 0:
            G.add_edge(sourceName, toName, weight=connectionTypes.index(toConnection))
            G_noWeights.add_edge(sourceName, toName)
            conTypesCount[connectionTypes.index(toConnection)] += 1
          

  ## draw graph
  edge_nodes = set(G)
  # Ensures the nodes around the circle are evenly distributed
  pos = nx.circular_layout(G.subgraph(edge_nodes))

  for i in G.nodes:
    pos[i] = np.array([random.randrange(200), random.randrange(200)])

  nx.draw(G, pos, with_labels=True, node_size = 7, font_size=6, width = 1, edge_color = (0.1, 0.1, 0.1, 0.1))

  plt.savefig("Graph.png", format="PNG")
  plt.show()




###
# Shows connection of one person
else:
  source = input("\nEnter source name: ")
  for i in range(1, len(data)):
    sourceName = data[i][1]
    if data[i][2] == '2026':
      for j in range(3, len(data[0]), 2):
        toName = data[i][j]
        toConnection = data[i][j+1]
      
        # if not empty toConnection
        if len(toConnection) != 0 and sourceName == source or toName == source:
          G.add_edge(sourceName, toName, weight=connectionTypes.index(toConnection))
          G_noWeights.add_edge(sourceName, toName)
          conTypesCount[connectionTypes.index(toConnection)] += 1

  edge_nodes = set(G)
  # Ensures the nodes around the circle are evenly distributed
  pos = nx.circular_layout(G.subgraph(edge_nodes))

  for i in G.nodes:
    pos[i] = np.array([random.randrange(200), random.randrange(200)])

  nx.draw(G, pos, with_labels=True, node_size = 7, font_size=6, width = 1, edge_color = (0.1, 0.1, 0.1, 0.1))

  plt.savefig("Graph.png", format="PNG")
  plt.show()