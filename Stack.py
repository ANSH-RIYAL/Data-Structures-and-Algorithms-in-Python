class Stack():
	 def __init__(self):
	 	self.S = []

	 def add(self, element):
	 	self.S.append(element)

	 def remove(self):
	 	if self.size() > 0:
	 		return self.S.pop()
	 	else:
	 		return False

	 def size(self):
	 	return len(self.S)


S = Stack()
S.add(1)
S.add(2)
S.size()
S.remove()
S.remove()
S.remove()
