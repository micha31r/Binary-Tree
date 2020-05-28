# Basic binary tree

import random

class Node:
	def __init__(self, value=0):
		self.left = None
		self.right = None
		self.value = value

	def add_node(self,value):
		if value > self.value:
			if self.left:
				self.left.add_node(value)
			else:
				self.left = Node(value)
		elif value < self.value:
			if self.right:
				self.right.add_node(value)
			else:
				self.right = Node(value)

	def find(self,value):
		print(self.value,value)
		if value < self.value:
			if self.right:
				return self.right.find(value)
		elif value > self.value:
			if self.left:
				return self.left.find(value)
		else:
			return True
		return False

	def cycle(self):
		if self.right:
			self.right.cycle()
		print(self.value)
		if self.left:
			self.left.cycle()

class Tree:
	def __init__(self):
		self.root = None # Starting node

	def add_value(self,value):
		if not self.root:
			self.root = Node(value)
		else:
			self.root.add_node(value)

	def exsist(self,value):
		return self.root.find(value)

	def sort(self):
		self.root.cycle()

tree = Tree()

# Add random values to the binary tree
for i in range(random.randint(10,50)):
	tree.add_value(random.randint(0,500))

# Sort numbers from smallest to biggest
tree.sort()

