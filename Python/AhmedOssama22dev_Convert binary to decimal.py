#arg:int rtype:int
def bin_to_dec(n):
	bin=list(str(n))
	dec=0
	for i in range(len(bin)):
		if(int(bin[i])==1):
			dec+=2**i
	return dec
#Test
print(bin_to_dec(10101))
