#Write a function called count_types. count_types
#should take as input a single string, and return a
#dictionary. In the dictionary, the keys should be
#types of characters, and the values should be the
#number of times each type of character appeared in
#the string.
#
#The types of characters that should be handled (and
#thus, the keys in the dictionary) are:
#
# - upper: the count of upper-case or capital letters
# - lower: the count of lower-case letters
# - punctuation: the count of punctuation characters.
#   You may assume this is limited to these punctuation
#   characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# - space: the count of spaces
# - numeral: the count of numerals, 0123456789
#
#Note, however, that any type of character that does
#NOT appear in the string should not be in the dictionary
#at all.
#
#For example:
#
#count_characters("aabbccc") -> 
# {"lower": 7}
#count_characters("ABC 123 doe ray me!") -> 
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
#
#Because the first string has only lower-case letters,
#"lower" is the only key in the dictionary.
#
#HINT: If you're sing the ord() function, capitals of
#ordinals between 65 and 90; lower-case letters have
#ordinals between 97 and 122; numerals are between 48
#and 57; spaces are 32; all other numbers between 33
#and 126 are punctuations, and no character will have
#an ordinal outside that range.


#Write your function here!

def count_types(string_input):
    char_type_dict = {}
    # solution 1
    for char in string_input:
        # if 97 <= ord(char) <= 122:
        #     char_type_dict['lower'] = char_type_dict.get('lower', 0) + 1
        # elif 65 <= ord(char) <= 90:
        #     char_type_dict['upper'] = char_type_dict.get('upper', 0) + 1
        # elif 48 <= ord(char) <= 57:
        #     char_type_dict['numeral'] = char_type_dict.get('numeral', 0) + 1
        # elif ord(char) == 32:
        #     char_type_dict['space'] = char_type_dict.get('space', 0) + 1
        # # elif 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or \
        # #     91 <= ord(char) <= 96 or 123 <= ord(char) <= 126:
        # #     char_type_dict['punctuation'] = char_type_dict.get('punctuation', 0) + 1
        # else:
        #     char_type_dict['punctuation'] = char_type_dict.get('punctuation', 0) + 1
        #    
        # solution 2
        # if char.islower():
        #     char_type_dict['lower'] = char_type_dict.get('lower', 0) + 1
        # elif char.isupper():
        #     char_type_dict['upper'] = char_type_dict.get('upper', 0) + 1
        # elif char.isdigit():
        #     char_type_dict['numeral'] = char_type_dict.get('numeral', 0) + 1
        # elif char.isspace():
        #     char_type_dict['space'] = char_type_dict.get('space', 0) + 1
        # else:
        #     char_type_dict['punctuation'] = char_type_dict.get('punctuation', 0) + 1


        if 'Z' >= char >= 'A':
            char_type_dict.setdefault("upper", 0)
            char_type_dict["upper"] += 1
        elif 'z' >= char >= 'a':
            char_type_dict.setdefault("lower", 0)
            char_type_dict["lower"] += 1
        elif char == ' ':
            char_type_dict.setdefault("space", 0)
            char_type_dict["space"] += 1
        elif '9' >= char >= '0':
            char_type_dict.setdefault("numeral", 0)
            char_type_dict["numeral"] += 1
        else:
            char_type_dict.setdefault("punctuation", 0)
            char_type_dict["punctuation"] += 1

    return char_type_dict
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"lower": 7}
#{"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))
# print(ord('a'))