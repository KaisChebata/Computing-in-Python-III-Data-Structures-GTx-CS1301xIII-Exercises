def save(file_name, inlist):
	output_file = open(file_name, 'w')
	for item in inlist:
		# output_file.write(item + '\n')
		print(item, file=output_file)
	output_file.close()

def load(file_name):
	lst = []
	input_file = open(file_name, 'r')

	for line in input_file:
		lst.append(line.strip())
	input_file.close()

	return lst

mylist = ["David", "Lucy", "Vrushali", "Ping", "Natalie",
          "Dana", "Addison", "Jasmine"]

save(r'Chapter 4.4 - File Input and Output\\saved_items.txt', mylist)
new_list = load(r'Chapter 4.4 - File Input and Output\\saved_items.txt')
print('new_list ->', new_list)