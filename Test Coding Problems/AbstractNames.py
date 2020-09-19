#Write a function called abstract_names. abstract_names
#should have one parameter: a list of lists. Each list will
#be a list of strings, each with a first name and a last
#name, and each with the same first name.
#
#For example, this could be one list of lists your function
#might receive:
#
# [["David Joyner", "David Tennant", "David Beckham"],
#  ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"],
#  ["Inés Sainz", "Inés Suarez", "Inés Melchor"]]
#
#abstract_names should return a dictionary. The keys to the
#dictionary should be the first names, and the values should
#be lists of the associated last names. The last names should
#be sorted alphabetically.
#
#For example, with the list above, the dictionary returned by
#abstract_names would be:
#
# {"David": ["Beckham", "Joyner", "Tennant"],
#  "Ananya": ["Agarwal", "Birla", "Chatterjee", "Roy"],
#  "Inés": ["Melchor", "Sainz", "Suarez"]}


#Write your function here!

def abstract_names(names_list):
    # solution 1
    dictionary = {}
    for names in names_list:
        lst = []
        names.sort()
        for name in names:
            first, last = name.split()
            lst.append(last)
        dictionary[first] = lst
    return dictionary

    # solution 2
    # dictionary = {}
    # for full_name_list in names_list:
    #     full_name_list.sort()
    #     for full_name in full_name_list:
    #         first, last = full_name.split()
    #         dictionary.setdefault(first, [])
    #         dictionary[first].append(last) 
    # return dictionary

    # return {name.split()[0]:[name.split()[1] for name in names] for names in names_list for name in names}
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"David": ["Beckham", "Joyner", "Tennant"], "Ananya": ["Agarwal", "Birla", "Chatterjee", "Roy"], "Inés": ["Melchor", "Sainz", "Suarez"]}
names = [["David Joyner", "David Tennant", "David Beckham"], ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"], ["Ines Sainz", "Ines Suarez", "Ines Melchor"]]
print(abstract_names(names))
