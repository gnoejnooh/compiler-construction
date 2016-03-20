class ASTNode:
	className = ''
	superClassName = ''
	constructors = []
	methods = []
	
	def __init__(self, className):
		self.className = className
		
	def __str__(self):
		print(self)
	

class classNode(Node):
	def __init__(self, className):
		ASTNode.__init__(self, className)
		
class classHasSuperClass(Node):
	def __init__(self, className, superClassName):
		ASTNode.__init__(self, className)
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
