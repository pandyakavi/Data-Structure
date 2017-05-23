from Stack_Cls import Stack_Cls as stack

parseq = raw_input()
st = stack()
Balanced = True

for i in range(0,len(parseq)):
	if parseq[i] == "(":
		st.Push(parseq[i])
	else:
		if st.isEmpty() == True:
			Balanced = False
			break
		else:
			st.Pop()

if st.isEmpty() == True and Balanced == True:
	print("Balanced Paranthesis")
else:
	print("UN-Balanced Paranthesis")
		
