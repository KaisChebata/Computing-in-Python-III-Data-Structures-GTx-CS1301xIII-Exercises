#Write a function called find_median. find_median
#should take as input a string representing a filename.
#The file corresponding to that filename will be a list
#of integers, one integer per line. find_median should
#return the median of the numbers in the file.
#
#If there is an odd number of values in the file, then
#find_median will return the middle value from the numbers
#in the file after they're sorted.
#
#If there is an even number of values in the file, then
#find_median should return the average of the two middle
#values after they're sorted.
#
#For example, in the dropdown in the top left you'll find a
#file named FindMedianInput.txt. There are 19 numbers in
#this file, so the median is the value at index 10 after
#sorting them: 16.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.


#Write your function here!

def find_median(file_name):
    with open(file_name, 'r') as file_reader:
        ints_lst = [int(line) for line in file_reader]
    ints_lst.sort()
    mid_point = len(ints_lst) // 2
    if len(ints_lst) % 2 == 0:
        return sum(ints_lst[mid_point -1:mid_point + 1]) / 2
    else:
        return ints_lst[mid_point]

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16
print(find_median(r"Test Coding Problems\\FindMedianInput.txt"))

# lst_1 = [1,4,2,5,0]
# lst_2 =[10,40,20,50]
# print(lst_1)
# lst_1.sort()
# print(lst_1)
# median = lst_1[len(lst_1)//2]
# print(median)
# print('----------------------')
# print(lst_2)
# lst_2.sort()
# print(lst_2)
# median1 = sum(lst_2[len(lst_2) // 2 - 1: len(lst_2) // 2 + 1]) / 2
# print(median1)