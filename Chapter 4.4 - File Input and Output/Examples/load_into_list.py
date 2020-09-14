lst = []

file_reader = open(r'Chapter 4.4 - File Input and Output\nums.txt', 'r')

for line in file_reader:
	lst.append(line.strip())
file_reader.close()

print(lst)

print('-----------------------------------')
mylist = []
output_file_reader = open(r'Chapter 4.4 - File Input and Output\\output_file.txt', 'r')
myint1 = int(output_file_reader.readline())
myint2 = int(output_file_reader.readline())
myint3 = int(output_file_reader.readline())

for line in output_file_reader:
	mylist.append(line.strip())

output_file_reader.close()

print('myint1 = {}, myint2 = {}, myint3 = {}'.format(myint1, myint2, myint3))
print('mylist ->', mylist)