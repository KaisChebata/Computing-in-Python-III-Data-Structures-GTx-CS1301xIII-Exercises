#Write a function called "scramble" that accepts a string
#as an argument and returns a new string. The new string 
#should start with the last half of the original string
#and end with the first half. 
#
#If the length of the string is odd, split the string 
#at the floor of the length / 2 (in other words, the second
#half is the longer half).
#
#For example:
#  scramble("abcd") -> "cdab"
#  screamble("abcde") -> "cdeab"
#  scramble("railroad")) -> "roadrail"
#  scramble("fireworks")) -> "worksfire"


#Write your function here!

# my solution:

# import math

# def scramble(a_string):
# 	half = math.ceil(len(a_string) / 2)
# 	return a_string[-half:] + a_string[:-half]

# given solution:

def scramble(word):
	midpoint = len(word) // 2

	first_half = word[:midpoint]
	second_half = word[midpoint:]

	return second_half + first_half

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the results you see in the examples above.

string1 = "abcd"
string2 = "abcde"
string3 = "railroad"
string4 = "fireworks"
print(string1 + " -> " + scramble(string1))
print(string2 + " -> " + scramble(string2))
print(string3 + " -> " + scramble(string3))
print(string4 + " -> " + scramble(string4))

mystring = 'Hello World'
print(mystring[11])
print(len(mystring))