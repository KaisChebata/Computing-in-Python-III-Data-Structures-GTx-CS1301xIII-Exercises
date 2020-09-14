myint1 = 12
myint2 = 23
myint3 = 34

myList = ["David", "Lucy", "Vrushali", "Ping", 
          "Natalie", "Dana", "Addison", "Jasmine"]

output_file = open('output_file.txt', 'a')

for num in (myint1, myint2, myint3):
	output_file.write(str(num) + '\n')

for name in myList:
	print(name, file=output_file)

output_file.close()