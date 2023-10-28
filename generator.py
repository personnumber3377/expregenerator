
import random


MAX_DEPTH = 5 # Maximum nesting for braces.


# < <= = == != >= >

COMPARISON_TYPES = [["<", 1], ["<=", 1], [">", 1], [">=", 1], ["=", 1], ["==", 1], ["!=", 1]]


LOGIC_TYPES = [["|", 1], ["&", 1]]



NODE_TYPES = [["+", 1], ["-", 1], ["*", 1], ["%", 1], ["placeholder", 2]]+LOGIC_TYPES+COMPARISON_TYPES # This list is of the format [OPERATOR, UNARY/BINARY] (Binary operation is one and unary is zero and two means number)



MAX_NUM = 100000

ZERO_CHANCE = 0.2 # This is a special case for the number zero. The number zero is special because it has a lot of edge cases so I have put a 30 percent chance for it to occur.

class ExprTree:
	def __init__(self):
		
		self.start_node = None

	def grow(self):

		self.start_node = ExprNode(0)

	def get_expression(self):

		return self.start_node.get_value()

class ExprNode:
	
	def __init__(self, cur_layer, node_type=None, max_layer=MAX_DEPTH):
		
		if node_type == None:
			node_type = random.choice(NODE_TYPES)

		self.left = None
		self.right = None
		self.val = None

		binary = node_type[1]

		if binary == 2: # This is actually a number.
			if random.random() < ZERO_CHANCE:
				self.val = 0
			else:
				self.val = random.randrange(0, MAX_NUM) # get random number
			return
		# We are not a number, so we are not a in a terminal node aka leaf

		operation = node_type[0]

		self.val = operation # assign operand to the value of this node.

		override = None
		if cur_layer == max_layer - 1:
			override = ["placeholder", 2] # Force all of the subsequent nodes to be number leafs :)


		self.left = ExprNode(cur_layer+1, node_type=override, max_layer=max_layer)

		self.right = ExprNode(cur_layer+1, node_type=override, max_layer=max_layer)

		return


	def get_value(self):
		
		if self.left == None and self.right == None: # Just get the value of this node because terminal node.
			#if self.val < 0:

			#	return "( - "+str(abs(self.val))+" )"
			#else:
			assert self.val >= 0 # Negative values not allowed :)
			return "( "+str(self.val)+" )"
		else:
			return "( "+str(self.left.get_value())+" "+str(self.val)+" "+str(self.right.get_value())+" )"






def gen_expr() -> str:
	tree = ExprTree()
	tree.grow()
	expression = tree.get_expression()
	return expression


def main() -> None:
	expression = gen_expr()
	print(expression)
	return 0

if __name__=="__main__":
	exit(main())