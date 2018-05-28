class Queue():
	 def __init__(self):
	 	self.Q = []

	 def add(self, element):
	 	self.Q.append(element)

	 def remove(self):
	 	if self.size() > 0:
	 		return self.Q.pop(0)
	 	else:
	 		return False

	 def size(self):
	 	return len(self.Q)

