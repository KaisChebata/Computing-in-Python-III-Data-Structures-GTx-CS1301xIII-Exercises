#Write a function called write_class_data. write_class_data
#will take as input two parameters: a string and a list of
#3-tuples.
#
#The string will represent the filename to which to write.
#
#Each 3-tuple in the list will contain three values:
#
# - A string representing the major of a college class (e.g.
#   "CS", "CHEM", "ENGL")
# - An integer representing a course number (e.g. 1301, 2241,
#   4001)
# - A string representing the name of a course (e.g.
#   "Introduction to Computing", "Organic Chemistry", etc.)
#
#write_class_data should write the list of classes to the file
#given by the filename using the following format:
#
# [major][number]: [class name]
#
#So, for this list:
#
# [("CS", 1301, "Introduction to Computing"),
#  ("CHEM", "1310", "General Chemistry")]
#
#The file printed would look like this:
#
# CS1301: Introduction to Computing
# CHEM1310: General Chemistry
#
#Note the specifics of that format: no space between the major
#and course number, no space between the course number and the
#colon, one space between the colon and the course name.
#
#We've included Sample.txt to show you what a longer version
#of one of these files might look like.


#Write your function here!


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
classes = [("CS", 1301, "Introduction to Computing"), ("CHEM", "1310", "General Chemistry")]
write_class_data("Test.txt", classes)
