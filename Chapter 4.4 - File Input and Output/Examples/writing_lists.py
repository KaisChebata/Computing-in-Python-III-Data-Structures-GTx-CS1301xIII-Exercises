# myint1 = 12
# myint2 = 23
# myint3 = 34

myList = ["David", "Lucy", "Vrushali", "Ping", 
          "Natalie", "Dana", "Addison", "Jasmine"]

# output_file = open('output_file.txt', 'w')
# output_file.write(str(myint1) + '\n')
# output_file.write(str(myint2) + '\n')
# output_file.write(str(myint3) + '\n')
# # output_file.writelines(myList)
# output_file.write('\n'.join(myList))
# # for name in myList:
# # 	output_file.write(name + '\n')

output_file = open(r'Chapter 4.4 - File Input and Output\\output_file.txt', 'w')
for name in myList:
	print(name, file=output_file)
output_file.close()
