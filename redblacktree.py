lass Node():
	def __init__(self, key):
		self.key = key
		self.color = "Red"
		self.left = None
		self.right = None
		self.parent = None
		self.height = 0

class RBTree():
	def __init__(self):
		self.root = None
		
	def add(self, key):
		if (self.root == None):
			self.root = Node(key)
			self.root.color = "Black"
			self.root.left = Node(None)
			self.root.left.color = "Black"
			self.root.left.parent = self.root
			self.root.right = Node(None)
			self.root.right.color = "Black"
			self.root.right.parent = self.root
		else:
			self.addNode(key, self.root)

	def addNode(self, key, node):
		if (key < node.key):
			if (node.left.key != None):
				self.addNode(key, node.left)
			else:
				node.left.key = key
				node.left.color = "Red"
				node.left.parent = node
				node.left.left = Node(None)
				node.left.left.color = "Black"
				node.left.left.parent = node.left
				node.left.right = Node(None)
				node.left.right.color = "Black"
				node.left.right.parent = node.right
		else:
			if (node.right.key != None):
				self.addNode(key, node.right)
			else:
				node.right.key = key
				node.right.color = "Red"	
				node.right.parent = node
				node.right.right = Node(None)
				node.right.right.color = "Black"
				node.right.right.parent = node.right
				node.right.left = Node(None)
				node.right.left.color = "Black"
				node.right.left.parent = node.right

		if node.left.key != None:
			self.fixTree(node.left)
		else:
			self.fixTree(node.right)

	def fixTree(self, node):
		while node != self.root and node.parent.color == "Red":
			if node.parent == node.parent.parent.left:
				uncle = node.parent.parent.right
				if uncle.color == "Red":
					node.parent.color = "Black"
					uncle.color = "Black"
					node.parent.parent.color = "Red"
					node = node.parent.parent
					self.root.color = "Black"
					return self.fixTree(node)
				else:
					if node == node.parent.right:
						node = node.parent
						self.leftrotate(node)
					node.parent.color = "Black"
					node.parent.parent.color = "Red"
					self.rightrotate(node.parent.parent)
			else:
				uncle = node.parent.parent.left
				if uncle.color == "Red":
					node.parent.color = "Black"
					uncle.color = "Black"
					node.parent.parent.color = "Red"
					node = node.parent.parent
					self.root.color = "Black"
					return self.fixTree(node)
				else:
					if node == node.parent.left:
						node = node.parent
						self.rightrotate(node)
					node.parent.color = "Black"
					node.parent.parent.color = "Red"
					self.leftrotate(node.parent.parent)
		self.root.color = "Black"

	def leftrotate(self, node):
		sibling = node.right
		node.right = sibling.left
	
		if sibling.left != None:
			sibling.left.parent = node
		sibling.parent = node.parent
		if node.parent == None:
			self.root = sibling
		else:
			if node == node.parent.left:
				node.parent.left = sibling
			else:
				node.parent.right = sibling
		sibling.left = node
		node.parent = sibling
		self.update_height(node)
		self.update_height(sibling)

	def rightrotate(self, node):
		sibling = node.left
		node.left = sibling.right

		if sibling.right != None:
			sibling.right.parent = node
		sibling.parent = node.parent
		if node.parent == None:
			self.root = sibling
		else:
			if node == node.parent.right:
				node.parent.right = sibling
			else:
				node.parent.left = sibling
		sibling.right = node
		node.parent = sibling
		self.update_height(node)
		self.update_height(sibling)

	def height(self, node):
		if (node == None):
			return 0
		else:
			return node.height

	def update_height(self, node):
		node.height = max(self.height(node.left), self.height(node.right)) + 1

	def printLevelOrder(self):
		h = self.height(self.root)
		for i in range(1, h + 3):
			self.printGivenLevel(self.root, i)
			print("\n")

	def printGivenLevel(self, node , level):
		if (node == None):
			return
		elif (level == 1):
			if node.key != None:
				print ("%d (%s)" %(node.key, node.color)),
		else:
			self.printGivenLevel(node.left , level - 1)
			self.printGivenLevel(node.right , level - 1)

tree = RBTree()
tree.add(43)
tree.add(9)
tree.add(0)
tree.add(-24)
tree.add(13)
tree.add(68)
tree.add(60)
tree.add(3)
tree.add(4)

tree.printLevelOrder()