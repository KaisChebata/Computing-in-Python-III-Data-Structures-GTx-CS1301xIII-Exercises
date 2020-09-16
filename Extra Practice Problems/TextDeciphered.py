"""
Sense Experiment 5

The following problem is being used in an experiment to see 
how we can give better immediate personal feedback and partial credit on our autograded coding problems. 
It is helpful if you complete it so we can understand more about the types of approaches 
students take to this problem.
"""

#For this question, your goal is to decipher a text message to plain English.
#You can ignore grammar, you're just translating common text slang into
#normal words.
#
#Write a function called text_deciphered. text_deciphered should have two
#parameters: a string representing a text message, and a dictionary representing
#a set of known abbreviations. In this dictionary, the keys are the English words
#and the values are the abbreviated words.
#
#Return a translated version of the string, replacing the abbreviated words with
#the real English words.
#
#For example:
#text_message = "Hey, wat r our plans for tn"
#abbrevs = {"what": "wat", "are": "r", "tonight": "tn"}
#text_deciphered(text_message, abbrevs) -> "Hey, what are our plans for tonight"


#Write your code here!



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Hey, what are our plans for tonight
text_message = "Hey, wat r our plans for tn"
abbrevs = {"what": "wat", "are": "r", "tonight": "tn"}
print(text_deciphered(text_message, abbrevs))