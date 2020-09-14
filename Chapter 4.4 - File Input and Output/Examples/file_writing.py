myint1, myint2, myint3 = 12, 23, 34

output_file = open(r'Chapter 4.4 - File Input and Output\\output_file.txt', 'w')
output_file.write(str(myint1))
output_file.write(str(myint2))
output_file.write(str(myint3))
output_file.close()

print(type(output_file))

# Exercise 1
string1 = 'Hi!'
string2 = 'Hey!'
string3 = 'Hello!'

file = open(r'Chapter 4.4 - File Input and Output\\my_file.txt', 'w')
file.write(string1)
file.write(string2)
file.write(string3)
file.close()