class Tree:
	nodes = []
	
	def __init__(self):
		self.nodes = []
	
	def __str__(self):
		return self.printTree()
		
	def printTree(self):
		result = ""
		for i in range(len(self.nodes)):
			result += "%s\n" % next(iter(self.nodes))
		return result
		
	def add_node(self, className, superClassName):
		tmpNode = Node(className, superClassName)
		self.nodes.append(tmpNode)
		return tmpNode
		
	def getNode_putClass(self, className):
		found_node = self.find_node_by_class(None)
		found_node.className = className
		return found_node
	
	def find_node_by_class(self, className):
		for i in range(len(self.nodes)):
			if self.nodes[i].className == className:
				return self.nodes[i]
		
		
class Node:
	"""
	Attributes:
		className: Name of the class
		superClassName: Name of super class
		constructors: List of constructors
		methods: List of methods
	"""
	className = 'None'
	superClassName = 'None'
	constructors = []
	methods = []
	
	def __init__(self, className, superClassName, constructors = None, methods = None):
		self.className = className
		self.superClassName = superClassName
	
	def __str__(self):
		return self.printNode()
		
	def printNode(self):
		result = "Class: %s\nSuper Class: %s" % (self.className, self.superClassName)
		return result
		
	def setSuperClass(self, superClassName):
		self.superClassName = superClassName
		return self
		
	def setClass(self, className):
		self = find_node_by_class(className)
		self.className = className
		return self

class classNode(Node):
	def __init__(self, className):
		Node.__init__(self, className, None)

class superClassNode(Node):
	def __init__(self, superClassName):
		Node.__init__(self, None, superClassName)		
		
class className(Node):
	def __init__(self, className, superClassName):
		self.className = className
		self.superClassName = superClassName
			
class constructors(Node):
	def __init__(self, constructors, constructor):
		self.constructors = constructors
		self.constructor = constructor
		
class constructor(Node):
	def __init__(self, constructor):
		self.constuctor = constructor
		
class methods(Node):
	def __init__(self, methods, method):
		self.methods = methods
		self.method = method

class method(Node):
	def __init__(self, method):
		self.method = method