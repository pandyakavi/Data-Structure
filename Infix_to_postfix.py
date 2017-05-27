
"""
#Infix to postfix algorithm

-> Things needed
	a. Empty Stack to push operators
	b. Empty list to append operands and operators other than '(' and ')'
	c. String to specify what are the operators
	d. Define the precedence of opeartors

-> Functioning of Algorithms
	1. Scan the input from left to right. If the input is operand then append to the list
	2. If input is '(' then push it to the stack
	3. If input is ')' pop the stack untill and unless '(' is found. Append the poped item to the end of the list
	4. If the input is in "*/+-" then if the current stack item has high precendence then pop that and append to list and then push 	this input to stack
	5. When all the items are scanned then if stack is not yet empty then pop the remaining items and append it to the output list.
"""
from Stack_Cls import Stack_Cls as Stack

inpt = raw_input()
stak = Stack()
otpt_lst = []
operators = "*/-+()"
precedence = {"*":3, "/":3, "+":2, "-":2, "(":1}

for item in inpt:
	if item not in operators:
		otpt_lst.append(item)
	elif item == "(":
		stak.Push(item)
	elif item == ")":
		token = stak.Pop()
		while token != "(":
			otpt_lst.append(token)
			token = stak.Pop()
	else:
		while stak.isEmpty() == False and precedence[stak.Peek()] >= precedence[item]:
			otpt_lst.append(stak.Pop())
		stak.Push(item)

while stak.isEmpty() == False:
	otpt_lst.append(stak.Pop())

print " ".join(otpt_lst)
		

"""
POSTFIX EVALUATION

->Things Needed
	a. Create an empty stack to store operands and their evaluated results

->Functioning of an Algorithm
	1. Scan the items of postfix expression from left to right
	2. If the item is operand then push it in the stack
	3. If the item is operator "+-/*" then pop two value/operands from stack. First poped item is Operand1 and second popped is Operand2
	4. Identify the kind of operator
	5. Perform Operand2(Operator)Operand1
	6. Push the result of step 5 in an stack
	
7. When all the items are scanned Stack will contain only one vale which is the final result. Pop the stack and print that value 

"""

def EvaluateMe(operator,Operand1,Operand2):
	if operator == "*":
		return Operand2 * Operand1
	elif operator == "/":
		return Operand2 / Operand1
	elif operator == "+":
		return Operand2 + Operand1
	elif operator == "-":
		return Operand2 - Operand1


postfix = " ".join(otpt_lst)
postfix = postfix.split(" ")
stk = Stack()

for item in postfix:
	if item not in operators:
		stk.Push(item)
	else:
		Operand1 = stk.Pop()
		Operand2 = stk.Pop()
		Result = EvaluateMe(item,int(Operand1),int(Operand2))
		stk.Push(Result)

print(stk.Pop())
