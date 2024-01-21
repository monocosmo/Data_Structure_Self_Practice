'''
178. Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Notice
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

class Solution:
  """
  @param n: An integer
  @param edges: a list of undirected edges
  @return: true if it's a valid tree, or false
  """
  # get nodes from edges
  def getNodes(self, n, edges):
    # use dictionary to store nodes
    nodesDic = {}
    for i in range(n):
      nodesDic[i] = set()

    for edge in edges:
      # one edge has two end nodes
      u = edges[0]
      v = edges[1]
      nodesDic[u].add(v)
      nodesDic[v].add(u)

    return nodesDic

  def validTree(self, n, edges):
    if n == 1:
      return True
    
    # 1. tree has n - 1 edges
    if(len(edges) != n -1):
      return False

    # get nodes
    graphNodes = self.getNodes(n, edges)

    # BFS to traverse the nodes in the graph
    queue = []
    visisted = set()
    queue.append(0) # start from Node 0
    visisted.add(0)
    while(len(queue) > 0):
      node = queue.pop(0)
      for neighbor in graphNodes[node]:
        if neighbor in visisted:
          continue
        queue.append(neighbor)
        visisted.add(neighbor)

    # 2. tree can be traversed by BFS
    return(len(visisted) == n)

