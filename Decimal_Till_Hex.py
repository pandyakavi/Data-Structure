from Stack_Cls import Stack_Cls as stack
#dividend / divisor = quotient
#12 / 3 = 4

remainder = stack()


dividend = int(raw_input())
divisor = int(raw_input())

digits = "0123456789ABCDEF"

while dividend//divisor >= 0:
	if dividend == 0:
		break
	else: 
		remainder.Push(digits[dividend%divisor])
		dividend//= divisor

remainder.Print()	

sum=0
for i in range(remainder.size()-1,-1,-1):
	sum+=digits.index(remainder.Pop())*(divisor**i)

print(sum)
