# Peek, Pop, isEmpty, Push, size()

class Stack_Class:

	def __init__(self):
		self.items = []

	def Peek(self):
		return self.items[-1]

	def Pop(self):
		#k = self.items[-1]
		#self.items.remove(k)
		return self.items.pop()#k

	def isEmpty(self):
		return self.items == []

	def Push(self,val):
		self.items.append(val)

	def size(self):
		return len(self.items)

	def Print(self):
		print(self.items)
		
