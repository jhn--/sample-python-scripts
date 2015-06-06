def flip_bit(number, n):
	mask = (0b1 << n)
	print bin(mask)

	desired = number ^ mask
	return bin(desired)

print flip_bit(0b111, 2)
