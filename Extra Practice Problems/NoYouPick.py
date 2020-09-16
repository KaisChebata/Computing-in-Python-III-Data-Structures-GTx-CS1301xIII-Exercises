"""
Sense Experiment 2

The following problem is being used in an experiment to see 
how we can give better immediate personal feedback and partial credit on our autograded coding problems. 
It is helpful if you complete it so we can understand more about the types of approaches 
students take to this problem.
"""

#Write a function called no_you_pick. no_you_pick should have two parameters. 
# The first parameter is a dictionary where the keys are restaurant names and the values are lists of attributes of those restaurants as strings, such as "vegetarian", "vegan", and "gluten-free".
#
#The second parameter is a list of strings representing of necessary attributes of the restaurant you select.
#
#Return a list of restaurants from the dictionary who each contain all the diet restrictions listed in the list, sorted alphabetically. If there are no restaurants that meet all the restrictions, return the string
#"Sorry, no restaurants meet your restrictions". Types of diet restrictions that exist in this question's universe are: vegetarian, vegan, kosher, gluten-free, dairy-free
#
#For example:
#grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
#                 "jacob's pickles": ["vegetarian", "gluten-free"], \
#                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher"]}
#guests_diet = ["dairy-free"]
#no_you_pick(grading_scale, guests_diet) -> ["blossom"]


#Write your code here!



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: blossom
grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
                 "jacob's pickles": ["vegetarian", "gluten-free"], \
                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher"]}
guests_diet = ["dairy-free"]
print(no_you_pick(grading_scale, guests_diet))