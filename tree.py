class Node:
	def __init__(self, value=0):
		self.left = None
		self.right = None
		self.value = value

	def compare(self,value):
		if value > self.value:
			if self.left:
				self.left.compare(value)
			else:
				self.left = Node(value)
		if value < self.value:
			if self.right:
				self.right.compare(value)
			else:
				self.right = Node(value)

class Tree:
	def __init__(self,value=0):
		self.root = Node(value) # Starting node

	def add_node(self,value):
		self.root.compare(value)

tree = Tree()
tree.add_node(20)
print(tree.root)

