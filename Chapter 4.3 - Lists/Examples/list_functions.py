mylist = [17, 12, 9, 18, 11, 19, 7, 13, 
			14, 16, 1, 10, 8, 4, 6, 3, 
			15, 2, 5, 20]

print('mylist:', mylist)
mylist.sort()
print('mylist after sorting:', mylist)
mylist.append(21)
print('mylist after appending 21 to it', mylist)
other_list = [26, 22, 23, 24]
print('other_list:', other_list)
mylist.extend(other_list)
print('mylist after extending with other_list:', mylist)
mylist.insert(15, 25)
print('mylist after inserting 25 at index 15:', mylist)
mylist.remove(26)
print('mylist after removing value 26:', mylist)
mylist.sort()
print('mylist after sorting again:', mylist)
mylist.reverse()
print('mylist after reversing:', mylist)
print('mylist.pop() ->', mylist.pop())
print('mylist after poping:', mylist)
del mylist[-5:]
print('after deleting the last five items:', mylist)
print(mylist.index(23), ': index of 23')
print(mylist.count(15), ': count of 15 in mylist')
print(4 in mylist, ': 4 in mylist')
print(25 in mylist, ': 25 in mylist')
myList1 = [1, 2, 3, -2, 0]
myList1.sort().reverse()
print(myList1)