def quotient_and_remainder(dividend, divisor):
	return (dividend // divisor, dividend % divisor)

mydividend = 11
mydivisor = 4

(myquotient, myremainder) = quotient_and_remainder(mydividend, mydivisor)

print('Quotient:', myquotient)
print('Remainder:', myremainder)