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
	
	def __init__(self, className, superClassName):
		self.className = className
		self.superClassName = superClassName
	
	def __str__(self):
		return self.printAST()
		
	def printAST(self):
		result = "Class: %s\nSuper Class: %s" % (self.className, self.superClassName)
		return result
		
	def setSuperClass(self, superClassName):
		self.superClassName = superClassName
		
	def setClass(self, className):
		self.className = className

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