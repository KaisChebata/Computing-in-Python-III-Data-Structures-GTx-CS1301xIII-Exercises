#Recall in the previous problem you counted the number of
#instances of a certain first name in a list of full names.
#You returned a dictionary with the name as the key, and the
#number of times it appeared as the value.
#
#Modify that code such that instead of having a count as the
#value, you instead have a list of the full names that had
#that first name. So, each key in the dictionary would still
#be a first name, but the values would be lists of names.
#Make sure to sort the list of names, too.
#
#Name this new function name_lists.


#Add your function here!

def name_lists(full_names_list):
    dict_names = {}
    # sol 1
    # for name in full_names_list:
    #     first_name = name.split()[0]
    #     dict_names[first_name] = sorted([n for n in full_names_list if n.split()[0] == first_name])

    # sol 2
    for name in full_names_list:
        first_name = name.split()[0]
        if first_name not in dict_names:
            dict_names[first_name] = []
        dict_names[first_name].append(name)
        
    for lst_names in dict_names.values():
        lst_names.sort()
    return dict_names

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Odle', 'Shelba Fry'],
#'David': ['David Joyner', 'David Zuber'], 'Brenton': ['Brenton Joyner', 'Brenton Zuber'],
#'Maren': ['Maren Fry'], 'Nicol': ['Nicol Barthel']}

name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
expect = {
'David': ['David Joyner', 'David Zuber'], 
'Brenton': ['Brenton Joyner', 'Brenton Zuber'], 
'Nicol': ['Nicol Barthel'], 
'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Fry', 'Shelba Odle'], 
'Maren': ['Maren Fry']
}
print('result   ->', name_lists(name_list))
print('----------------------------------------------------')
print('expected ->', expect)
print('----------------------------------------------------')
print(name_lists(name_list) == expect)


# {
# 'David': ['David Joyner', 'David Zuber'], 
# 'Brenton': ['Brenton Joyner', 'Brenton Zuber'], 
# 'Nicol': ['Nicol Barthel'], 
# 'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Odle', 'Shelba Fry'], 
# 'Maren': ['Maren Fry']}

# {
# 'David': ['David Joyner', 'David Zuber'], 
# 'Brenton': ['Brenton Joyner', 'Brenton Zuber'], 
# 'Nicol': ['Nicol Barthel'], 
# 'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Fry', 'Shelba Odle'], 
# 'Maren': ['Maren Fry']}

