from Stack_Class import Stack_Class as stack
#dividend / divisor = quotient
#12 / 3 = 4

remainder = stack()


dividend = int(raw_input())
divisor = 2

while dividend//divisor >= 0:
	if dividend == 0:
		break
	else: 
		remainder.Push(dividend%divisor)
		dividend//= divisor

remainder.Print()	

sum=0
for i in range(remainder.size()-1,-1,-1):
	sum+=remainder.Pop()*(divisor**i)

print(sum)
