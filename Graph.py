from Queue import Queue
from Stack import Stack

class Node:
	def __init__(self, val, weight = 1, dist = 1):
		self.val = val
		self.neighbours = []
		self.weight = weight
		self.dist = dist

class Graph:

	def __init__(self, nodes = []):
		self.nodes = nodes

	def add_node(self, val, weight = 1):
		new_node = Node(val, weight)
		self.nodes.append(new_node)

	def add_edge(self, node_u, node_v):
		node_u.neighbours.append(node_v)

	def BFS(self):
		if len(self.nodes) == 0:
			return []

		root = self.nodes[0]
		visited = set([root])
		Q = Queue()
		Q.add(root)
		BfsResult = []


		while Q.size() > 0:
			QueueHead = Q.remove()
			BfsResult.append(QueueHead)
			for neighbour in QueueHead.neighbours:
				if neighbour not in visited:
					Q.add(neighbour)
					visited.add(neighbour)

		return BfsResult

	def DFS(self):
		if len(self.nodes) == 0:
			return []

		root = self.nodes[0]
		visited = set([root])
		S = Stack()
		S.add(root)
		DfsResult = []


		while S.size() > 0:
			StackTop = S.remove()
			DfsResult.append(StackTop)
			for neighbour in StackTop.neighbours:
				if neighbour not in visited:
					S.add(neighbour)
					visited.add(neighbour)

		return DfsResult