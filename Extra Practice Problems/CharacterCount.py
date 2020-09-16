#Write a function called count_characters. count_characters
#should take as input a single string, and return a
#dictionary. In the dictionary, the keys should be
#characters, and the values should be the number of times
#each character appeared in the string.
#
#For example:
#
#  count_characters("aabbccc") -> {'a': 2, 'b': 2, 'c': 3}
#  count_characters("AaBbbb") -> {'A': 1, 'B': 1, 'a': 1, 'b': 3}
#
#You should not need to make any assumptions about the
#characters in the string: spaces, punctuation, line breaks,
#and any other characters should be handled automatically.
#You may count upper and lower case separately.


#Write your function here!

def count_characters(a_string):
    return {char:a_string.count(char) for char in a_string}

    # counter = {}
    # for char in a_string:
    #     counter[char] = counter.get(char, 0) + 1
    # return counter

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{'a': 2, 'b': 2, 'c': 3}
print(count_characters("aabbccc"))