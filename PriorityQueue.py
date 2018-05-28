from bisect import insort

class PriorityQueue():
	 def __init__(self):
	 	self.PQ = []

	 def add(self, element):
	 	insort(self.PQ, element)

	 def remove(self):
	 	if self.size() > 0:
	 		return self.PQ.pop()
	 	else:
	 		return False

	 def size(self):
	 	return len(self.PQ)
