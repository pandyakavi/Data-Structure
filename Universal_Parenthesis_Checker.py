from Stack_Cls import Stack_Cls as stack

def Match(top,symbol):
	open_par = "([{"
	close_par = ")]}"

	return open_par.index(top) == close_par.index(symbol)

strn = raw_input()
arr = stack()

Balanced = True
for i in range(0,len(strn)):
	if strn[i] in "([{":
		arr.Push(strn[i])
	else:
		if arr.isEmpty() == True:
			Balanced = False; break
		else:
			top = arr.Pop()
			if Match(top,strn[i]) == False:
				Balanced = False; break		

if arr.isEmpty() == True and Balanced == True:
	print("Paranthesis are Balanced")
else:
	print("Paranthesis are UN-Balanced")


