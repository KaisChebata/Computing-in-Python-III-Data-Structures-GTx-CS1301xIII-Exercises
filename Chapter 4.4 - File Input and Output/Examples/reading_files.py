input_file = open(r"Chapter 4.4 - File Input and Output\\output_file.txt", 'r')
print(input_file.readline().strip())
print(input_file.readline().strip())
print('--------------------------------------')

for line in input_file.readlines():
	print(line.strip())

input_file.close()

print('--------------------------------------')

file_reader = open(r'Chapter 4.4 - File Input and Output\\nums.txt', 'r')
myint1 = int(file_reader.readline())
myint2 = int(file_reader.readline())
myint3 = int(file_reader.readline())

print('myint1 = ', myint1)
print('myint2 = ', myint2)
print('myint3 = ', myint3)
print(type(myint1))

file_reader.close()

