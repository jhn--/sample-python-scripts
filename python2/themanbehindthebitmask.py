def check_bit4(inte):
	mask = 0b1000
	if (inte & mask):
		return "on"
	else:
		return "off"

print check_bit4(12)
#print check_bit4(bin(4))
print check_bit4(0b1000)